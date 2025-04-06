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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1111llllll_opy_ import bstack111l11111l_opy_
class bstack1lllll1l111_opy_(abc.ABC):
    bin_session_id: str
    bstack1111llllll_opy_: bstack111l11111l_opy_
    def __init__(self):
        self.bstack1llllll1lll_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1111llllll_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1llll11l1l1_opy_(self):
        return (self.bstack1llllll1lll_opy_ != None and self.bin_session_id != None and self.bstack1111llllll_opy_ != None)
    def configure(self, bstack1llllll1lll_opy_, config, bin_session_id: str, bstack1111llllll_opy_: bstack111l11111l_opy_):
        self.bstack1llllll1lll_opy_ = bstack1llllll1lll_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1111llllll_opy_ = bstack1111llllll_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨࠥࡳ࡯ࡥࡷ࡯ࡩࠥࢁࡳࡦ࡮ࡩ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥ࠮ࡠࡡࡱࡥࡲ࡫࡟ࡠࡿ࠽ࠤࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨᅟ") + str(self.bin_session_id) + bstack1l1l111_opy_ (u"ࠥࠦᅠ"))
    def bstack1ll1llll1l1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l1l111_opy_ (u"ࠦࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡐࡲࡲࡪࠨᅡ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False