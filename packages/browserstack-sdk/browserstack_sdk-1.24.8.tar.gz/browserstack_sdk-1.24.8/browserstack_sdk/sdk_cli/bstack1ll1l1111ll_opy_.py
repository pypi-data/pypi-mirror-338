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
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack11111l1111_opy_,
    bstack1111ll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1111l111ll_opy_ import bstack11111l11ll_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
import weakref
class bstack1ll1l111l11_opy_(bstack1lllll1l111_opy_):
    bstack1ll11lll1ll_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1111ll11ll_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1111ll11ll_opy_]]
    def __init__(self, bstack1ll11lll1ll_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1l111lll_opy_ = dict()
        self.bstack1ll11lll1ll_opy_ = bstack1ll11lll1ll_opy_
        self.frameworks = frameworks
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1lll_opy_, bstack1111llll11_opy_.POST), self.__1ll1l111l1l_opy_)
        if any(bstack1lll1l11lll_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_(
                (bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.PRE), self.__1ll11llll11_opy_
            )
            bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_(
                (bstack11111l11l1_opy_.QUIT, bstack1111llll11_opy_.POST), self.__1ll1l111111_opy_
            )
    def __1ll1l111l1l_opy_(
        self,
        f: bstack1llll11lll1_opy_,
        bstack1ll1l11111l_opy_: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1l1l111_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᅢ"):
                return
            contexts = bstack1ll1l11111l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1l1l111_opy_ (u"ࠨࡡࡣࡱࡸࡸ࠿ࡨ࡬ࡢࡰ࡮ࠦᅣ") in page.url:
                                self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡔࡶࡲࡶ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡴࡥࡸࠢࡳࡥ࡬࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠤᅤ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, self.bstack1ll11lll1ll_opy_, True)
                                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡡࡢࡳࡳࡥࡰࡢࡩࡨࡣ࡮ࡴࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᅥ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠤࠥᅦ"))
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡲࡪࡽࠠࡱࡣࡪࡩࠥࡀࠢᅧ"),e)
    def __1ll11llll11_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, self.bstack1ll11lll1ll_opy_, False):
            return
        if not f.bstack1ll1l11l1l1_opy_(f.hub_url(driver)):
            self.bstack1ll1l111lll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, self.bstack1ll11lll1ll_opy_, True)
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣ࡮ࡴࡩࡵ࠼ࠣࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᅨ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠧࠨᅩ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, self.bstack1ll11lll1ll_opy_, True)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡩ࡯࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᅪ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠢࠣᅫ"))
    def __1ll1l111111_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll11llllll_opy_(instance)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡳࡸ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᅬ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠤࠥᅭ"))
    def bstack1ll1l1111l1_opy_(self, context: bstack11111l11ll_opy_, reverse=True) -> List[Tuple[Callable, bstack1111ll11ll_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll11lllll1_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lll1l11lll_opy_.bstack1ll1l1l1l11_opy_(data[1])
                    and data[1].bstack1ll11lllll1_opy_(context)
                    and getattr(data[0](), bstack1l1l111_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᅮ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack11111lll1l_opy_, reverse=reverse)
    def bstack1ll1l111ll1_opy_(self, context: bstack11111l11ll_opy_, reverse=True) -> List[Tuple[Callable, bstack1111ll11ll_opy_]]:
        matches = []
        for data in self.bstack1ll1l111lll_opy_.values():
            if (
                data[1].bstack1ll11lllll1_opy_(context)
                and getattr(data[0](), bstack1l1l111_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣᅯ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack11111lll1l_opy_, reverse=reverse)
    def bstack1ll11llll1l_opy_(self, instance: bstack1111ll11ll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll11llllll_opy_(self, instance: bstack1111ll11ll_opy_) -> bool:
        if self.bstack1ll11llll1l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, self.bstack1ll11lll1ll_opy_, False)
            return True
        return False