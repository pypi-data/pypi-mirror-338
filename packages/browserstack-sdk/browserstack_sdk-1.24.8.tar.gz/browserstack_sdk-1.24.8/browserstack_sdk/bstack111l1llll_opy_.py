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
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l1111ll1l_opy_():
  def __init__(self, args, logger, bstack111l1l1ll1_opy_, bstack111l1ll111_opy_, bstack111l11l1l1_opy_):
    self.args = args
    self.logger = logger
    self.bstack111l1l1ll1_opy_ = bstack111l1l1ll1_opy_
    self.bstack111l1ll111_opy_ = bstack111l1ll111_opy_
    self.bstack111l11l1l1_opy_ = bstack111l11l1l1_opy_
  def bstack1l11llll1l_opy_(self, bstack111l11ll1l_opy_, bstack111l1ll1_opy_, bstack111l11l11l_opy_=False):
    bstack1l111l1l_opy_ = []
    manager = multiprocessing.Manager()
    bstack111l1ll11l_opy_ = manager.list()
    bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
    if bstack111l11l11l_opy_:
      for index, platform in enumerate(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿅")]):
        if index == 0:
          bstack111l1ll1_opy_[bstack1l1l111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦ࿆ࠩ")] = self.args
        bstack1l111l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111l11ll1l_opy_,
                                                    args=(bstack111l1ll1_opy_, bstack111l1ll11l_opy_)))
    else:
      for index, platform in enumerate(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿇")]):
        bstack1l111l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111l11ll1l_opy_,
                                                    args=(bstack111l1ll1_opy_, bstack111l1ll11l_opy_)))
    i = 0
    for t in bstack1l111l1l_opy_:
      try:
        if bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ࿈")):
          os.environ[bstack1l1l111_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ࿉")] = json.dumps(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿊")][i % self.bstack111l11l1l1_opy_])
      except Exception as e:
        self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹ࠺ࠡࡽࢀࠦ࿋").format(str(e)))
      i += 1
      t.start()
    for t in bstack1l111l1l_opy_:
      t.join()
    return list(bstack111l1ll11l_opy_)