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
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1l111llllll_opy_, bstack1l1lll1ll_opy_, get_host_info, bstack11ll1ll1lll_opy_, \
 bstack111l111l1_opy_, bstack1l11ll111l_opy_, bstack111lllll1l_opy_, bstack11lll11l11l_opy_, bstack1ll11l1ll1_opy_
import bstack_utils.accessibility as bstack11l1l1lll_opy_
from bstack_utils.bstack11l11ll1ll_opy_ import bstack1l1lll1lll_opy_
from bstack_utils.percy import bstack1lll1l1l1l_opy_
from bstack_utils.config import Config
bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
logger = logging.getLogger(__name__)
percy = bstack1lll1l1l1l_opy_()
@bstack111lllll1l_opy_(class_method=False)
def bstack111ll1l1111_opy_(bs_config, bstack1llll1l1_opy_):
  try:
    data = {
        bstack1l1l111_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ᷌"): bstack1l1l111_opy_ (u"࠭ࡪࡴࡱࡱࠫ᷍"),
        bstack1l1l111_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ᷎࠭"): bs_config.get(bstack1l1l111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ᷏࠭"), bstack1l1l111_opy_ (u"᷐ࠩࠪ")),
        bstack1l1l111_opy_ (u"ࠪࡲࡦࡳࡥࠨ᷑"): bs_config.get(bstack1l1l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ᷒"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l1l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᷓ"): bs_config.get(bstack1l1l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᷔ")),
        bstack1l1l111_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᷕ"): bs_config.get(bstack1l1l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫᷖ"), bstack1l1l111_opy_ (u"ࠩࠪᷗ")),
        bstack1l1l111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᷘ"): bstack1ll11l1ll1_opy_(),
        bstack1l1l111_opy_ (u"ࠫࡹࡧࡧࡴࠩᷙ"): bstack11ll1ll1lll_opy_(bs_config),
        bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨᷚ"): get_host_info(),
        bstack1l1l111_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧᷛ"): bstack1l1lll1ll_opy_(),
        bstack1l1l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᷜ"): os.environ.get(bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᷝ")),
        bstack1l1l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧᷞ"): os.environ.get(bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨᷟ"), False),
        bstack1l1l111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭ᷠ"): bstack1l111llllll_opy_(),
        bstack1l1l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷡ"): bstack111l1lll1ll_opy_(),
        bstack1l1l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪᷢ"): bstack111l1llll1l_opy_(bstack1llll1l1_opy_),
        bstack1l1l111_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬᷣ"): bstack11l11111_opy_(bs_config, bstack1llll1l1_opy_.get(bstack1l1l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩᷤ"), bstack1l1l111_opy_ (u"ࠩࠪᷥ"))),
        bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷦ"): bstack111l111l1_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack1l1l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧᷧ").format(str(error)))
    return None
def bstack111l1llll1l_opy_(framework):
  return {
    bstack1l1l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬᷨ"): framework.get(bstack1l1l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧᷩ"), bstack1l1l111_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧᷪ")),
    bstack1l1l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᷫ"): framework.get(bstack1l1l111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᷬ")),
    bstack1l1l111_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧᷭ"): framework.get(bstack1l1l111_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᷮ")),
    bstack1l1l111_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧᷯ"): bstack1l1l111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᷰ"),
    bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᷱ"): framework.get(bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᷲ"))
  }
def bstack11l11111_opy_(bs_config, framework):
  bstack1l11lll1l_opy_ = False
  bstack11lll1l111_opy_ = False
  bstack111l1lll111_opy_ = False
  if bstack1l1l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ᷳ") in bs_config:
    bstack111l1lll111_opy_ = True
  elif bstack1l1l111_opy_ (u"ࠪࡥࡵࡶࠧᷴ") in bs_config:
    bstack1l11lll1l_opy_ = True
  else:
    bstack11lll1l111_opy_ = True
  bstack1lll1l1l_opy_ = {
    bstack1l1l111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ᷵"): bstack1l1lll1lll_opy_.bstack111l1ll1ll1_opy_(bs_config, framework),
    bstack1l1l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᷶"): bstack11l1l1lll_opy_.bstack1l11l111ll1_opy_(bs_config),
    bstack1l1l111_opy_ (u"࠭ࡰࡦࡴࡦࡽ᷷ࠬ"): bs_config.get(bstack1l1l111_opy_ (u"ࠧࡱࡧࡵࡧࡾ᷸࠭"), False),
    bstack1l1l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧ᷹ࠪ"): bstack11lll1l111_opy_,
    bstack1l1l111_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ᷺"): bstack1l11lll1l_opy_,
    bstack1l1l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ᷻"): bstack111l1lll111_opy_
  }
  return bstack1lll1l1l_opy_
@bstack111lllll1l_opy_(class_method=False)
def bstack111l1lll1ll_opy_():
  try:
    bstack111l1ll1lll_opy_ = json.loads(os.getenv(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ᷼"), bstack1l1l111_opy_ (u"ࠬࢁࡽࠨ᷽")))
    return {
        bstack1l1l111_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ᷾"): bstack111l1ll1lll_opy_
    }
  except Exception as error:
    logger.error(bstack1l1l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ᷿").format(str(error)))
    return {}
def bstack111ll1l111l_opy_(array, bstack111l1llll11_opy_, bstack111l1lllll1_opy_):
  result = {}
  for o in array:
    key = o[bstack111l1llll11_opy_]
    result[key] = o[bstack111l1lllll1_opy_]
  return result
def bstack111ll111111_opy_(bstack1l11ll1111_opy_=bstack1l1l111_opy_ (u"ࠨࠩḀ")):
  bstack111l1lll1l1_opy_ = bstack11l1l1lll_opy_.on()
  bstack111l1llllll_opy_ = bstack1l1lll1lll_opy_.on()
  bstack111l1lll11l_opy_ = percy.bstack1llll11lll_opy_()
  if bstack111l1lll11l_opy_ and not bstack111l1llllll_opy_ and not bstack111l1lll1l1_opy_:
    return bstack1l11ll1111_opy_ not in [bstack1l1l111_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ḁ"), bstack1l1l111_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧḂ")]
  elif bstack111l1lll1l1_opy_ and not bstack111l1llllll_opy_:
    return bstack1l11ll1111_opy_ not in [bstack1l1l111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬḃ"), bstack1l1l111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧḄ"), bstack1l1l111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪḅ")]
  return bstack111l1lll1l1_opy_ or bstack111l1llllll_opy_ or bstack111l1lll11l_opy_
@bstack111lllll1l_opy_(class_method=False)
def bstack111ll111l1l_opy_(bstack1l11ll1111_opy_, test=None):
  bstack111l1ll1l1l_opy_ = bstack11l1l1lll_opy_.on()
  if not bstack111l1ll1l1l_opy_ or bstack1l11ll1111_opy_ not in [bstack1l1l111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩḆ")] or test == None:
    return None
  return {
    bstack1l1l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨḇ"): bstack111l1ll1l1l_opy_ and bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨḈ"), None) == True and bstack11l1l1lll_opy_.bstack1l1l1l1ll_opy_(test[bstack1l1l111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨḉ")])
  }