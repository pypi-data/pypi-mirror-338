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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack1l111ll1l1l_opy_ as bstack1l111ll1l11_opy_, EVENTS
from bstack_utils.bstack11l1l1ll1l_opy_ import bstack11l1l1ll1l_opy_
from bstack_utils.helper import bstack1ll11l1ll1_opy_, bstack111ll1111l_opy_, bstack111l111l1_opy_, bstack1l11l1111ll_opy_, \
  bstack1l11l111111_opy_, bstack1l1lll1ll_opy_, get_host_info, bstack1l111llllll_opy_, bstack1l1l1lll_opy_, bstack111lllll1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1111ll11l_opy_ import get_logger
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
logger = get_logger(__name__)
bstack1111l1ll1_opy_ = bstack1llll11ll11_opy_()
@bstack111lllll1l_opy_(class_method=False)
def _1l11l11l111_opy_(driver, bstack111l1l1lll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l1l111_opy_ (u"ࠨࡱࡶࡣࡳࡧ࡭ࡦࠩᒊ"): caps.get(bstack1l1l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᒋ"), None),
        bstack1l1l111_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᒌ"): bstack111l1l1lll_opy_.get(bstack1l1l111_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᒍ"), None),
        bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫᒎ"): caps.get(bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᒏ"), None),
        bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᒐ"): caps.get(bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᒑ"), None)
    }
  except Exception as error:
    logger.debug(bstack1l1l111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭ᒒ") + str(error))
  return response
def on():
    if os.environ.get(bstack1l1l111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᒓ"), None) is None or os.environ[bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᒔ")] == bstack1l1l111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᒕ"):
        return False
    return True
def bstack1l11l111ll1_opy_(config):
  return config.get(bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᒖ"), False) or any([p.get(bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᒗ"), False) == True for p in config.get(bstack1l1l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᒘ"), [])])
def bstack1111llll1_opy_(config, bstack1l11ll11l_opy_):
  try:
    if not bstack111l111l1_opy_(config):
      return False
    bstack1l11l111l11_opy_ = config.get(bstack1l1l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᒙ"), False)
    if int(bstack1l11ll11l_opy_) < len(config.get(bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᒚ"), [])) and config[bstack1l1l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᒛ")][bstack1l11ll11l_opy_]:
      bstack1l11l11111l_opy_ = config[bstack1l1l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᒜ")][bstack1l11ll11l_opy_].get(bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᒝ"), None)
    else:
      bstack1l11l11111l_opy_ = config.get(bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᒞ"), None)
    if bstack1l11l11111l_opy_ != None:
      bstack1l11l111l11_opy_ = bstack1l11l11111l_opy_
    bstack1l111ll11l1_opy_ = os.getenv(bstack1l1l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᒟ")) is not None and len(os.getenv(bstack1l1l111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᒠ"))) > 0 and os.getenv(bstack1l1l111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᒡ")) != bstack1l1l111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᒢ")
    return bstack1l11l111l11_opy_ and bstack1l111ll11l1_opy_
  except Exception as error:
    logger.debug(bstack1l1l111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻ࡫ࡲࡪࡨࡼ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬᒣ") + str(error))
  return False
def bstack1l1l1l1ll_opy_(test_tags):
  bstack1ll1ll11l1l_opy_ = os.getenv(bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᒤ"))
  if bstack1ll1ll11l1l_opy_ is None:
    return True
  bstack1ll1ll11l1l_opy_ = json.loads(bstack1ll1ll11l1l_opy_)
  try:
    include_tags = bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒥ")] if bstack1l1l111_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒦ") in bstack1ll1ll11l1l_opy_ and isinstance(bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒧ")], list) else []
    exclude_tags = bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒨ")] if bstack1l1l111_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒩ") in bstack1ll1ll11l1l_opy_ and isinstance(bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒪ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l1l111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨᒫ") + str(error))
  return False
def bstack1l111llll11_opy_(config, bstack1l111ll11ll_opy_, bstack1l111lll1ll_opy_, bstack1l111ll1lll_opy_):
  bstack1l111ll111l_opy_ = bstack1l11l1111ll_opy_(config)
  bstack1l11l111lll_opy_ = bstack1l11l111111_opy_(config)
  if bstack1l111ll111l_opy_ is None or bstack1l11l111lll_opy_ is None:
    logger.error(bstack1l1l111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨᒬ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᒭ"), bstack1l1l111_opy_ (u"ࠩࡾࢁࠬᒮ")))
    data = {
        bstack1l1l111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᒯ"): config[bstack1l1l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᒰ")],
        bstack1l1l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᒱ"): config.get(bstack1l1l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᒲ"), os.path.basename(os.getcwd())),
        bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡚ࡩ࡮ࡧࠪᒳ"): bstack1ll11l1ll1_opy_(),
        bstack1l1l111_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ᒴ"): config.get(bstack1l1l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᒵ"), bstack1l1l111_opy_ (u"ࠪࠫᒶ")),
        bstack1l1l111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᒷ"): {
            bstack1l1l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬᒸ"): bstack1l111ll11ll_opy_,
            bstack1l1l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᒹ"): bstack1l111lll1ll_opy_,
            bstack1l1l111_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᒺ"): __version__,
            bstack1l1l111_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪᒻ"): bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᒼ"),
            bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᒽ"): bstack1l1l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ᒾ"),
            bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬᒿ"): bstack1l111ll1lll_opy_
        },
        bstack1l1l111_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨᓀ"): settings,
        bstack1l1l111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨᓁ"): bstack1l111llllll_opy_(),
        bstack1l1l111_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨᓂ"): bstack1l1lll1ll_opy_(),
        bstack1l1l111_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫᓃ"): get_host_info(),
        bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᓄ"): bstack111l111l1_opy_(config)
    }
    headers = {
        bstack1l1l111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᓅ"): bstack1l1l111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᓆ"),
    }
    config = {
        bstack1l1l111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᓇ"): (bstack1l111ll111l_opy_, bstack1l11l111lll_opy_),
        bstack1l1l111_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᓈ"): headers
    }
    response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᓉ"), bstack1l111ll1l11_opy_ + bstack1l1l111_opy_ (u"ࠩ࠲ࡺ࠷࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩᓊ"), data, config)
    bstack1l11l111l1l_opy_ = response.json()
    if bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫᓋ")]:
      parsed = json.loads(os.getenv(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᓌ"), bstack1l1l111_opy_ (u"ࠬࢁࡽࠨᓍ")))
      parsed[bstack1l1l111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᓎ")] = bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠧࡥࡣࡷࡥࠬᓏ")][bstack1l1l111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓐ")]
      os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᓑ")] = json.dumps(parsed)
      bstack11l1l1ll1l_opy_.bstack1l111lll111_opy_(bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠪࡨࡦࡺࡡࠨᓒ")][bstack1l1l111_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᓓ")])
      bstack11l1l1ll1l_opy_.bstack1l111lll11l_opy_(bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠬࡪࡡࡵࡣࠪᓔ")][bstack1l1l111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨᓕ")])
      bstack11l1l1ll1l_opy_.store()
      return bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠧࡥࡣࡷࡥࠬᓖ")][bstack1l1l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭ᓗ")], bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠩࡧࡥࡹࡧࠧᓘ")][bstack1l1l111_opy_ (u"ࠪ࡭ࡩ࠭ᓙ")]
    else:
      logger.error(bstack1l1l111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠬᓚ") + bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᓛ")])
      if bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᓜ")] == bstack1l1l111_opy_ (u"ࠧࡊࡰࡹࡥࡱ࡯ࡤࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡲࡤࡷࡸ࡫ࡤ࠯ࠩᓝ"):
        for bstack1l111lllll1_opy_ in bstack1l11l111l1l_opy_[bstack1l1l111_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᓞ")]:
          logger.error(bstack1l111lllll1_opy_[bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᓟ")])
      return None, None
  except Exception as error:
    logger.error(bstack1l1l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠦᓠ") +  str(error))
    return None, None
def bstack1l111ll1111_opy_():
  if os.getenv(bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᓡ")) is None:
    return {
        bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᓢ"): bstack1l1l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᓣ"),
        bstack1l1l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᓤ"): bstack1l1l111_opy_ (u"ࠨࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢ࡫ࡥࡩࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠧᓥ")
    }
  data = {bstack1l1l111_opy_ (u"ࠩࡨࡲࡩ࡚ࡩ࡮ࡧࠪᓦ"): bstack1ll11l1ll1_opy_()}
  headers = {
      bstack1l1l111_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᓧ"): bstack1l1l111_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࠬᓨ") + os.getenv(bstack1l1l111_opy_ (u"ࠧࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠥᓩ")),
      bstack1l1l111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᓪ"): bstack1l1l111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᓫ")
  }
  response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠨࡒࡘࡘࠬᓬ"), bstack1l111ll1l11_opy_ + bstack1l1l111_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠵ࡳࡵࡱࡳࠫᓭ"), data, { bstack1l1l111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫᓮ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l1l111_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯ࠢࡰࡥࡷࡱࡥࡥࠢࡤࡷࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠡࡣࡷࠤࠧᓯ") + bstack111ll1111l_opy_().isoformat() + bstack1l1l111_opy_ (u"ࠬࡠࠧᓰ"))
      return {bstack1l1l111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᓱ"): bstack1l1l111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨᓲ"), bstack1l1l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᓳ"): bstack1l1l111_opy_ (u"ࠩࠪᓴ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l1l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠣࡳ࡫ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱ࠾ࠥࠨᓵ") + str(error))
    return {
        bstack1l1l111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᓶ"): bstack1l1l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᓷ"),
        bstack1l1l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᓸ"): str(error)
    }
def bstack1111lll1l_opy_(caps, options, desired_capabilities={}):
  try:
    bstack1ll1l1ll1ll_opy_ = caps.get(bstack1l1l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᓹ"), {}).get(bstack1l1l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᓺ"), caps.get(bstack1l1l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩᓻ"), bstack1l1l111_opy_ (u"ࠪࠫᓼ")))
    if bstack1ll1l1ll1ll_opy_:
      logger.warn(bstack1l1l111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᓽ"))
      return False
    if options:
      bstack1l111lll1l1_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack1l111lll1l1_opy_ = desired_capabilities
    else:
      bstack1l111lll1l1_opy_ = {}
    browser = caps.get(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᓾ"), bstack1l1l111_opy_ (u"࠭ࠧᓿ")).lower() or bstack1l111lll1l1_opy_.get(bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᔀ"), bstack1l1l111_opy_ (u"ࠨࠩᔁ")).lower()
    if browser != bstack1l1l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᔂ"):
      logger.warning(bstack1l1l111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᔃ"))
      return False
    browser_version = caps.get(bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᔄ")) or caps.get(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᔅ")) or bstack1l111lll1l1_opy_.get(bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᔆ")) or bstack1l111lll1l1_opy_.get(bstack1l1l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᔇ"), {}).get(bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᔈ")) or bstack1l111lll1l1_opy_.get(bstack1l1l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᔉ"), {}).get(bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᔊ"))
    if browser_version and browser_version != bstack1l1l111_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫᔋ") and int(browser_version.split(bstack1l1l111_opy_ (u"ࠬ࠴ࠧᔌ"))[0]) <= 98:
      logger.warning(bstack1l1l111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠ࠺࠺࠱ࠦᔍ"))
      return False
    if not options:
      bstack1lll1111111_opy_ = caps.get(bstack1l1l111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᔎ")) or bstack1l111lll1l1_opy_.get(bstack1l1l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᔏ"), {})
      if bstack1l1l111_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭ᔐ") in bstack1lll1111111_opy_.get(bstack1l1l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨᔑ"), []):
        logger.warn(bstack1l1l111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨᔒ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack1l1l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻࡧ࡬ࡪࡦࡤࡸࡪࠦࡡ࠲࠳ࡼࠤࡸࡻࡰࡱࡱࡵࡸࠥࡀࠢᔓ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1llllll11l1_opy_ = config.get(bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᔔ"), {})
    bstack1llllll11l1_opy_[bstack1l1l111_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠪᔕ")] = os.getenv(bstack1l1l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᔖ"))
    bstack1l111llll1l_opy_ = json.loads(os.getenv(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᔗ"), bstack1l1l111_opy_ (u"ࠪࡿࢂ࠭ᔘ"))).get(bstack1l1l111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᔙ"))
    caps[bstack1l1l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᔚ")] = True
    if bstack1l1l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᔛ") in caps:
      caps[bstack1l1l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᔜ")][bstack1l1l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᔝ")] = bstack1llllll11l1_opy_
      caps[bstack1l1l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᔞ")][bstack1l1l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᔟ")][bstack1l1l111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᔠ")] = bstack1l111llll1l_opy_
    else:
      caps[bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᔡ")] = bstack1llllll11l1_opy_
      caps[bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᔢ")][bstack1l1l111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᔣ")] = bstack1l111llll1l_opy_
  except Exception as error:
    logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤᔤ") +  str(error))
def bstack1l111ll11l_opy_(driver, bstack1l11l1111l1_opy_):
  try:
    setattr(driver, bstack1l1l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩᔥ"), True)
    session = driver.session_id
    if session:
      bstack1l111l1llll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1l111l1llll_opy_ = False
      bstack1l111l1llll_opy_ = url.scheme in [bstack1l1l111_opy_ (u"ࠥ࡬ࡹࡺࡰࠣᔦ"), bstack1l1l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥᔧ")]
      if bstack1l111l1llll_opy_:
        if bstack1l11l1111l1_opy_:
          logger.info(bstack1l1l111_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧᔨ"))
      return bstack1l11l1111l1_opy_
  except Exception as e:
    logger.error(bstack1l1l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤᔩ") + str(e))
    return False
def bstack11llllllll_opy_(driver, name, path):
  try:
    bstack1lll1111lll_opy_ = {
        bstack1l1l111_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧᔪ"): threading.current_thread().current_test_uuid,
        bstack1l1l111_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᔫ"): os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᔬ"), bstack1l1l111_opy_ (u"ࠪࠫᔭ")),
        bstack1l1l111_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨᔮ"): os.environ.get(bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᔯ"), bstack1l1l111_opy_ (u"࠭ࠧᔰ"))
    }
    bstack1ll1ll11lll_opy_ = bstack1111l1ll1_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1ll1ll1l1_opy_.value)
    logger.debug(bstack1l1l111_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪᔱ"))
    try:
      logger.debug(driver.execute_async_script(bstack11l1l1ll1l_opy_.perform_scan, {bstack1l1l111_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣᔲ"): name}))
      bstack1111l1ll1_opy_.end(EVENTS.bstack1ll1ll1l1_opy_.value, bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᔳ"), bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᔴ"), True, None)
    except Exception as error:
      bstack1111l1ll1_opy_.end(EVENTS.bstack1ll1ll1l1_opy_.value, bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᔵ"), bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᔶ"), False, str(error))
    bstack1ll1ll11lll_opy_ = bstack1111l1ll1_opy_.bstack1l111ll1ll1_opy_(EVENTS.bstack1ll1l1l1lll_opy_.value)
    bstack1111l1ll1_opy_.mark(bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᔷ"))
    try:
      logger.debug(driver.execute_async_script(bstack11l1l1ll1l_opy_.bstack1l111l1lll1_opy_, bstack1lll1111lll_opy_))
      bstack1111l1ll1_opy_.end(bstack1ll1ll11lll_opy_, bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᔸ"), bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᔹ"),True, None)
    except Exception as error:
      bstack1111l1ll1_opy_.end(bstack1ll1ll11lll_opy_, bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᔺ"), bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᔻ"),False, str(error))
    logger.info(bstack1l1l111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠢᔼ"))
  except Exception as bstack1ll1lll111l_opy_:
    logger.error(bstack1l1l111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢᔽ") + str(path) + bstack1l1l111_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣᔾ") + str(bstack1ll1lll111l_opy_))