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
import threading
from bstack_utils.helper import bstack11l1l1l1l1_opy_
from bstack_utils.constants import bstack1l11111ll11_opy_, EVENTS, STAGE
from bstack_utils.bstack1111ll11l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l1lll1lll_opy_:
    bstack111llll1ll1_opy_ = None
    @classmethod
    def bstack1ll111l1ll_opy_(cls):
        if cls.on() and os.getenv(bstack1l1l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤḊ")):
            logger.info(
                bstack1l1l111_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨḋ").format(os.getenv(bstack1l1l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦḌ"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫḍ"), None) is None or os.environ[bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬḎ")] == bstack1l1l111_opy_ (u"ࠤࡱࡹࡱࡲࠢḏ"):
            return False
        return True
    @classmethod
    def bstack111l1ll1ll1_opy_(cls, bs_config, framework=bstack1l1l111_opy_ (u"ࠥࠦḐ")):
        bstack1l111l111ll_opy_ = False
        for fw in bstack1l11111ll11_opy_:
            if fw in framework:
                bstack1l111l111ll_opy_ = True
        return bstack11l1l1l1l1_opy_(bs_config.get(bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨḑ"), bstack1l111l111ll_opy_))
    @classmethod
    def bstack111l1ll11l1_opy_(cls, framework):
        return framework in bstack1l11111ll11_opy_
    @classmethod
    def bstack111ll1l1ll1_opy_(cls, bs_config, framework):
        return cls.bstack111l1ll1ll1_opy_(bs_config, framework) is True and cls.bstack111l1ll11l1_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩḒ"), None)
    @staticmethod
    def bstack11l11l1ll1_opy_():
        if getattr(threading.current_thread(), bstack1l1l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪḓ"), None):
            return {
                bstack1l1l111_opy_ (u"ࠧࡵࡻࡳࡩࠬḔ"): bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹ࠭ḕ"),
                bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩḖ"): getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧḗ"), None)
            }
        if getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨḘ"), None):
            return {
                bstack1l1l111_opy_ (u"ࠬࡺࡹࡱࡧࠪḙ"): bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࠫḚ"),
                bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧḛ"): getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬḜ"), None)
            }
        return None
    @staticmethod
    def bstack111l1ll11ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1lll1lll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11l111111l_opy_(test, hook_name=None):
        bstack111l1ll1111_opy_ = test.parent
        if hook_name in [bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧḝ"), bstack1l1l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫḞ"), bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪḟ"), bstack1l1l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧḠ")]:
            bstack111l1ll1111_opy_ = test
        scope = []
        while bstack111l1ll1111_opy_ is not None:
            scope.append(bstack111l1ll1111_opy_.name)
            bstack111l1ll1111_opy_ = bstack111l1ll1111_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack111l1ll1l11_opy_(hook_type):
        if hook_type == bstack1l1l111_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦḡ"):
            return bstack1l1l111_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦḢ")
        elif hook_type == bstack1l1l111_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧḣ"):
            return bstack1l1l111_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤḤ")
    @staticmethod
    def bstack111l1ll111l_opy_(bstack111l1l11l_opy_):
        try:
            if not bstack1l1lll1lll_opy_.on():
                return bstack111l1l11l_opy_
            if os.environ.get(bstack1l1l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣḥ"), None) == bstack1l1l111_opy_ (u"ࠦࡹࡸࡵࡦࠤḦ"):
                tests = os.environ.get(bstack1l1l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤḧ"), None)
                if tests is None or tests == bstack1l1l111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦḨ"):
                    return bstack111l1l11l_opy_
                bstack111l1l11l_opy_ = tests.split(bstack1l1l111_opy_ (u"ࠧ࠭ࠩḩ"))
                return bstack111l1l11l_opy_
        except Exception as exc:
            logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤḪ") + str(str(exc)) + bstack1l1l111_opy_ (u"ࠤࠥḫ"))
        return bstack111l1l11l_opy_