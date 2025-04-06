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
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1l11l1111ll_opy_, bstack1l11l111111_opy_, bstack1l1l1lll_opy_, bstack111lllll1l_opy_, bstack11ll1lll111_opy_, bstack11llll11ll1_opy_, bstack11lll11l11l_opy_, bstack1ll11l1ll1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack111llll1ll1_opy_ import bstack111llllllll_opy_
import bstack_utils.bstack1lll1l11_opy_ as bstack11l1l1l1ll_opy_
from bstack_utils.bstack11l11ll1ll_opy_ import bstack1l1lll1lll_opy_
import bstack_utils.accessibility as bstack11l1l1lll_opy_
from bstack_utils.bstack11l1l1ll1l_opy_ import bstack11l1l1ll1l_opy_
from bstack_utils.bstack11l11lllll_opy_ import bstack111lll11ll_opy_
bstack111ll11ll11_opy_ = bstack1l1l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ᳒")
logger = logging.getLogger(__name__)
class bstack1l11l11lll_opy_:
    bstack111llll1ll1_opy_ = None
    bs_config = None
    bstack1llll1l1_opy_ = None
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1l111111111_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def launch(cls, bs_config, bstack1llll1l1_opy_):
        cls.bs_config = bs_config
        cls.bstack1llll1l1_opy_ = bstack1llll1l1_opy_
        try:
            cls.bstack111ll1l1l11_opy_()
            bstack1l111ll111l_opy_ = bstack1l11l1111ll_opy_(bs_config)
            bstack1l11l111lll_opy_ = bstack1l11l111111_opy_(bs_config)
            data = bstack11l1l1l1ll_opy_.bstack111ll1l1111_opy_(bs_config, bstack1llll1l1_opy_)
            config = {
                bstack1l1l111_opy_ (u"ࠨࡣࡸࡸ࡭࠭᳓"): (bstack1l111ll111l_opy_, bstack1l11l111lll_opy_),
                bstack1l1l111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵ᳔ࠪ"): cls.default_headers()
            }
            response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ᳕"), cls.request_url(bstack1l1l111_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠵࠳ࡧࡻࡩ࡭ࡦࡶ᳖ࠫ")), data, config)
            if response.status_code != 200:
                bstack1lllll1ll11_opy_ = response.json()
                if bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ᳗࠭")] == False:
                    cls.bstack111ll1l11l1_opy_(bstack1lllll1ll11_opy_)
                    return
                cls.bstack111ll11l1l1_opy_(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ᳘࠭")])
                cls.bstack111ll11l1ll_opy_(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ᳙ࠧ")])
                return None
            bstack111ll111lll_opy_ = cls.bstack111ll11l11l_opy_(response)
            return bstack111ll111lll_opy_
        except Exception as error:
            logger.error(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡿࢂࠨ᳚").format(str(error)))
            return None
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    def stop(cls, bstack111ll11l111_opy_=None):
        if not bstack1l1lll1lll_opy_.on() and not bstack11l1l1lll_opy_.on():
            return
        if os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᳛")) == bstack1l1l111_opy_ (u"ࠥࡲࡺࡲ࡬᳜ࠣ") or os.environ.get(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅ᳝ࠩ")) == bstack1l1l111_opy_ (u"ࠧࡴࡵ࡭࡮᳞ࠥ"):
            logger.error(bstack1l1l111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯᳟ࠩ"))
            return {
                bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ᳠"): bstack1l1l111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᳡"),
                bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧ᳢ࠪ"): bstack1l1l111_opy_ (u"ࠪࡘࡴࡱࡥ࡯࠱ࡥࡹ࡮ࡲࡤࡊࡆࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥ࠮ࠣࡦࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡲ࡯ࡧࡩࡶࠣ࡬ࡦࡼࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠨ᳣")
            }
        try:
            cls.bstack111llll1ll1_opy_.shutdown()
            data = {
                bstack1l1l111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵ᳤ࠩ"): bstack1ll11l1ll1_opy_()
            }
            if not bstack111ll11l111_opy_ is None:
                data[bstack1l1l111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟࡮ࡧࡷࡥࡩࡧࡴࡢ᳥ࠩ")] = [{
                    bstack1l1l111_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ᳦࠭"): bstack1l1l111_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨ᳧ࠬ"),
                    bstack1l1l111_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨ᳨"): bstack111ll11l111_opy_
                }]
            config = {
                bstack1l1l111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᳩ"): cls.default_headers()
            }
            bstack11lll1lll1l_opy_ = bstack1l1l111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳࠫᳪ").format(os.environ[bstack1l1l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᳫ")])
            bstack111ll11llll_opy_ = cls.request_url(bstack11lll1lll1l_opy_)
            response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠬࡖࡕࡕࠩᳬ"), bstack111ll11llll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l1l111_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯᳭ࠧ"))
        except Exception as error:
            logger.error(bstack1l1l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻࠼ࠣࠦᳮ") + str(error))
            return {
                bstack1l1l111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᳯ"): bstack1l1l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᳰ"),
                bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᳱ"): str(error)
            }
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    def bstack111ll11l11l_opy_(cls, response):
        bstack1lllll1ll11_opy_ = response.json() if not isinstance(response, dict) else response
        bstack111ll111lll_opy_ = {}
        if bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠫ࡯ࡽࡴࠨᳲ")) is None:
            os.environ[bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᳳ")] = bstack1l1l111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ᳴")
        else:
            os.environ[bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᳵ")] = bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠨ࡬ࡺࡸࠬᳶ"), bstack1l1l111_opy_ (u"ࠩࡱࡹࡱࡲࠧ᳷"))
        os.environ[bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ᳸")] = bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭᳹"), bstack1l1l111_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᳺ"))
        logger.info(bstack1l1l111_opy_ (u"࠭ࡔࡦࡵࡷ࡬ࡺࡨࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ᳻") + os.getenv(bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ᳼")));
        if bstack1l1lll1lll_opy_.bstack111ll1l1ll1_opy_(cls.bs_config, cls.bstack1llll1l1_opy_.get(bstack1l1l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ᳽"), bstack1l1l111_opy_ (u"ࠩࠪ᳾"))) is True:
            bstack111ll111l11_opy_, build_hashed_id, bstack111ll11ll1l_opy_ = cls.bstack111ll1l1l1l_opy_(bstack1lllll1ll11_opy_)
            if bstack111ll111l11_opy_ != None and build_hashed_id != None:
                bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᳿")] = {
                    bstack1l1l111_opy_ (u"ࠫ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠧᴀ"): bstack111ll111l11_opy_,
                    bstack1l1l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᴁ"): build_hashed_id,
                    bstack1l1l111_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᴂ"): bstack111ll11ll1l_opy_
                }
            else:
                bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᴃ")] = {}
        else:
            bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᴄ")] = {}
        if bstack11l1l1lll_opy_.bstack1l11l111ll1_opy_(cls.bs_config) is True:
            bstack111ll11lll1_opy_, build_hashed_id = cls.bstack111ll1ll1ll_opy_(bstack1lllll1ll11_opy_)
            if bstack111ll11lll1_opy_ != None and build_hashed_id != None:
                bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᴅ")] = {
                    bstack1l1l111_opy_ (u"ࠪࡥࡺࡺࡨࡠࡶࡲ࡯ࡪࡴࠧᴆ"): bstack111ll11lll1_opy_,
                    bstack1l1l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᴇ"): build_hashed_id,
                }
            else:
                bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᴈ")] = {}
        else:
            bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᴉ")] = {}
        if bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᴊ")].get(bstack1l1l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᴋ")) != None or bstack111ll111lll_opy_[bstack1l1l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᴌ")].get(bstack1l1l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᴍ")) != None:
            cls.bstack111ll1ll111_opy_(bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠫ࡯ࡽࡴࠨᴎ")), bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᴏ")))
        return bstack111ll111lll_opy_
    @classmethod
    def bstack111ll1l1l1l_opy_(cls, bstack1lllll1ll11_opy_):
        if bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᴐ")) == None:
            cls.bstack111ll11l1l1_opy_()
            return [None, None, None]
        if bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᴑ")][bstack1l1l111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩᴒ")] != True:
            cls.bstack111ll11l1l1_opy_(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᴓ")])
            return [None, None, None]
        logger.debug(bstack1l1l111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᴔ"))
        os.environ[bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᴕ")] = bstack1l1l111_opy_ (u"ࠬࡺࡲࡶࡧࠪᴖ")
        if bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"࠭ࡪࡸࡶࠪᴗ")):
            os.environ[bstack1l1l111_opy_ (u"ࠧࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࡤࡌࡏࡓࡡࡆࡖࡆ࡙ࡈࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫᴘ")] = json.dumps({
                bstack1l1l111_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪᴙ"): bstack1l11l1111ll_opy_(cls.bs_config),
                bstack1l1l111_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫᴚ"): bstack1l11l111111_opy_(cls.bs_config)
            })
        if bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᴛ")):
            os.environ[bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᴜ")] = bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᴝ")]
        if bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᴞ")].get(bstack1l1l111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᴟ"), {}).get(bstack1l1l111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᴠ")):
            os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᴡ")] = str(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᴢ")][bstack1l1l111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬᴣ")][bstack1l1l111_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᴤ")])
        else:
            os.environ[bstack1l1l111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᴥ")] = bstack1l1l111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᴦ")
        return [bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠨ࡬ࡺࡸࠬᴧ")], bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᴨ")], os.environ[bstack1l1l111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᴩ")]]
    @classmethod
    def bstack111ll1ll1ll_opy_(cls, bstack1lllll1ll11_opy_):
        if bstack1lllll1ll11_opy_.get(bstack1l1l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᴪ")) == None:
            cls.bstack111ll11l1ll_opy_()
            return [None, None]
        if bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᴫ")][bstack1l1l111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᴬ")] != True:
            cls.bstack111ll11l1ll_opy_(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᴭ")])
            return [None, None]
        if bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᴮ")].get(bstack1l1l111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᴯ")):
            logger.debug(bstack1l1l111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᴰ"))
            parsed = json.loads(os.getenv(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᴱ"), bstack1l1l111_opy_ (u"ࠬࢁࡽࠨᴲ")))
            capabilities = bstack11l1l1l1ll_opy_.bstack111ll1l111l_opy_(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᴳ")][bstack1l1l111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᴴ")][bstack1l1l111_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᴵ")], bstack1l1l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᴶ"), bstack1l1l111_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩᴷ"))
            bstack111ll11lll1_opy_ = capabilities[bstack1l1l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩᴸ")]
            os.environ[bstack1l1l111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᴹ")] = bstack111ll11lll1_opy_
            parsed[bstack1l1l111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᴺ")] = capabilities[bstack1l1l111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᴻ")]
            os.environ[bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᴼ")] = json.dumps(parsed)
            scripts = bstack11l1l1l1ll_opy_.bstack111ll1l111l_opy_(bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᴽ")][bstack1l1l111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫᴾ")][bstack1l1l111_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᴿ")], bstack1l1l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᵀ"), bstack1l1l111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࠧᵁ"))
            bstack11l1l1ll1l_opy_.bstack1l111lll111_opy_(scripts)
            commands = bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᵂ")][bstack1l1l111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩᵃ")][bstack1l1l111_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠪᵄ")].get(bstack1l1l111_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᵅ"))
            bstack11l1l1ll1l_opy_.bstack1l111lll11l_opy_(commands)
            bstack11l1l1ll1l_opy_.store()
        return [bstack111ll11lll1_opy_, bstack1lllll1ll11_opy_[bstack1l1l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᵆ")]]
    @classmethod
    def bstack111ll11l1l1_opy_(cls, response=None):
        os.environ[bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᵇ")] = bstack1l1l111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᵈ")
        os.environ[bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᵉ")] = bstack1l1l111_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᵊ")
        os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨᵋ")] = bstack1l1l111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᵌ")
        os.environ[bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᵍ")] = bstack1l1l111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᵎ")
        os.environ[bstack1l1l111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᵏ")] = bstack1l1l111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᵐ")
        cls.bstack111ll1l11l1_opy_(response, bstack1l1l111_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣᵑ"))
        return [None, None, None]
    @classmethod
    def bstack111ll11l1ll_opy_(cls, response=None):
        os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᵒ")] = bstack1l1l111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᵓ")
        os.environ[bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᵔ")] = bstack1l1l111_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᵕ")
        os.environ[bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᵖ")] = bstack1l1l111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᵗ")
        cls.bstack111ll1l11l1_opy_(response, bstack1l1l111_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᵘ"))
        return [None, None, None]
    @classmethod
    def bstack111ll1ll111_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᵙ")] = jwt
        os.environ[bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᵚ")] = build_hashed_id
    @classmethod
    def bstack111ll1l11l1_opy_(cls, response=None, product=bstack1l1l111_opy_ (u"ࠦࠧᵛ")):
        if response == None:
            logger.error(product + bstack1l1l111_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢᵜ"))
        for error in response[bstack1l1l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ᵝ")]:
            bstack11llll11l11_opy_ = error[bstack1l1l111_opy_ (u"ࠧ࡬ࡧࡼࠫᵞ")]
            error_message = error[bstack1l1l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᵟ")]
            if error_message:
                if bstack11llll11l11_opy_ == bstack1l1l111_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣᵠ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l1l111_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦᵡ") + product + bstack1l1l111_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᵢ"))
    @classmethod
    def bstack111ll1l1l11_opy_(cls):
        if cls.bstack111llll1ll1_opy_ is not None:
            return
        cls.bstack111llll1ll1_opy_ = bstack111llllllll_opy_(cls.bstack111ll111ll1_opy_)
        cls.bstack111llll1ll1_opy_.start()
    @classmethod
    def bstack11l11111l1_opy_(cls):
        if cls.bstack111llll1ll1_opy_ is None:
            return
        cls.bstack111llll1ll1_opy_.shutdown()
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    def bstack111ll111ll1_opy_(cls, bstack111ll1l1ll_opy_, event_url=bstack1l1l111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫᵣ")):
        config = {
            bstack1l1l111_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᵤ"): cls.default_headers()
        }
        logger.debug(bstack1l1l111_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢᵥ").format(bstack1l1l111_opy_ (u"ࠨ࠮ࠣࠫᵦ").join([event[bstack1l1l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᵧ")] for event in bstack111ll1l1ll_opy_])))
        response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᵨ"), cls.request_url(event_url), bstack111ll1l1ll_opy_, config)
        bstack1l11l111l1l_opy_ = response.json()
    @classmethod
    def bstack111ll111l_opy_(cls, bstack111ll1l1ll_opy_, event_url=bstack1l1l111_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᵩ")):
        logger.debug(bstack1l1l111_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧᵪ").format(bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᵫ")]))
        if not bstack11l1l1l1ll_opy_.bstack111ll111111_opy_(bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᵬ")]):
            logger.debug(bstack1l1l111_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨᵭ").format(bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᵮ")]))
            return
        bstack1lll1l1l_opy_ = bstack11l1l1l1ll_opy_.bstack111ll111l1l_opy_(bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᵯ")], bstack111ll1l1ll_opy_.get(bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᵰ")))
        if bstack1lll1l1l_opy_ != None:
            if bstack111ll1l1ll_opy_.get(bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᵱ")) != None:
                bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᵲ")][bstack1l1l111_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬᵳ")] = bstack1lll1l1l_opy_
            else:
                bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ᵴ")] = bstack1lll1l1l_opy_
        if event_url == bstack1l1l111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᵵ"):
            cls.bstack111ll1l1l11_opy_()
            logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨᵶ").format(bstack111ll1l1ll_opy_[bstack1l1l111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᵷ")]))
            cls.bstack111llll1ll1_opy_.add(bstack111ll1l1ll_opy_)
        elif event_url == bstack1l1l111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᵸ"):
            cls.bstack111ll111ll1_opy_([bstack111ll1l1ll_opy_], event_url)
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    def bstack11l11lll1_opy_(cls, logs):
        bstack111ll1ll11l_opy_ = []
        for log in logs:
            bstack111ll11111l_opy_ = {
                bstack1l1l111_opy_ (u"࠭࡫ࡪࡰࡧࠫᵹ"): bstack1l1l111_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩᵺ"),
                bstack1l1l111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᵻ"): log[bstack1l1l111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᵼ")],
                bstack1l1l111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᵽ"): log[bstack1l1l111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᵾ")],
                bstack1l1l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬᵿ"): {},
                bstack1l1l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᶀ"): log[bstack1l1l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᶁ")],
            }
            if bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᶂ") in log:
                bstack111ll11111l_opy_[bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᶃ")] = log[bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᶄ")]
            elif bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᶅ") in log:
                bstack111ll11111l_opy_[bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᶆ")] = log[bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᶇ")]
            bstack111ll1ll11l_opy_.append(bstack111ll11111l_opy_)
        cls.bstack111ll111l_opy_({
            bstack1l1l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᶈ"): bstack1l1l111_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᶉ"),
            bstack1l1l111_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧᶊ"): bstack111ll1ll11l_opy_
        })
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    def bstack111ll1111l1_opy_(cls, steps):
        bstack111ll1l1lll_opy_ = []
        for step in steps:
            bstack111ll1111ll_opy_ = {
                bstack1l1l111_opy_ (u"ࠪ࡯࡮ࡴࡤࠨᶋ"): bstack1l1l111_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧᶌ"),
                bstack1l1l111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᶍ"): step[bstack1l1l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᶎ")],
                bstack1l1l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᶏ"): step[bstack1l1l111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᶐ")],
                bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᶑ"): step[bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᶒ")],
                bstack1l1l111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᶓ"): step[bstack1l1l111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᶔ")]
            }
            if bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᶕ") in step:
                bstack111ll1111ll_opy_[bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᶖ")] = step[bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᶗ")]
            elif bstack1l1l111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᶘ") in step:
                bstack111ll1111ll_opy_[bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᶙ")] = step[bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᶚ")]
            bstack111ll1l1lll_opy_.append(bstack111ll1111ll_opy_)
        cls.bstack111ll111l_opy_({
            bstack1l1l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᶛ"): bstack1l1l111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᶜ"),
            bstack1l1l111_opy_ (u"ࠧ࡭ࡱࡪࡷࠬᶝ"): bstack111ll1l1lll_opy_
        })
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1lll11lll1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack11l11lll_opy_(cls, screenshot):
        cls.bstack111ll111l_opy_({
            bstack1l1l111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᶞ"): bstack1l1l111_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᶟ"),
            bstack1l1l111_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᶠ"): [{
                bstack1l1l111_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᶡ"): bstack1l1l111_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧᶢ"),
                bstack1l1l111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᶣ"): datetime.datetime.utcnow().isoformat() + bstack1l1l111_opy_ (u"࡛ࠧࠩᶤ"),
                bstack1l1l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᶥ"): screenshot[bstack1l1l111_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨᶦ")],
                bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᶧ"): screenshot[bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᶨ")]
            }]
        }, event_url=bstack1l1l111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᶩ"))
    @classmethod
    @bstack111lllll1l_opy_(class_method=True)
    def bstack1ll1ll1lll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack111ll111l_opy_({
            bstack1l1l111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᶪ"): bstack1l1l111_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᶫ"),
            bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᶬ"): {
                bstack1l1l111_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᶭ"): cls.current_test_uuid(),
                bstack1l1l111_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤᶮ"): cls.bstack11l111ll1l_opy_(driver)
            }
        })
    @classmethod
    def bstack11l11ll11l_opy_(cls, event: str, bstack111ll1l1ll_opy_: bstack111lll11ll_opy_):
        bstack111ll1ll1l_opy_ = {
            bstack1l1l111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᶯ"): event,
            bstack111ll1l1ll_opy_.bstack11l1111111_opy_(): bstack111ll1l1ll_opy_.bstack11l1111ll1_opy_(event)
        }
        cls.bstack111ll111l_opy_(bstack111ll1ll1l_opy_)
        result = getattr(bstack111ll1l1ll_opy_, bstack1l1l111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᶰ"), None)
        if event == bstack1l1l111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᶱ"):
            threading.current_thread().bstackTestMeta = {bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᶲ"): bstack1l1l111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᶳ")}
        elif event == bstack1l1l111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᶴ"):
            threading.current_thread().bstackTestMeta = {bstack1l1l111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᶵ"): getattr(result, bstack1l1l111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᶶ"), bstack1l1l111_opy_ (u"ࠬ࠭ᶷ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᶸ"), None) is None or os.environ[bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᶹ")] == bstack1l1l111_opy_ (u"ࠣࡰࡸࡰࡱࠨᶺ")) and (os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᶻ"), None) is None or os.environ[bstack1l1l111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᶼ")] == bstack1l1l111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᶽ")):
            return False
        return True
    @staticmethod
    def bstack111ll1ll1l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11l11lll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l1l111_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᶾ"): bstack1l1l111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᶿ"),
            bstack1l1l111_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ᷀"): bstack1l1l111_opy_ (u"ࠨࡶࡵࡹࡪ࠭᷁")
        }
        if os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙᷂࠭"), None):
            headers[bstack1l1l111_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ᷃")] = bstack1l1l111_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ᷄").format(os.environ[bstack1l1l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ᷅")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l1l111_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ᷆").format(bstack111ll11ll11_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ᷇"), None)
    @staticmethod
    def bstack11l111ll1l_opy_(driver):
        return {
            bstack11ll1lll111_opy_(): bstack11llll11ll1_opy_(driver)
        }
    @staticmethod
    def bstack111ll1l11ll_opy_(exception_info, report):
        return [{bstack1l1l111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ᷈"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111l111ll1_opy_(typename):
        if bstack1l1l111_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ᷉") in typename:
            return bstack1l1l111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵ᷊ࠦ")
        return bstack1l1l111_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ᷋")