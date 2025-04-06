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
logger = logging.getLogger(__name__)
bstack111llllll1l_opy_ = 1000
bstack111llll1lll_opy_ = 2
class bstack111llllllll_opy_:
    def __init__(self, handler, bstack111lllll11l_opy_=bstack111llllll1l_opy_, bstack111lllllll1_opy_=bstack111llll1lll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111lllll11l_opy_ = bstack111lllll11l_opy_
        self.bstack111lllllll1_opy_ = bstack111lllllll1_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack111l1111ll_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111lllll111_opy_()
    def bstack111lllll111_opy_(self):
        self.bstack111l1111ll_opy_ = threading.Event()
        def bstack111lllll1ll_opy_():
            self.bstack111l1111ll_opy_.wait(self.bstack111lllllll1_opy_)
            if not self.bstack111l1111ll_opy_.is_set():
                self.bstack111llllll11_opy_()
        self.timer = threading.Thread(target=bstack111lllll1ll_opy_, daemon=True)
        self.timer.start()
    def bstack11l11111111_opy_(self):
        try:
            if self.bstack111l1111ll_opy_ and not self.bstack111l1111ll_opy_.is_set():
                self.bstack111l1111ll_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠫࡠࡹࡴࡰࡲࡢࡸ࡮ࡳࡥࡳ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࠨ᱘") + (str(e) or bstack1l1l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡤࡱࡱࡺࡪࡸࡴࡦࡦࠣࡸࡴࠦࡳࡵࡴ࡬ࡲ࡬ࠨ᱙")))
        finally:
            self.timer = None
    def bstack111lllll1l1_opy_(self):
        if self.timer:
            self.bstack11l11111111_opy_()
        self.bstack111lllll111_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111lllll11l_opy_:
                threading.Thread(target=self.bstack111llllll11_opy_).start()
    def bstack111llllll11_opy_(self, source = bstack1l1l111_opy_ (u"࠭ࠧᱚ")):
        with self.lock:
            if not self.queue:
                self.bstack111lllll1l1_opy_()
                return
            data = self.queue[:self.bstack111lllll11l_opy_]
            del self.queue[:self.bstack111lllll11l_opy_]
        self.handler(data)
        if source != bstack1l1l111_opy_ (u"ࠧࡴࡪࡸࡸࡩࡵࡷ࡯ࠩᱛ"):
            self.bstack111lllll1l1_opy_()
    def shutdown(self):
        self.bstack11l11111111_opy_()
        while self.queue:
            self.bstack111llllll11_opy_(source=bstack1l1l111_opy_ (u"ࠨࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠪᱜ"))