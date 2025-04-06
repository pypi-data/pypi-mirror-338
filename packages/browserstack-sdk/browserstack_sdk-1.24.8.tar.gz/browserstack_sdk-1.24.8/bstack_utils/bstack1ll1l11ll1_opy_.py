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
from browserstack_sdk.bstack11llll111_opy_ import bstack1l11l111_opy_
from browserstack_sdk.bstack111ll1llll_opy_ import RobotHandler
def bstack1l11l1111_opy_(framework):
    if framework.lower() == bstack1l1l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᢏ"):
        return bstack1l11l111_opy_.version()
    elif framework.lower() == bstack1l1l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᢐ"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l1l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᢑ"):
        import behave
        return behave.__version__
    else:
        return bstack1l1l111_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬᢒ")
def bstack1llllll1l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l1l111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧᢓ"))
        framework_version.append(importlib.metadata.version(bstack1l1l111_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᢔ")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l1l111_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᢕ"))
        framework_version.append(importlib.metadata.version(bstack1l1l111_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᢖ")))
    except:
        pass
    return {
        bstack1l1l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᢗ"): bstack1l1l111_opy_ (u"ࠪࡣࠬᢘ").join(framework_name),
        bstack1l1l111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᢙ"): bstack1l1l111_opy_ (u"ࠬࡥࠧᢚ").join(framework_version)
    }