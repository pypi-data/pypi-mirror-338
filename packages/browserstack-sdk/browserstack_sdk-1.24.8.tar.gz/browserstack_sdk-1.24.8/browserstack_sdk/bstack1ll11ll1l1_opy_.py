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
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1l1l11l111_opy_ = {}
        bstack11l1l11lll_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ๢"), bstack1l1l111_opy_ (u"ࠨࠩ๣"))
        if not bstack11l1l11lll_opy_:
            return bstack1l1l11l111_opy_
        try:
            bstack11l1l1l111_opy_ = json.loads(bstack11l1l11lll_opy_)
            if bstack1l1l111_opy_ (u"ࠤࡲࡷࠧ๤") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠥࡳࡸࠨ๥")] = bstack11l1l1l111_opy_[bstack1l1l111_opy_ (u"ࠦࡴࡹࠢ๦")]
            if bstack1l1l111_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ๧") in bstack11l1l1l111_opy_ or bstack1l1l111_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ๨") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ๩")] = bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ๪"), bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ๫")))
            if bstack1l1l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦ๬") in bstack11l1l1l111_opy_ or bstack1l1l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ๭") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ๮")] = bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢ๯"), bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ๰")))
            if bstack1l1l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ๱") in bstack11l1l1l111_opy_ or bstack1l1l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ๲") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦ๳")] = bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ๴"), bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ๵")))
            if bstack1l1l111_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨ๶") in bstack11l1l1l111_opy_ or bstack1l1l111_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ๷") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ๸")] = bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤ๹"), bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢ๺")))
            if bstack1l1l111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ๻") in bstack11l1l1l111_opy_ or bstack1l1l111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ๼") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ๽")] = bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤ๾"), bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ๿")))
            if bstack1l1l111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ຀") in bstack11l1l1l111_opy_ or bstack1l1l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧກ") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨຂ")] = bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ຃"), bstack11l1l1l111_opy_.get(bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣຄ")))
            if bstack1l1l111_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤ຅") in bstack11l1l1l111_opy_:
                bstack1l1l11l111_opy_[bstack1l1l111_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥຆ")] = bstack11l1l1l111_opy_[bstack1l1l111_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦງ")]
        except Exception as error:
            logger.error(bstack1l1l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡥࡹࡧ࠺ࠡࠤຈ") +  str(error))
        return bstack1l1l11l111_opy_