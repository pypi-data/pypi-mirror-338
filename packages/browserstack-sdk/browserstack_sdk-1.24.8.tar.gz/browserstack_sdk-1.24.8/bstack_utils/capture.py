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
import builtins
import logging
class bstack11l11lll1l_opy_:
    def __init__(self, handler):
        self._1l111l1l11l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1l111l11lll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1l1l111_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᕝ"), bstack1l1l111_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᕞ"), bstack1l1l111_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬᕟ"), bstack1l1l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᕠ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1l111l11l11_opy_
        self._1l111l1l111_opy_()
    def _1l111l11l11_opy_(self, *args, **kwargs):
        self._1l111l1l11l_opy_(*args, **kwargs)
        message = bstack1l1l111_opy_ (u"࠭ࠠࠨᕡ").join(map(str, args)) + bstack1l1l111_opy_ (u"ࠧ࡝ࡰࠪᕢ")
        self._log_message(bstack1l1l111_opy_ (u"ࠨࡋࡑࡊࡔ࠭ᕣ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1l1l111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᕤ"): level, bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᕥ"): msg})
    def _1l111l1l111_opy_(self):
        for level, bstack1l111l11l1l_opy_ in self._1l111l11lll_opy_.items():
            setattr(logging, level, self._1l111l11ll1_opy_(level, bstack1l111l11l1l_opy_))
    def _1l111l11ll1_opy_(self, level, bstack1l111l11l1l_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1l111l11l1l_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1l111l1l11l_opy_
        for level, bstack1l111l11l1l_opy_ in self._1l111l11lll_opy_.items():
            setattr(logging, level, bstack1l111l11l1l_opy_)