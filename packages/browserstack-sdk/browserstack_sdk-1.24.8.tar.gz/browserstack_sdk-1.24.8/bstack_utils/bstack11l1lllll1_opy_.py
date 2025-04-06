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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11lll1l1l1l_opy_, bstack1l111ll1l1_opy_, bstack1l11ll111l_opy_, bstack1lll11ll1l_opy_, \
    bstack11ll11ll1ll_opy_
from bstack_utils.measure import measure
def bstack1ll111l11l_opy_(bstack111lll1llll_opy_):
    for driver in bstack111lll1llll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11ll111l11_opy_, stage=STAGE.bstack1l1l1111l_opy_)
def bstack11ll111111_opy_(driver, status, reason=bstack1l1l111_opy_ (u"ࠫࠬᱟ")):
    bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
    if bstack111l11l1l_opy_.bstack111l1l111l_opy_():
        return
    bstack11l111l11_opy_ = bstack1ll1l1l1l1_opy_(bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᱠ"), bstack1l1l111_opy_ (u"࠭ࠧᱡ"), status, reason, bstack1l1l111_opy_ (u"ࠧࠨᱢ"), bstack1l1l111_opy_ (u"ࠨࠩᱣ"))
    driver.execute_script(bstack11l111l11_opy_)
@measure(event_name=EVENTS.bstack11ll111l11_opy_, stage=STAGE.bstack1l1l1111l_opy_)
def bstack11l1l1lll1_opy_(page, status, reason=bstack1l1l111_opy_ (u"ࠩࠪᱤ")):
    try:
        if page is None:
            return
        bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
        if bstack111l11l1l_opy_.bstack111l1l111l_opy_():
            return
        bstack11l111l11_opy_ = bstack1ll1l1l1l1_opy_(bstack1l1l111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᱥ"), bstack1l1l111_opy_ (u"ࠫࠬᱦ"), status, reason, bstack1l1l111_opy_ (u"ࠬ࠭ᱧ"), bstack1l1l111_opy_ (u"࠭ࠧᱨ"))
        page.evaluate(bstack1l1l111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᱩ"), bstack11l111l11_opy_)
    except Exception as e:
        print(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨᱪ"), e)
def bstack1ll1l1l1l1_opy_(type, name, status, reason, bstack1l1l1llll1_opy_, bstack11ll11l1l1_opy_):
    bstack1l11lllll_opy_ = {
        bstack1l1l111_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᱫ"): type,
        bstack1l1l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱬ"): {}
    }
    if type == bstack1l1l111_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᱭ"):
        bstack1l11lllll_opy_[bstack1l1l111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᱮ")][bstack1l1l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᱯ")] = bstack1l1l1llll1_opy_
        bstack1l11lllll_opy_[bstack1l1l111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᱰ")][bstack1l1l111_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᱱ")] = json.dumps(str(bstack11ll11l1l1_opy_))
    if type == bstack1l1l111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᱲ"):
        bstack1l11lllll_opy_[bstack1l1l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱳ")][bstack1l1l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᱴ")] = name
    if type == bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᱵ"):
        bstack1l11lllll_opy_[bstack1l1l111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᱶ")][bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᱷ")] = status
        if status == bstack1l1l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᱸ") and str(reason) != bstack1l1l111_opy_ (u"ࠤࠥᱹ"):
            bstack1l11lllll_opy_[bstack1l1l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᱺ")][bstack1l1l111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᱻ")] = json.dumps(str(reason))
    bstack1ll11l11l1_opy_ = bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᱼ").format(json.dumps(bstack1l11lllll_opy_))
    return bstack1ll11l11l1_opy_
def bstack1ll1ll1ll1_opy_(url, config, logger, bstack1lll1lllll_opy_=False):
    hostname = bstack1l111ll1l1_opy_(url)
    is_private = bstack1lll11ll1l_opy_(hostname)
    try:
        if is_private or bstack1lll1lllll_opy_:
            file_path = bstack11lll1l1l1l_opy_(bstack1l1l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᱽ"), bstack1l1l111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᱾"), logger)
            if os.environ.get(bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭᱿")) and eval(
                    os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᲀ"))):
                return
            if (bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᲁ") in config and not config[bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᲂ")]):
                os.environ[bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᲃ")] = str(True)
                bstack111llll1111_opy_ = {bstack1l1l111_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨᲄ"): hostname}
                bstack11ll11ll1ll_opy_(bstack1l1l111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᲅ"), bstack1l1l111_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ᲆ"), bstack111llll1111_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l1ll11l_opy_(caps, bstack111lll1lll1_opy_):
    if bstack1l1l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᲇ") in caps:
        caps[bstack1l1l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᲈ")][bstack1l1l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᲉ")] = True
        if bstack111lll1lll1_opy_:
            caps[bstack1l1l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᲊ")][bstack1l1l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ᲋")] = bstack111lll1lll1_opy_
    else:
        caps[bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ᲌")] = True
        if bstack111lll1lll1_opy_:
            caps[bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᲍")] = bstack111lll1lll1_opy_
def bstack11l111111ll_opy_(bstack111lll1111_opy_):
    bstack111llll111l_opy_ = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭᲎"), bstack1l1l111_opy_ (u"ࠪࠫ᲏"))
    if bstack111llll111l_opy_ == bstack1l1l111_opy_ (u"ࠫࠬᲐ") or bstack111llll111l_opy_ == bstack1l1l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭Ბ"):
        threading.current_thread().testStatus = bstack111lll1111_opy_
    else:
        if bstack111lll1111_opy_ == bstack1l1l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭Გ"):
            threading.current_thread().testStatus = bstack111lll1111_opy_