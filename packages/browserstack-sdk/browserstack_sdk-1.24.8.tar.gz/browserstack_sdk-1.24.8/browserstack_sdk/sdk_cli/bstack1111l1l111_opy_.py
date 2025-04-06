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
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1111l111ll_opy_ import bstack11111llll1_opy_, bstack11111l11ll_opy_
import os
import threading
class bstack1111llll11_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1l111_opy_ (u"ࠦࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥ࿒").format(self.name)
class bstack11111l11l1_opy_(Enum):
    NONE = 0
    bstack1111ll1lll_opy_ = 1
    bstack1111l1l1ll_opy_ = 3
    bstack1111ll1ll1_opy_ = 4
    bstack1111lll1ll_opy_ = 5
    QUIT = 6
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1l111_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧ࿓").format(self.name)
class bstack1111ll11ll_opy_(bstack11111llll1_opy_):
    framework_name: str
    framework_version: str
    state: bstack11111l11l1_opy_
    previous_state: bstack11111l11l1_opy_
    bstack11111lll1l_opy_: datetime
    bstack1111l11l11_opy_: datetime
    def __init__(
        self,
        context: bstack11111l11ll_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack11111l11l1_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack11111l11l1_opy_.NONE
        self.bstack11111lll1l_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1111l11l11_opy_ = datetime.now(tz=timezone.utc)
    def bstack1111lllll1_opy_(self, bstack1111l1l1l1_opy_: bstack11111l11l1_opy_):
        bstack1111l1l11l_opy_ = bstack11111l11l1_opy_(bstack1111l1l1l1_opy_).name
        if not bstack1111l1l11l_opy_:
            return False
        if bstack1111l1l1l1_opy_ == self.state:
            return False
        if self.state == bstack11111l11l1_opy_.bstack1111l1l1ll_opy_: # bstack11111l1l11_opy_ bstack1111l11111_opy_ for bstack1111l11l1l_opy_ in bstack11111ll111_opy_, it bstack1111l1ll11_opy_ bstack1111ll11l1_opy_ bstack11111l1ll1_opy_ times bstack1111ll1l1l_opy_ a new state
            return True
        if (
            bstack1111l1l1l1_opy_ == bstack11111l11l1_opy_.NONE
            or (self.state != bstack11111l11l1_opy_.NONE and bstack1111l1l1l1_opy_ == bstack11111l11l1_opy_.bstack1111ll1lll_opy_)
            or (self.state < bstack11111l11l1_opy_.bstack1111ll1lll_opy_ and bstack1111l1l1l1_opy_ == bstack11111l11l1_opy_.bstack1111ll1ll1_opy_)
            or (self.state < bstack11111l11l1_opy_.bstack1111ll1lll_opy_ and bstack1111l1l1l1_opy_ == bstack11111l11l1_opy_.QUIT)
        ):
            raise ValueError(bstack1l1l111_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡶࡤࡸࡪࠦࡴࡳࡣࡱࡷ࡮ࡺࡩࡰࡰ࠽ࠤࠧ࿔") + str(self.state) + bstack1l1l111_opy_ (u"ࠢࠡ࠿ࡁࠤࠧ࿕") + str(bstack1111l1l1l1_opy_))
        self.previous_state = self.state
        self.state = bstack1111l1l1l1_opy_
        self.bstack1111l11l11_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack11111l1111_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1111lll11l_opy_: Dict[str, bstack1111ll11ll_opy_] = dict()
    framework_name: str
    framework_version: str
    classes: List[Type]
    def __init__(
        self,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
    ):
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.classes = classes
    @abc.abstractmethod
    def bstack11111ll1l1_opy_(self, instance: bstack1111ll11ll_opy_, method_name: str, bstack1111l1llll_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1111llll1l_opy_(
        self, method_name, previous_state: bstack11111l11l1_opy_, *args, **kwargs
    ) -> bstack11111l11l1_opy_:
        return
    @abc.abstractmethod
    def bstack1111ll1111_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack11111lllll_opy_(self, bstack1111l11ll1_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1111l11ll1_opy_:
                bstack11111lll11_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11111lll11_opy_):
                    self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡷࡱࡴࡦࡺࡣࡩࡧࡧࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࠨ࿖") + str(method_name) + bstack1l1l111_opy_ (u"ࠤࠥ࿗"))
                    continue
                bstack1111ll1l11_opy_ = self.bstack1111llll1l_opy_(
                    method_name, previous_state=bstack11111l11l1_opy_.NONE
                )
                bstack1111lll111_opy_ = self.bstack1111ll111l_opy_(
                    method_name,
                    (bstack1111ll1l11_opy_ if bstack1111ll1l11_opy_ else bstack11111l11l1_opy_.NONE),
                    bstack11111lll11_opy_,
                )
                if not callable(bstack1111lll111_opy_):
                    self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠣࡲࡴࡺࠠࡱࡣࡷࡧ࡭࡫ࡤ࠻ࠢࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࠫࡿࡸ࡫࡬ࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀ࠾ࠥࠨ࿘") + str(self.framework_version) + bstack1l1l111_opy_ (u"ࠦ࠮ࠨ࿙"))
                    continue
                setattr(clazz, method_name, bstack1111lll111_opy_)
    def bstack1111ll111l_opy_(
        self,
        method_name: str,
        bstack1111ll1l11_opy_: bstack11111l11l1_opy_,
        bstack11111lll11_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1111ll11_opy_ = datetime.now()
            (bstack1111ll1l11_opy_,) = wrapped.__vars__
            bstack1111ll1l11_opy_ = (
                bstack1111ll1l11_opy_
                if bstack1111ll1l11_opy_ and bstack1111ll1l11_opy_ != bstack11111l11l1_opy_.NONE
                else self.bstack1111llll1l_opy_(method_name, previous_state=bstack1111ll1l11_opy_, *args, **kwargs)
            )
            if bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.bstack1111ll1lll_opy_:
                ctx = bstack11111llll1_opy_.create_context(self.bstack1111l1111l_opy_(target))
                if not self.bstack11111l111l_opy_() or ctx.id not in bstack11111l1111_opy_.bstack1111lll11l_opy_:
                    bstack11111l1111_opy_.bstack1111lll11l_opy_[ctx.id] = bstack1111ll11ll_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1111ll1l11_opy_
                    )
                self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡣࡳࡧࡤࡸࡪࡪ࠺ࠡࡽࡷࡥࡷ࡭ࡥࡵ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨ࿚") + str(bstack11111l1111_opy_.bstack1111lll11l_opy_.keys()) + bstack1l1l111_opy_ (u"ࠨࠢ࿛"))
            else:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡ࡫ࡱࡺࡴࡱࡥࡥ࠼ࠣࡿࡹࡧࡲࡨࡧࡷ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤ࿜") + str(bstack11111l1111_opy_.bstack1111lll11l_opy_.keys()) + bstack1l1l111_opy_ (u"ࠣࠤ࿝"))
            instance = bstack11111l1111_opy_.bstack11111l1lll_opy_(self.bstack1111l1111l_opy_(target))
            if bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.NONE or not instance:
                ctx = bstack11111llll1_opy_.create_context(self.bstack1111l1111l_opy_(target))
                self.logger.warning(bstack1l1l111_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡹࡳࡺࡲࡢࡥ࡮ࡩࡩࡀࠠࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨ࿞") + str(bstack11111l1111_opy_.bstack1111lll11l_opy_.keys()) + bstack1l1l111_opy_ (u"ࠥࠦ࿟"))
                return bstack11111lll11_opy_(target, *args, **kwargs)
            bstack1111lll1l1_opy_ = self.bstack1111ll1111_opy_(
                target,
                (instance, method_name),
                (bstack1111ll1l11_opy_, bstack1111llll11_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1111lllll1_opy_(bstack1111ll1l11_opy_):
                self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠥࡹࡴࡢࡶࡨ࠱ࡹࡸࡡ࡯ࡵ࡬ࡸ࡮ࡵ࡮࠻ࠢࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡶࡲࡦࡸ࡬ࡳࡺࡹ࡟ࡴࡶࡤࡸࡪࢃࠠ࠾ࡀࠣࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡳࡵࡣࡷࡩࢂࠦࠨࡼࡶࡼࡴࡪ࠮ࡴࡢࡴࡪࡩࡹ࠯ࡽ࠯ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡽࡤࡶ࡬ࡹࡽࠪࠢ࡞ࠦ࿠") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠧࡣࠢ࿡"))
            result = (
                bstack1111lll1l1_opy_(target, bstack11111lll11_opy_, *args, **kwargs)
                if callable(bstack1111lll1l1_opy_)
                else bstack11111lll11_opy_(target, *args, **kwargs)
            )
            bstack11111ll11l_opy_ = self.bstack1111ll1111_opy_(
                target,
                (instance, method_name),
                (bstack1111ll1l11_opy_, bstack1111llll11_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack11111ll1l1_opy_(instance, method_name, datetime.now() - bstack1111ll11_opy_, *args, **kwargs)
            return bstack11111ll11l_opy_ if bstack11111ll11l_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1111ll1l11_opy_,)
        return wrapped
    @staticmethod
    def bstack11111l1lll_opy_(target: object, strict=True):
        ctx = bstack11111llll1_opy_.create_context(target)
        instance = bstack11111l1111_opy_.bstack1111lll11l_opy_.get(ctx.id, None)
        if instance and instance.bstack1111l11lll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1111l1ll1l_opy_(
        ctx: bstack11111l11ll_opy_, state: bstack11111l11l1_opy_, reverse=True
    ) -> List[bstack1111ll11ll_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack11111l1111_opy_.bstack1111lll11l_opy_.values(),
            ),
            key=lambda t: t.bstack11111lll1l_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111l1lll1_opy_(instance: bstack1111ll11ll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack1111l111l1_opy_(instance: bstack1111ll11ll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1111lllll1_opy_(instance: bstack1111ll11ll_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack11111l1111_opy_.logger.debug(bstack1l1l111_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡ࡭ࡨࡽࡂࢁ࡫ࡦࡻࢀࠤࡻࡧ࡬ࡶࡧࡀࠦ࿢") + str(value) + bstack1l1l111_opy_ (u"ࠢࠣ࿣"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack11111l1111_opy_.bstack11111l1lll_opy_(target, strict)
        return bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack11111l1111_opy_.bstack11111l1lll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack11111l111l_opy_(self):
        return self.framework_name == bstack1l1l111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬ࿤")
    def bstack1111l1111l_opy_(self, target):
        return target if not self.bstack11111l111l_opy_() else self.bstack11111ll1ll_opy_()
    @staticmethod
    def bstack11111ll1ll_opy_():
        return str(os.getpid()) + str(threading.get_ident())