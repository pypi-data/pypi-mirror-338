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
import re
from bstack_utils.bstack11l1lllll1_opy_ import bstack11l111111ll_opy_
def bstack11l1111l11l_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1l111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᰥ")):
        return bstack1l1l111_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᰦ")
    elif fixture_name.startswith(bstack1l1l111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᰧ")):
        return bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᰨ")
    elif fixture_name.startswith(bstack1l1l111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᰩ")):
        return bstack1l1l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᰪ")
    elif fixture_name.startswith(bstack1l1l111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᰫ")):
        return bstack1l1l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᰬ")
def bstack11l1111111l_opy_(fixture_name):
    return bool(re.match(bstack1l1l111_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᰭ"), fixture_name))
def bstack11l1111l1ll_opy_(fixture_name):
    return bool(re.match(bstack1l1l111_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᰮ"), fixture_name))
def bstack11l111111l1_opy_(fixture_name):
    return bool(re.match(bstack1l1l111_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᰯ"), fixture_name))
def bstack11l1111l111_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1l111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᰰ")):
        return bstack1l1l111_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᰱ"), bstack1l1l111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᰲ")
    elif fixture_name.startswith(bstack1l1l111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᰳ")):
        return bstack1l1l111_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᰴ"), bstack1l1l111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᰵ")
    elif fixture_name.startswith(bstack1l1l111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᰶ")):
        return bstack1l1l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰ᰷ࠪ"), bstack1l1l111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ᰸")
    elif fixture_name.startswith(bstack1l1l111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᰹")):
        return bstack1l1l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫ᰺"), bstack1l1l111_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭᰻")
    return None, None
def bstack11l11111lll_opy_(hook_name):
    if hook_name in [bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ᰼"), bstack1l1l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ᰽")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11111l11_opy_(hook_name):
    if hook_name in [bstack1l1l111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ᰾"), bstack1l1l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭᰿")]:
        return bstack1l1l111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭᱀")
    elif hook_name in [bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨ᱁"), bstack1l1l111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ᱂")]:
        return bstack1l1l111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨ᱃")
    elif hook_name in [bstack1l1l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᱄"), bstack1l1l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨ᱅")]:
        return bstack1l1l111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ᱆")
    elif hook_name in [bstack1l1l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ᱇"), bstack1l1l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ᱈")]:
        return bstack1l1l111_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭᱉")
    return hook_name
def bstack11l11111ll1_opy_(node, scenario):
    if hasattr(node, bstack1l1l111_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭᱊")):
        parts = node.nodeid.rsplit(bstack1l1l111_opy_ (u"ࠧࡡࠢ᱋"))
        params = parts[-1]
        return bstack1l1l111_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨ᱌").format(scenario.name, params)
    return scenario.name
def bstack11l1111l1l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l1l111_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᱍ")):
            examples = list(node.callspec.params[bstack1l1l111_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧᱎ")].values())
        return examples
    except:
        return []
def bstack11l1111lll1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l11111l1l_opy_(report):
    try:
        status = bstack1l1l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᱏ")
        if report.passed or (report.failed and hasattr(report, bstack1l1l111_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ᱐"))):
            status = bstack1l1l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ᱑")
        elif report.skipped:
            status = bstack1l1l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭᱒")
        bstack11l111111ll_opy_(status)
    except:
        pass
def bstack111llll11_opy_(status):
    try:
        bstack11l1111ll1l_opy_ = bstack1l1l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᱓")
        if status == bstack1l1l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᱔"):
            bstack11l1111ll1l_opy_ = bstack1l1l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᱕")
        elif status == bstack1l1l111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᱖"):
            bstack11l1111ll1l_opy_ = bstack1l1l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᱗")
        bstack11l111111ll_opy_(bstack11l1111ll1l_opy_)
    except:
        pass
def bstack11l1111ll11_opy_(item=None, report=None, summary=None, extra=None):
    return