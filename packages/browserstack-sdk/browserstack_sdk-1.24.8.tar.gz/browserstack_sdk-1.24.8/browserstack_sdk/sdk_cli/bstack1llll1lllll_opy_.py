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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l1111_opy_,
    bstack1111ll11ll_opy_,
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1llll11lll1_opy_(bstack11111l1111_opy_):
    bstack1l1l1l11ll1_opy_ = bstack1l1l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢዳ")
    bstack1l1lll1lll1_opy_ = bstack1l1l111_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣዴ")
    bstack1l1llll11l1_opy_ = bstack1l1l111_opy_ (u"ࠤ࡫ࡹࡧࡥࡵࡳ࡮ࠥድ")
    bstack1l1lll11l11_opy_ = bstack1l1l111_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤዶ")
    bstack1l1l1l11lll_opy_ = bstack1l1l111_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࠢዷ")
    bstack1l1l1l11l1l_opy_ = bstack1l1l111_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࡢࡵࡼࡲࡨࠨዸ")
    NAME = bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥዹ")
    bstack1l1l1l111ll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1l11l1l_opy_: Any
    bstack1l1l1l1111l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1l1l111_opy_ (u"ࠢ࡭ࡣࡸࡲࡨ࡮ࠢዺ"), bstack1l1l111_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤዻ"), bstack1l1l111_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦዼ"), bstack1l1l111_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤዽ"), bstack1l1l111_opy_ (u"ࠦࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠨዾ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack11111lllll_opy_(methods)
    def bstack11111ll1l1_opy_(self, instance: bstack1111ll11ll_opy_, method_name: str, bstack1111l1llll_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1111ll1111_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1111ll1l11_opy_, bstack1l1l1l11111_opy_ = bstack11111l1l1l_opy_
        bstack1l1l11lllll_opy_ = bstack1llll11lll1_opy_.bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_)
        if bstack1l1l11lllll_opy_ in bstack1llll11lll1_opy_.bstack1l1l1l111ll_opy_:
            bstack1l1l11llll1_opy_ = None
            for callback in bstack1llll11lll1_opy_.bstack1l1l1l111ll_opy_[bstack1l1l11lllll_opy_]:
                try:
                    bstack1l1l1l11l11_opy_ = callback(self, target, exec, bstack11111l1l1l_opy_, result, *args, **kwargs)
                    if bstack1l1l11llll1_opy_ == None:
                        bstack1l1l11llll1_opy_ = bstack1l1l1l11l11_opy_
                except Exception as e:
                    self.logger.error(bstack1l1l111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࠥዿ") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢጀ"))
                    traceback.print_exc()
            if bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.PRE and callable(bstack1l1l11llll1_opy_):
                return bstack1l1l11llll1_opy_
            elif bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.POST and bstack1l1l11llll1_opy_:
                return bstack1l1l11llll1_opy_
    def bstack1111llll1l_opy_(
        self, method_name, previous_state: bstack11111l11l1_opy_, *args, **kwargs
    ) -> bstack11111l11l1_opy_:
        if method_name == bstack1l1l111_opy_ (u"ࠧ࡭ࡣࡸࡲࡨ࡮ࠧጁ") or method_name == bstack1l1l111_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࠩጂ") or method_name == bstack1l1l111_opy_ (u"ࠩࡱࡩࡼࡥࡰࡢࡩࡨࠫጃ"):
            return bstack11111l11l1_opy_.bstack1111ll1lll_opy_
        if method_name == bstack1l1l111_opy_ (u"ࠪࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠬጄ"):
            return bstack11111l11l1_opy_.bstack1111l1l1ll_opy_
        if method_name == bstack1l1l111_opy_ (u"ࠫࡨࡲ࡯ࡴࡧࠪጅ"):
            return bstack11111l11l1_opy_.QUIT
        return bstack11111l11l1_opy_.NONE
    @staticmethod
    def bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_]):
        return bstack1l1l111_opy_ (u"ࠧࡀࠢጆ").join((bstack11111l11l1_opy_(bstack11111l1l1l_opy_[0]).name, bstack1111llll11_opy_(bstack11111l1l1l_opy_[1]).name))
    @staticmethod
    def bstack1ll1ll1ll1l_opy_(bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_], callback: Callable):
        bstack1l1l11lllll_opy_ = bstack1llll11lll1_opy_.bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_)
        if not bstack1l1l11lllll_opy_ in bstack1llll11lll1_opy_.bstack1l1l1l111ll_opy_:
            bstack1llll11lll1_opy_.bstack1l1l1l111ll_opy_[bstack1l1l11lllll_opy_] = []
        bstack1llll11lll1_opy_.bstack1l1l1l111ll_opy_[bstack1l1l11lllll_opy_].append(callback)
    @staticmethod
    def bstack1ll1ll111ll_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1ll1lll1l11_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1ll1ll111l1_opy_(instance: bstack1111ll11ll_opy_, default_value=None):
        return bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, bstack1llll11lll1_opy_.bstack1l1lll11l11_opy_, default_value)
    @staticmethod
    def bstack1ll1l1l1l11_opy_(instance: bstack1111ll11ll_opy_) -> bool:
        return True
    @staticmethod
    def bstack1ll1lll11l1_opy_(instance: bstack1111ll11ll_opy_, default_value=None):
        return bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, bstack1llll11lll1_opy_.bstack1l1llll11l1_opy_, default_value)
    @staticmethod
    def bstack1ll1ll1l1ll_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll1ll11111_opy_(method_name: str, *args):
        if not bstack1llll11lll1_opy_.bstack1ll1ll111ll_opy_(method_name):
            return False
        if not bstack1llll11lll1_opy_.bstack1l1l1l11lll_opy_ in bstack1llll11lll1_opy_.bstack1l1l1ll1l1l_opy_(*args):
            return False
        bstack1ll1l1l11l1_opy_ = bstack1llll11lll1_opy_.bstack1ll1l11lll1_opy_(*args)
        return bstack1ll1l1l11l1_opy_ and bstack1l1l111_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨጇ") in bstack1ll1l1l11l1_opy_ and bstack1l1l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣገ") in bstack1ll1l1l11l1_opy_[bstack1l1l111_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣጉ")]
    @staticmethod
    def bstack1ll1ll1l111_opy_(method_name: str, *args):
        if not bstack1llll11lll1_opy_.bstack1ll1ll111ll_opy_(method_name):
            return False
        if not bstack1llll11lll1_opy_.bstack1l1l1l11lll_opy_ in bstack1llll11lll1_opy_.bstack1l1l1ll1l1l_opy_(*args):
            return False
        bstack1ll1l1l11l1_opy_ = bstack1llll11lll1_opy_.bstack1ll1l11lll1_opy_(*args)
        return (
            bstack1ll1l1l11l1_opy_
            and bstack1l1l111_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤጊ") in bstack1ll1l1l11l1_opy_
            and bstack1l1l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡤࡴ࡬ࡴࡹࠨጋ") in bstack1ll1l1l11l1_opy_[bstack1l1l111_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦጌ")]
        )
    @staticmethod
    def bstack1l1l1ll1l1l_opy_(*args):
        return str(bstack1llll11lll1_opy_.bstack1ll1ll1l1ll_opy_(*args)).lower()