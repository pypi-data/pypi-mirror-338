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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack1111ll11ll_opy_,
)
from bstack_utils.helper import  bstack1l11ll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111l111_opy_, bstack1111111l1l_opy_, bstack1lllll11111_opy_, bstack1lllll111ll_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11lll11lll_opy_ import bstack1lll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll111lll_opy_ import bstack1lll1lll1ll_opy_
from bstack_utils.percy import bstack1lll1l1l1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1lll11l1ll1_opy_(bstack1lllll1l111_opy_):
    def __init__(self, bstack1l1llllllll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1llllllll_opy_ = bstack1l1llllllll_opy_
        self.percy = bstack1lll1l1l1l_opy_()
        self.bstack111lll11_opy_ = bstack1lll1llll1_opy_()
        self.bstack1l1lllll1l1_opy_()
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.PRE), self.bstack1ll11111111_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), self.bstack1ll1l1ll111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll11111ll1_opy_(self, instance: bstack1111ll11ll_opy_, driver: object):
        bstack1ll11l1ll1l_opy_ = TestFramework.bstack1111l1ll1l_opy_(instance.context)
        for t in bstack1ll11l1ll1l_opy_:
            bstack1ll11ll1l1l_opy_ = TestFramework.bstack1111l111l1_opy_(t, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
            if any(instance is d[1] for d in bstack1ll11ll1l1l_opy_) or instance == driver:
                return t
    def bstack1ll11111111_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lll1l11lll_opy_.bstack1ll1ll111ll_opy_(method_name):
                return
            platform_index = f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_, 0)
            bstack1ll11l11lll_opy_ = self.bstack1ll11111ll1_opy_(instance, driver)
            bstack1l1llll1l11_opy_ = TestFramework.bstack1111l111l1_opy_(bstack1ll11l11lll_opy_, TestFramework.bstack1l1llll1l1l_opy_, None)
            if not bstack1l1llll1l11_opy_:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡶࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡡࡴࠢࡶࡩࡸࡹࡩࡰࡰࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡽࡪࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠣᇕ"))
                return
            driver_command = f.bstack1ll1ll1l1ll_opy_(*args)
            for command in bstack1l1l111lll_opy_:
                if command == driver_command:
                    self.bstack1l1lllllll_opy_(driver, platform_index)
            bstack11l1l11l1_opy_ = self.percy.bstack11llllll1_opy_()
            if driver_command in bstack11ll11lll_opy_[bstack11l1l11l1_opy_]:
                self.bstack111lll11_opy_.bstack1ll11lll1l_opy_(bstack1l1llll1l11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡪࡸࡲࡰࡴࠥᇖ"), e)
    def bstack1ll1l1ll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
        bstack1ll11ll1l1l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇗ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠦࠧᇘ"))
            return
        if len(bstack1ll11ll1l1l_opy_) > 1:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇙ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠨࠢᇚ"))
        bstack1l1llll1lll_opy_, bstack1l1lllllll1_opy_ = bstack1ll11ll1l1l_opy_[0]
        driver = bstack1l1llll1lll_opy_()
        if not driver:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇛ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠣࠤᇜ"))
            return
        bstack1l1llllll1l_opy_ = {
            TestFramework.bstack1ll1l1l1ll1_opy_: bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᇝ"),
            TestFramework.bstack1ll1ll1ll11_opy_: bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࠡࡷࡸ࡭ࡩࠨᇞ"),
            TestFramework.bstack1l1llll1l1l_opy_: bstack1l1l111_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡵࡩࡷࡻ࡮ࠡࡰࡤࡱࡪࠨᇟ")
        }
        bstack1l1lllll1ll_opy_ = { key: f.bstack1111l111l1_opy_(instance, key) for key in bstack1l1llllll1l_opy_ }
        bstack1l1lllll11l_opy_ = [key for key, value in bstack1l1lllll1ll_opy_.items() if not value]
        if bstack1l1lllll11l_opy_:
            for key in bstack1l1lllll11l_opy_:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠣᇠ") + str(key) + bstack1l1l111_opy_ (u"ࠨࠢᇡ"))
            return
        platform_index = f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_, 0)
        if self.bstack1l1llllllll_opy_.percy_capture_mode == bstack1l1l111_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᇢ"):
            bstack1l1lll1l_opy_ = bstack1l1lllll1ll_opy_.get(TestFramework.bstack1l1llll1l1l_opy_) + bstack1l1l111_opy_ (u"ࠣ࠯ࡷࡩࡸࡺࡣࡢࡵࡨࠦᇣ")
            bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1l1lllll111_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l1lll1l_opy_,
                bstack1l1lll11ll_opy_=bstack1l1lllll1ll_opy_[TestFramework.bstack1ll1l1l1ll1_opy_],
                bstack1l1111ll_opy_=bstack1l1lllll1ll_opy_[TestFramework.bstack1ll1ll1ll11_opy_],
                bstack1l111l1ll1_opy_=platform_index
            )
            bstack1llll11ll11_opy_.end(EVENTS.bstack1l1lllll111_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᇤ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᇥ"), True, None, None, None, None, test_name=bstack1l1lll1l_opy_)
    def bstack1l1lllllll_opy_(self, driver, platform_index):
        if self.bstack111lll11_opy_.bstack11l1ll1ll_opy_() is True or self.bstack111lll11_opy_.capturing() is True:
            return
        self.bstack111lll11_opy_.bstack11ll1l111_opy_()
        while not self.bstack111lll11_opy_.bstack11l1ll1ll_opy_():
            bstack1l1llll1l11_opy_ = self.bstack111lll11_opy_.bstack1ll1l111_opy_()
            self.bstack1llll11ll_opy_(driver, bstack1l1llll1l11_opy_, platform_index)
        self.bstack111lll11_opy_.bstack1l1l11lll_opy_()
    def bstack1llll11ll_opy_(self, driver, bstack1l11l111ll_opy_, platform_index, test=None):
        from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
        bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1111111l1_opy_.value)
        if test != None:
            bstack1l1lll11ll_opy_ = getattr(test, bstack1l1l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᇦ"), None)
            bstack1l1111ll_opy_ = getattr(test, bstack1l1l111_opy_ (u"ࠬࡻࡵࡪࡦࠪᇧ"), None)
            PercySDK.screenshot(driver, bstack1l11l111ll_opy_, bstack1l1lll11ll_opy_=bstack1l1lll11ll_opy_, bstack1l1111ll_opy_=bstack1l1111ll_opy_, bstack1l111l1ll1_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l11l111ll_opy_)
        bstack1llll11ll11_opy_.end(EVENTS.bstack1111111l1_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᇨ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᇩ"), True, None, None, None, None, test_name=bstack1l11l111ll_opy_)
    def bstack1l1lllll1l1_opy_(self):
        os.environ[bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᇪ")] = str(self.bstack1l1llllllll_opy_.success)
        os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ᇫ")] = str(self.bstack1l1llllllll_opy_.percy_capture_mode)
        self.percy.bstack1l1llllll11_opy_(self.bstack1l1llllllll_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1llll1ll1_opy_(self.bstack1l1llllllll_opy_.percy_build_id)