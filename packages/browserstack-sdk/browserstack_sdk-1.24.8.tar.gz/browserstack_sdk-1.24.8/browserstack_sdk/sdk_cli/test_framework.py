# coding: UTF-8
import sys
bstack11lll_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack1l111l_opy_ = 7
def bstack1l1l111_opy_ (bstack111l_opy_):
    global bstack1ll1ll_opy_
    bstack1l11l_opy_ = ord (bstack111l_opy_ [-1])
    bstack11l11_opy_ = bstack111l_opy_ [:-1]
    bstack111lll_opy_ = bstack1l11l_opy_ % len (bstack11l11_opy_)
    bstack1ll11ll_opy_ = bstack11l11_opy_ [:bstack111lll_opy_] + bstack11l11_opy_ [bstack111lll_opy_:]
    if bstack11lll_opy_:
        bstack11l111l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack1l11lll_opy_ + bstack1l11l_opy_) % bstack1l111l_opy_) for bstack1l11lll_opy_, char in enumerate (bstack1ll11ll_opy_)])
    else:
        bstack11l111l_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack1l11lll_opy_ + bstack1l11l_opy_) % bstack1l111l_opy_) for bstack1l11lll_opy_, char in enumerate (bstack1ll11ll_opy_)])
    return eval (bstack11l111l_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1111l111ll_opy_ import bstack11111llll1_opy_, bstack11111l11ll_opy_
class bstack1lllll11111_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1l111_opy_ (u"࡙ࠦ࡫ࡳࡵࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᑕ").format(self.name)
class bstack111111l111_opy_(Enum):
    NONE = 0
    BEFORE_ALL = 1
    LOG = 2
    SETUP_FIXTURE = 3
    INIT_TEST = 4
    BEFORE_EACH = 5
    AFTER_EACH = 6
    TEST = 7
    STEP = 8
    LOG_REPORT = 9
    AFTER_ALL = 10
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1l111_opy_ (u"࡚ࠧࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᑖ").format(self.name)
class bstack1111111l1l_opy_(bstack11111llll1_opy_):
    bstack1lll1111l1l_opy_: List[str]
    bstack1l11ll111ll_opy_: Dict[str, str]
    state: bstack111111l111_opy_
    bstack11111lll1l_opy_: datetime
    bstack1111l11l11_opy_: datetime
    def __init__(
        self,
        context: bstack11111l11ll_opy_,
        bstack1lll1111l1l_opy_: List[str],
        bstack1l11ll111ll_opy_: Dict[str, str],
        state=bstack111111l111_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1lll1111l1l_opy_ = bstack1lll1111l1l_opy_
        self.bstack1l11ll111ll_opy_ = bstack1l11ll111ll_opy_
        self.state = state
        self.bstack11111lll1l_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1111l11l11_opy_ = datetime.now(tz=timezone.utc)
    def bstack1111lllll1_opy_(self, bstack1111l1l1l1_opy_: bstack111111l111_opy_):
        bstack1111l1l11l_opy_ = bstack111111l111_opy_(bstack1111l1l1l1_opy_).name
        if not bstack1111l1l11l_opy_:
            return False
        if bstack1111l1l1l1_opy_ == self.state:
            return False
        self.state = bstack1111l1l1l1_opy_
        self.bstack1111l11l11_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1l11l1lllll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1lllll111ll_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1ll1ll1ll11_opy_ = bstack1l1l111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡺࡻࡩࡥࠤᑗ")
    bstack1l1l111l1l1_opy_ = bstack1l1l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡯ࡤࠣᑘ")
    bstack1ll1l1l1ll1_opy_ = bstack1l1l111_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠦᑙ")
    bstack1l1l111lll1_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡤࡶࡡࡵࡪࠥᑚ")
    bstack1l11ll11111_opy_ = bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡶࡤ࡫ࡸࠨᑛ")
    bstack1l1ll11llll_opy_ = bstack1l1l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᑜ")
    bstack1ll111lll11_opy_ = bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡹࡵ࡭ࡶࡢࡥࡹࠨᑝ")
    bstack1ll111ll111_opy_ = bstack1l1l111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᑞ")
    bstack1ll11l111ll_opy_ = bstack1l1l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᑟ")
    bstack1l11l1lll1l_opy_ = bstack1l1l111_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᑠ")
    bstack1ll1lllll1l_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠣᑡ")
    bstack1ll11l1l11l_opy_ = bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᑢ")
    bstack1l11ll1lll1_opy_ = bstack1l1l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡦࡳࡩ࡫ࠢᑣ")
    bstack1l1llll1l1l_opy_ = bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠢᑤ")
    bstack1ll1llll111_opy_ = bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᑥ")
    bstack1l1ll1l1l11_opy_ = bstack1l1l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࠨᑦ")
    bstack1l11llll1l1_opy_ = bstack1l1l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠧᑧ")
    bstack1l11ll1ll1l_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡭ࡱࡪࡷࠧᑨ")
    bstack1l11ll11l11_opy_ = bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡯ࡨࡸࡦࠨᑩ")
    bstack1l11l1l1ll1_opy_ = bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡶࡧࡴࡶࡥࡴࠩᑪ")
    bstack1l1l1ll111l_opy_ = bstack1l1l111_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᑫ")
    bstack1l11ll1l1l1_opy_ = bstack1l1l111_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᑬ")
    bstack1l11l1llll1_opy_ = bstack1l1l111_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᑭ")
    bstack1l11lll11l1_opy_ = bstack1l1l111_opy_ (u"ࠣࡪࡲࡳࡰࡥࡩࡥࠤᑮ")
    bstack1l11lllll1l_opy_ = bstack1l1l111_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡧࡶࡹࡱࡺࠢᑯ")
    bstack1l1l111l1ll_opy_ = bstack1l1l111_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠ࡮ࡲ࡫ࡸࠨᑰ")
    bstack1l11ll1ll11_opy_ = bstack1l1l111_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠢᑱ")
    bstack1l1l1111l1l_opy_ = bstack1l1l111_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᑲ")
    bstack1l1l11111l1_opy_ = bstack1l1l111_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᑳ")
    bstack1ll11l1ll11_opy_ = bstack1l1l111_opy_ (u"ࠢࡕࡇࡖࡘࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࠤᑴ")
    bstack1ll1111ll11_opy_ = bstack1l1l111_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡌࡐࡉࠥᑵ")
    bstack1111lll11l_opy_: Dict[str, bstack1111111l1l_opy_] = dict()
    bstack1l11l11ll11_opy_: Dict[str, List[Callable]] = dict()
    bstack1lll1111l1l_opy_: List[str]
    bstack1l11ll111ll_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1lll1111l1l_opy_: List[str],
        bstack1l11ll111ll_opy_: Dict[str, str],
    ):
        self.bstack1lll1111l1l_opy_ = bstack1lll1111l1l_opy_
        self.bstack1l11ll111ll_opy_ = bstack1l11ll111ll_opy_
    def track_event(
        self,
        context: bstack1l11l1lllll_opy_,
        test_framework_state: bstack111111l111_opy_,
        test_hook_state: bstack1lllll11111_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᑶ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠥࠦᑷ"))
    def bstack1l1l11ll1ll_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1l11lllll_opy_ = TestFramework.bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_)
        if not bstack1l1l11lllll_opy_ in TestFramework.bstack1l11l11ll11_opy_:
            return
        self.logger.debug(bstack1l1l111_opy_ (u"ࠦ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࠢᑸ") + str(len(TestFramework.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_])) + bstack1l1l111_opy_ (u"ࠧࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࡴࠤᑹ"))
        for callback in TestFramework.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_]:
            try:
                callback(self, instance, bstack11111l1l1l_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1l1l111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࠦᑺ") + str(e) + bstack1l1l111_opy_ (u"ࠢࠣᑻ"))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll111l1lll_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll11lll11l_opy_(self, instance, bstack11111l1l1l_opy_):
        return
    @abc.abstractmethod
    def bstack1ll111ll1l1_opy_(self, instance, bstack11111l1l1l_opy_):
        return
    @staticmethod
    def bstack11111l1lll_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack11111llll1_opy_.create_context(target)
        instance = TestFramework.bstack1111lll11l_opy_.get(ctx.id, None)
        if instance and instance.bstack1111l11lll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1ll11l1llll_opy_(reverse=True) -> List[bstack1111111l1l_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1111lll11l_opy_.values(),
            ),
            key=lambda t: t.bstack11111lll1l_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111l1ll1l_opy_(ctx: bstack11111l11ll_opy_, reverse=True) -> List[bstack1111111l1l_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1111lll11l_opy_.values(),
            ),
            key=lambda t: t.bstack11111lll1l_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111l1lll1_opy_(instance: bstack1111111l1l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack1111l111l1_opy_(instance: bstack1111111l1l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1111lllll1_opy_(instance: bstack1111111l1l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l1l111_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣ࡯ࡪࡿ࠽ࡼ࡭ࡨࡽࢂࠦࡶࡢ࡮ࡸࡩࡂࠨᑼ") + str(value) + bstack1l1l111_opy_ (u"ࠤࠥᑽ"))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l11lll1l1l_opy_(instance: bstack1111111l1l_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥ࡯ࡶࡵ࡭ࡪࡹ࠽ࠣᑾ") + str(entries) + bstack1l1l111_opy_ (u"ࠦࠧᑿ"))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l11l11l1l1_opy_(instance: bstack111111l111_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l1l111_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣ࡯ࡪࡿ࠽ࡼ࡭ࡨࡽࢂࠦࡶࡢ࡮ࡸࡩࡂࠨᒀ") + str(value) + bstack1l1l111_opy_ (u"ࠨࠢᒁ"))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack11111l1lll_opy_(target, strict)
        return TestFramework.bstack1111l111l1_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack11111l1lll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l1l111l11l_opy_(instance: bstack1111111l1l_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1l11lll1111_opy_(instance: bstack1111111l1l_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_]):
        return bstack1l1l111_opy_ (u"ࠢ࠻ࠤᒂ").join((bstack111111l111_opy_(bstack11111l1l1l_opy_[0]).name, bstack1lllll11111_opy_(bstack11111l1l1l_opy_[1]).name))
    @staticmethod
    def bstack1ll1ll1ll1l_opy_(bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_], callback: Callable):
        bstack1l1l11lllll_opy_ = TestFramework.bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_)
        TestFramework.logger.debug(bstack1l1l111_opy_ (u"ࠣࡵࡨࡸࡤ࡮࡯ࡰ࡭ࡢࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡨࡰࡱ࡮ࡣࡷ࡫ࡧࡪࡵࡷࡶࡾࡥ࡫ࡦࡻࡀࠦᒃ") + str(bstack1l1l11lllll_opy_) + bstack1l1l111_opy_ (u"ࠤࠥᒄ"))
        if not bstack1l1l11lllll_opy_ in TestFramework.bstack1l11l11ll11_opy_:
            TestFramework.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_] = []
        TestFramework.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_].append(callback)
    @staticmethod
    def bstack1ll111ll1ll_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡵ࡫ࡱࡷࠧᒅ"):
            return klass.__qualname__
        return module + bstack1l1l111_opy_ (u"ࠦ࠳ࠨᒆ") + klass.__qualname__
    @staticmethod
    def bstack1ll111l1l1l_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}