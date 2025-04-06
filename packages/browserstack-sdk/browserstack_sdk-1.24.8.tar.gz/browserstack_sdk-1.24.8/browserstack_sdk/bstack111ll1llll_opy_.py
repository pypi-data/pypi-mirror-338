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
class RobotHandler():
    def __init__(self, args, logger, bstack111l1l1ll1_opy_, bstack111l1ll111_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l1ll1_opy_ = bstack111l1l1ll1_opy_
        self.bstack111l1ll111_opy_ = bstack111l1ll111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11l111111l_opy_(bstack111l11l111_opy_):
        bstack111l111lll_opy_ = []
        if bstack111l11l111_opy_:
            tokens = str(os.path.basename(bstack111l11l111_opy_)).split(bstack1l1l111_opy_ (u"ࠧࡥࠢ࿌"))
            camelcase_name = bstack1l1l111_opy_ (u"ࠨࠠࠣ࿍").join(t.title() for t in tokens)
            suite_name, bstack111l111l1l_opy_ = os.path.splitext(camelcase_name)
            bstack111l111lll_opy_.append(suite_name)
        return bstack111l111lll_opy_
    @staticmethod
    def bstack111l111ll1_opy_(typename):
        if bstack1l1l111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ࿎") in typename:
            return bstack1l1l111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ࿏")
        return bstack1l1l111_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ࿐")