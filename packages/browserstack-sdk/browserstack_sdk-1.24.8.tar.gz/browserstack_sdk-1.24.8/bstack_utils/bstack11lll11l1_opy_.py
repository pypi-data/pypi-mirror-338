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
import threading
import logging
import bstack_utils.accessibility as bstack11l1l1lll_opy_
from bstack_utils.helper import bstack1l11ll111l_opy_
logger = logging.getLogger(__name__)
def bstack1l11llllll_opy_(bstack1ll1lll11_opy_):
  return True if bstack1ll1lll11_opy_ in threading.current_thread().__dict__.keys() else False
def bstack1l111llll1_opy_(context, *args):
    tags = getattr(args[0], bstack1l1l111_opy_ (u"ࠧࡵࡣࡪࡷࠬᕔ"), [])
    bstack1ll1111l1_opy_ = bstack11l1l1lll_opy_.bstack1l1l1l1ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack1ll1111l1_opy_
    try:
      bstack1llllll1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11llllll_opy_(bstack1l1l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧᕕ")) else context.browser
      if bstack1llllll1ll_opy_ and bstack1llllll1ll_opy_.session_id and bstack1ll1111l1_opy_ and bstack1l11ll111l_opy_(
              threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᕖ"), None):
          threading.current_thread().isA11yTest = bstack11l1l1lll_opy_.bstack1l111ll11l_opy_(bstack1llllll1ll_opy_, bstack1ll1111l1_opy_)
    except Exception as e:
       logger.debug(bstack1l1l111_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡧ࠱࠲ࡻࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪᕗ").format(str(e)))
def bstack1l1l1ll1_opy_(bstack1llllll1ll_opy_):
    if bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨᕘ"), None) and bstack1l11ll111l_opy_(
      threading.current_thread(), bstack1l1l111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᕙ"), None) and not bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"࠭ࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࠩᕚ"), False):
      threading.current_thread().a11y_stop = True
      bstack11l1l1lll_opy_.bstack11llllllll_opy_(bstack1llllll1ll_opy_, name=bstack1l1l111_opy_ (u"ࠢࠣᕛ"), path=bstack1l1l111_opy_ (u"ࠣࠤᕜ"))