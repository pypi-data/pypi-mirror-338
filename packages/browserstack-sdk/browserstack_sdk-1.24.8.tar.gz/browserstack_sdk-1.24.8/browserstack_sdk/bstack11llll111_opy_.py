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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.accessibility as bstack11l1l1lll_opy_
from browserstack_sdk.bstack1lll1111l1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11ll1111l1_opy_
class bstack1l11l111_opy_:
    def __init__(self, args, logger, bstack111l1l1ll1_opy_, bstack111l1ll111_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l1ll1_opy_ = bstack111l1l1ll1_opy_
        self.bstack111l1ll111_opy_ = bstack111l1ll111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111l1l11l_opy_ = []
        self.bstack111l1l11ll_opy_ = None
        self.bstack1111l1l1l_opy_ = []
        self.bstack111l1l11l1_opy_ = self.bstack1l1111l11_opy_()
        self.bstack1ll1l1ll_opy_ = -1
    def bstack111l1ll1_opy_(self, bstack111l1ll1ll_opy_):
        self.parse_args()
        self.bstack111l11l1ll_opy_()
        self.bstack111l1lll11_opy_(bstack111l1ll1ll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111l1l1111_opy_():
        import importlib
        if getattr(importlib, bstack1l1l111_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ྥ"), False):
            bstack111l1l1l1l_opy_ = importlib.find_loader(bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫྦ"))
        else:
            bstack111l1l1l1l_opy_ = importlib.util.find_spec(bstack1l1l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬྦྷ"))
    def bstack111l1ll1l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1ll1l1ll_opy_ = -1
        if self.bstack111l1ll111_opy_ and bstack1l1l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫྨ") in self.bstack111l1l1ll1_opy_:
            self.bstack1ll1l1ll_opy_ = int(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬྩ")])
        try:
            bstack111l1l1l11_opy_ = [bstack1l1l111_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨྪ"), bstack1l1l111_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪྫ"), bstack1l1l111_opy_ (u"ࠨ࠯ࡳࠫྫྷ")]
            if self.bstack1ll1l1ll_opy_ >= 0:
                bstack111l1l1l11_opy_.extend([bstack1l1l111_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྭ"), bstack1l1l111_opy_ (u"ࠪ࠱ࡳ࠭ྮ")])
            for arg in bstack111l1l1l11_opy_:
                self.bstack111l1ll1l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l11l1ll_opy_(self):
        bstack111l1l11ll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111l1l11ll_opy_ = bstack111l1l11ll_opy_
        return bstack111l1l11ll_opy_
    def bstack1l1lll1111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111l1l1111_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11ll1111l1_opy_)
    def bstack111l1lll11_opy_(self, bstack111l1ll1ll_opy_):
        bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
        if bstack111l1ll1ll_opy_:
            self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨྯ"))
            self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"࡚ࠬࡲࡶࡧࠪྰ"))
        if bstack111l11l1l_opy_.bstack111l1l111l_opy_():
            self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬྱ"))
            self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠧࡕࡴࡸࡩࠬྲ"))
        self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠨ࠯ࡳࠫླ"))
        self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧྴ"))
        self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬྵ"))
        self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫྶ"))
        if self.bstack1ll1l1ll_opy_ > 1:
            self.bstack111l1l11ll_opy_.append(bstack1l1l111_opy_ (u"ࠬ࠳࡮ࠨྷ"))
            self.bstack111l1l11ll_opy_.append(str(self.bstack1ll1l1ll_opy_))
    def bstack111l11lll1_opy_(self):
        bstack1111l1l1l_opy_ = []
        for spec in self.bstack111l1l11l_opy_:
            bstack111ll11l_opy_ = [spec]
            bstack111ll11l_opy_ += self.bstack111l1l11ll_opy_
            bstack1111l1l1l_opy_.append(bstack111ll11l_opy_)
        self.bstack1111l1l1l_opy_ = bstack1111l1l1l_opy_
        return bstack1111l1l1l_opy_
    def bstack1l1111l11_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1l11l1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1l11l1_opy_ = False
        return self.bstack111l1l11l1_opy_
    def bstack1l11llll1l_opy_(self, bstack111l11ll1l_opy_, bstack111l1ll1_opy_):
        bstack111l1ll1_opy_[bstack1l1l111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ྸ")] = self.bstack111l1l1ll1_opy_
        multiprocessing.set_start_method(bstack1l1l111_opy_ (u"ࠧࡴࡲࡤࡻࡳ࠭ྐྵ"))
        bstack1l111l1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack111l1ll11l_opy_ = manager.list()
        if bstack1l1l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྺ") in self.bstack111l1l1ll1_opy_:
            for index, platform in enumerate(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྻ")]):
                bstack1l111l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111l11ll1l_opy_,
                                                            args=(self.bstack111l1l11ll_opy_, bstack111l1ll1_opy_, bstack111l1ll11l_opy_)))
            bstack111l11ll11_opy_ = len(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྼ")])
        else:
            bstack1l111l1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111l11ll1l_opy_,
                                                        args=(self.bstack111l1l11ll_opy_, bstack111l1ll1_opy_, bstack111l1ll11l_opy_)))
            bstack111l11ll11_opy_ = 1
        i = 0
        for t in bstack1l111l1l_opy_:
            os.environ[bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ྽")] = str(i)
            if bstack1l1l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྾") in self.bstack111l1l1ll1_opy_:
                os.environ[bstack1l1l111_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ྿")] = json.dumps(self.bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿀")][i % bstack111l11ll11_opy_])
            i += 1
            t.start()
        for t in bstack1l111l1l_opy_:
            t.join()
        return list(bstack111l1ll11l_opy_)
    @staticmethod
    def bstack111ll1lll_opy_(driver, bstack111l1l1lll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ࿁"), None)
        if item and getattr(item, bstack1l1l111_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡣࡢࡵࡨࠫ࿂"), None) and not getattr(item, bstack1l1l111_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡴࡶ࡟ࡥࡱࡱࡩࠬ࿃"), False):
            logger.info(
                bstack1l1l111_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠥ࿄"))
            bstack111l11llll_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11l1l1lll_opy_.bstack11llllllll_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)