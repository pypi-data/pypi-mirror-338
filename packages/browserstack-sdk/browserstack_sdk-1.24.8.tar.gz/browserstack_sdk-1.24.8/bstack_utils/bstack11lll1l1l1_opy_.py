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
class bstack1l1l11111l_opy_:
    def __init__(self, handler):
        self._111llll11l1_opy_ = None
        self.handler = handler
        self._111llll1l1l_opy_ = self.bstack111llll1l11_opy_()
        self.patch()
    def patch(self):
        self._111llll11l1_opy_ = self._111llll1l1l_opy_.execute
        self._111llll1l1l_opy_.execute = self.bstack111llll11ll_opy_()
    def bstack111llll11ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l1l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤᱝ"), driver_command, None, this, args)
            response = self._111llll11l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l1l111_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᱞ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._111llll1l1l_opy_.execute = self._111llll11l1_opy_
    @staticmethod
    def bstack111llll1l11_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver