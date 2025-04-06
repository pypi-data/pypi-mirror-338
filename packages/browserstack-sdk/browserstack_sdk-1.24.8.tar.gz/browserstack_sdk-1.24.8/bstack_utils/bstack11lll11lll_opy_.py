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
from collections import deque
from bstack_utils.constants import *
class bstack1lll1llll1_opy_:
    def __init__(self):
        self._11l11l1ll11_opy_ = deque()
        self._11l11l1111l_opy_ = {}
        self._11l11l1l111_opy_ = False
    def bstack11l11l1l11l_opy_(self, test_name, bstack11l11l111ll_opy_):
        bstack11l11l11l11_opy_ = self._11l11l1111l_opy_.get(test_name, {})
        return bstack11l11l11l11_opy_.get(bstack11l11l111ll_opy_, 0)
    def bstack11l11l111l1_opy_(self, test_name, bstack11l11l111ll_opy_):
        bstack11l11l1l1l1_opy_ = self.bstack11l11l1l11l_opy_(test_name, bstack11l11l111ll_opy_)
        self.bstack11l11l11l1l_opy_(test_name, bstack11l11l111ll_opy_)
        return bstack11l11l1l1l1_opy_
    def bstack11l11l11l1l_opy_(self, test_name, bstack11l11l111ll_opy_):
        if test_name not in self._11l11l1111l_opy_:
            self._11l11l1111l_opy_[test_name] = {}
        bstack11l11l11l11_opy_ = self._11l11l1111l_opy_[test_name]
        bstack11l11l1l1l1_opy_ = bstack11l11l11l11_opy_.get(bstack11l11l111ll_opy_, 0)
        bstack11l11l11l11_opy_[bstack11l11l111ll_opy_] = bstack11l11l1l1l1_opy_ + 1
    def bstack1ll11lll1l_opy_(self, bstack11l11l11lll_opy_, bstack11l11l1l1ll_opy_):
        bstack11l11l11111_opy_ = self.bstack11l11l111l1_opy_(bstack11l11l11lll_opy_, bstack11l11l1l1ll_opy_)
        event_name = bstack1l11111111l_opy_[bstack11l11l1l1ll_opy_]
        bstack1l1llll1l11_opy_ = bstack1l1l111_opy_ (u"ࠣࡽࢀ࠱ࢀࢃ࠭ࡼࡿࠥᯥ").format(bstack11l11l11lll_opy_, event_name, bstack11l11l11111_opy_)
        self._11l11l1ll11_opy_.append(bstack1l1llll1l11_opy_)
    def bstack11l1ll1ll_opy_(self):
        return len(self._11l11l1ll11_opy_) == 0
    def bstack1ll1l111_opy_(self):
        bstack11l11l11ll1_opy_ = self._11l11l1ll11_opy_.popleft()
        return bstack11l11l11ll1_opy_
    def capturing(self):
        return self._11l11l1l111_opy_
    def bstack11ll1l111_opy_(self):
        self._11l11l1l111_opy_ = True
    def bstack1l1l11lll_opy_(self):
        self._11l11l1l111_opy_ = False