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
from datetime import datetime, timezone
from pyexpat import features
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1111l111ll_opy_ import bstack11111llll1_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack111111l111_opy_,
    bstack1111111l1l_opy_,
    bstack1lllll11111_opy_,
    bstack1l11l1lllll_opy_,
    bstack1lllll111ll_opy_,
)
import traceback
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
from bstack_utils.constants import EVENTS
class PytestBDDFramework(TestFramework):
    bstack1l11l1lll11_opy_ = bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧግ")
    bstack1l1l11111ll_opy_ = bstack1l1l111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࠦጎ")
    bstack1l11l1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨጏ")
    bstack1l11ll1llll_opy_ = bstack1l1l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࠥጐ")
    bstack1l1l11l11ll_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧ጑")
    bstack1l11ll1111l_opy_: bool
    bstack1l1l1111l11_opy_ = [
        bstack111111l111_opy_.BEFORE_ALL,
        bstack111111l111_opy_.AFTER_ALL,
        bstack111111l111_opy_.BEFORE_EACH,
        bstack111111l111_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l11ll111ll_opy_: Dict[str, str],
        bstack1lll1111l1l_opy_: List[str]=[bstack1l1l111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢጒ")],
    ):
        super().__init__(bstack1lll1111l1l_opy_, bstack1l11ll111ll_opy_)
        self.bstack1l11ll1111l_opy_ = any(bstack1l1l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣጓ") in item.lower() for item in bstack1lll1111l1l_opy_)
    def track_event(
        self,
        context: bstack1l11l1lllll_opy_,
        test_framework_state: bstack111111l111_opy_,
        test_hook_state: bstack1lllll11111_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack111111l111_opy_.NONE:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࠨጔ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠨࠢጕ"))
            return
        if not self.bstack1l11ll1111l_opy_:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠽ࠣ጖") + str(str(self.bstack1lll1111l1l_opy_)) + bstack1l1l111_opy_ (u"ࠣࠤ጗"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦጘ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠥࠦጙ"))
            return
        instance = self.__1l11lllllll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡦࡸࡧࡴ࠿ࠥጚ") + str(args) + bstack1l1l111_opy_ (u"ࠧࠨጛ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1l1111l11_opy_ and test_hook_state == bstack1lllll11111_opy_.PRE:
                bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack11llll11ll_opy_.value)
                name = str(EVENTS.bstack11llll11ll_opy_.name)+bstack1l1l111_opy_ (u"ࠨ࠺ࠣጜ")+str(test_framework_state.name)
                TestFramework.bstack1l1l111l11l_opy_(instance, name, bstack1ll1ll11lll_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴࠣࡴࡷ࡫࠺ࠡࡽࢀࠦጝ").format(e))
        try:
            if test_framework_state == bstack111111l111_opy_.TEST:
                if not TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1l1l111l1l1_opy_) and test_hook_state == bstack1lllll11111_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1l1l111ll1l_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l1l111_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣጞ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠤࠥጟ"))
                if test_hook_state == bstack1lllll11111_opy_.PRE and not TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll111ll111_opy_):
                    TestFramework.bstack1111lllll1_opy_(instance, TestFramework.bstack1ll111ll111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1l11llllll1_opy_(instance, args)
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣጠ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠦࠧጡ"))
                elif test_hook_state == bstack1lllll11111_opy_.POST and not TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll11l111ll_opy_):
                    TestFramework.bstack1111lllll1_opy_(instance, TestFramework.bstack1ll11l111ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣጢ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠨࠢጣ"))
            elif test_framework_state == bstack111111l111_opy_.STEP:
                if test_hook_state == bstack1lllll11111_opy_.PRE:
                    PytestBDDFramework.__1l1l11l1lll_opy_(instance, args)
                elif test_hook_state == bstack1lllll11111_opy_.POST:
                    PytestBDDFramework.__1l1l11ll1l1_opy_(instance, args)
            elif test_framework_state == bstack111111l111_opy_.LOG and test_hook_state == bstack1lllll11111_opy_.POST:
                PytestBDDFramework.__1l1l11l11l1_opy_(instance, *args)
            elif test_framework_state == bstack111111l111_opy_.LOG_REPORT and test_hook_state == bstack1lllll11111_opy_.POST:
                self.__1l11l1l1lll_opy_(instance, *args)
            elif test_framework_state in PytestBDDFramework.bstack1l1l1111l11_opy_:
                self.__1l11llll11l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣጤ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠣࠤጥ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1l11ll1ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1l1111l11_opy_ and test_hook_state == bstack1lllll11111_opy_.POST:
                name = str(EVENTS.bstack11llll11ll_opy_.name)+bstack1l1l111_opy_ (u"ࠤ࠽ࠦጦ")+str(test_framework_state.name)
                bstack1ll1ll11lll_opy_ = TestFramework.bstack1l11lll1111_opy_(instance, name)
                bstack1llll11ll11_opy_.end(EVENTS.bstack11llll11ll_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥጧ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤጨ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧጩ").format(e))
    def bstack1ll111l1lll_opy_(self):
        return self.bstack1l11ll1111l_opy_
    def __1l11ll1l111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1l111_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥጪ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111l1l1l_opy_(rep, [bstack1l1l111_opy_ (u"ࠢࡸࡪࡨࡲࠧጫ"), bstack1l1l111_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤጬ"), bstack1l1l111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤጭ"), bstack1l1l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥጮ"), bstack1l1l111_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧጯ"), bstack1l1l111_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦጰ")])
        return None
    def __1l11l1l1lll_opy_(self, instance: bstack1111111l1l_opy_, *args):
        result = self.__1l11ll1l111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111l111ll1_opy_ = None
        if result.get(bstack1l1l111_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢጱ"), None) == bstack1l1l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢጲ") and len(args) > 1 and getattr(args[1], bstack1l1l111_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤጳ"), None) is not None:
            failure = [{bstack1l1l111_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬጴ"): [args[1].excinfo.exconly(), result.get(bstack1l1l111_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤጵ"), None)]}]
            bstack111l111ll1_opy_ = bstack1l1l111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧጶ") if bstack1l1l111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣጷ") in getattr(args[1].excinfo, bstack1l1l111_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣጸ"), bstack1l1l111_opy_ (u"ࠢࠣጹ")) else bstack1l1l111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤጺ")
        bstack1l1l11l1l11_opy_ = result.get(bstack1l1l111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥጻ"), TestFramework.bstack1l1l1111l1l_opy_)
        if bstack1l1l11l1l11_opy_ != TestFramework.bstack1l1l1111l1l_opy_:
            TestFramework.bstack1111lllll1_opy_(instance, TestFramework.bstack1ll111lll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1l11lll1l1l_opy_(instance, {
            TestFramework.bstack1l1ll1l1l11_opy_: failure,
            TestFramework.bstack1l11llll1l1_opy_: bstack111l111ll1_opy_,
            TestFramework.bstack1l1ll11llll_opy_: bstack1l1l11l1l11_opy_,
        })
    def __1l11lllllll_opy_(
        self,
        context: bstack1l11l1lllll_opy_,
        test_framework_state: bstack111111l111_opy_,
        test_hook_state: bstack1lllll11111_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack111111l111_opy_.SETUP_FIXTURE:
            instance = self.__1l11lll1lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1l1111111_opy_ bstack1l1l11l111l_opy_ this to be bstack1l1l111_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥጼ")
            if test_framework_state == bstack111111l111_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1l111l111_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack111111l111_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1l111_opy_ (u"ࠦࡳࡵࡤࡦࠤጽ"), None), bstack1l1l111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧጾ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1l111_opy_ (u"ࠨ࡮ࡰࡦࡨࠦጿ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l1l111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢፀ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack11111l1lll_opy_(target) if target else None
        return instance
    def __1l11llll11l_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        test_framework_state: bstack111111l111_opy_,
        test_hook_state: bstack1lllll11111_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l11llll111_opy_ = TestFramework.bstack1111l111l1_opy_(instance, PytestBDDFramework.bstack1l1l11111ll_opy_, {})
        if not key in bstack1l11llll111_opy_:
            bstack1l11llll111_opy_[key] = []
        bstack1l11ll11lll_opy_ = TestFramework.bstack1111l111l1_opy_(instance, PytestBDDFramework.bstack1l11l1ll1ll_opy_, {})
        if not key in bstack1l11ll11lll_opy_:
            bstack1l11ll11lll_opy_[key] = []
        bstack1l11ll1l1ll_opy_ = {
            PytestBDDFramework.bstack1l1l11111ll_opy_: bstack1l11llll111_opy_,
            PytestBDDFramework.bstack1l11l1ll1ll_opy_: bstack1l11ll11lll_opy_,
        }
        if test_hook_state == bstack1lllll11111_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l1l111_opy_ (u"ࠣ࡭ࡨࡽࠧፁ"): key,
                TestFramework.bstack1l11lll11l1_opy_: uuid4().__str__(),
                TestFramework.bstack1l11lllll1l_opy_: TestFramework.bstack1l1l11111l1_opy_,
                TestFramework.bstack1l11ll1l1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1l111l1ll_opy_: [],
                TestFramework.bstack1l11ll1ll11_opy_: hook_name
            }
            bstack1l11llll111_opy_[key].append(hook)
            bstack1l11ll1l1ll_opy_[PytestBDDFramework.bstack1l11ll1llll_opy_] = key
        elif test_hook_state == bstack1lllll11111_opy_.POST:
            bstack1l1l111111l_opy_ = bstack1l11llll111_opy_.get(key, [])
            hook = bstack1l1l111111l_opy_.pop() if bstack1l1l111111l_opy_ else None
            if hook:
                result = self.__1l11ll1l111_opy_(*args)
                if result:
                    bstack1l11ll1l11l_opy_ = result.get(bstack1l1l111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥፂ"), TestFramework.bstack1l1l11111l1_opy_)
                    if bstack1l11ll1l11l_opy_ != TestFramework.bstack1l1l11111l1_opy_:
                        hook[TestFramework.bstack1l11lllll1l_opy_] = bstack1l11ll1l11l_opy_
                hook[TestFramework.bstack1l11l1llll1_opy_] = datetime.now(tz=timezone.utc)
                bstack1l11ll11lll_opy_[key].append(hook)
                bstack1l11ll1l1ll_opy_[PytestBDDFramework.bstack1l1l11l11ll_opy_] = key
        TestFramework.bstack1l11lll1l1l_opy_(instance, bstack1l11ll1l1ll_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤፃ") + str(bstack1l11ll11lll_opy_) + bstack1l1l111_opy_ (u"ࠦࠧፄ"))
    def __1l11lll1lll_opy_(
        self,
        context: bstack1l11l1lllll_opy_,
        test_framework_state: bstack111111l111_opy_,
        test_hook_state: bstack1lllll11111_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111l1l1l_opy_(args[0], [bstack1l1l111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦፅ"), bstack1l1l111_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢፆ"), bstack1l1l111_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢፇ"), bstack1l1l111_opy_ (u"ࠣ࡫ࡧࡷࠧፈ"), bstack1l1l111_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦፉ"), bstack1l1l111_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥፊ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l1l111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥፋ")) else fixturedef.get(bstack1l1l111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦፌ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1l111_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦፍ")) else None
        node = request.node if hasattr(request, bstack1l1l111_opy_ (u"ࠢ࡯ࡱࡧࡩࠧፎ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1l111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣፏ")) else None
        baseid = fixturedef.get(bstack1l1l111_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤፐ"), None) or bstack1l1l111_opy_ (u"ࠥࠦፑ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1l111_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤፒ")):
            target = PytestBDDFramework.__1l1l11lll1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1l111_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢፓ")) else None
            if target and not TestFramework.bstack11111l1lll_opy_(target):
                self.__1l1l111l111_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣፔ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠢࠣፕ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨፖ") + str(target) + bstack1l1l111_opy_ (u"ࠤࠥፗ"))
            return None
        instance = TestFramework.bstack11111l1lll_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧፘ") + str(target) + bstack1l1l111_opy_ (u"ࠦࠧፙ"))
            return None
        bstack1l1l11l1111_opy_ = TestFramework.bstack1111l111l1_opy_(instance, PytestBDDFramework.bstack1l11l1lll11_opy_, {})
        if os.getenv(bstack1l1l111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨፚ"), bstack1l1l111_opy_ (u"ࠨ࠱ࠣ፛")) == bstack1l1l111_opy_ (u"ࠢ࠲ࠤ፜"):
            bstack1l1l11l1l1l_opy_ = bstack1l1l111_opy_ (u"ࠣ࠼ࠥ፝").join((scope, fixturename))
            bstack1l11lll11ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1l11l1ll1l1_opy_ = {
                bstack1l1l111_opy_ (u"ࠤ࡮ࡩࡾࠨ፞"): bstack1l1l11l1l1l_opy_,
                bstack1l1l111_opy_ (u"ࠥࡸࡦ࡭ࡳࠣ፟"): PytestBDDFramework.__1l11l1ll111_opy_(request.node, scenario),
                bstack1l1l111_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧ፠"): fixturedef,
                bstack1l1l111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ፡"): scope,
                bstack1l1l111_opy_ (u"ࠨࡴࡺࡲࡨࠦ።"): None,
            }
            try:
                if test_hook_state == bstack1lllll11111_opy_.POST and callable(getattr(args[-1], bstack1l1l111_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦ፣"), None)):
                    bstack1l11l1ll1l1_opy_[bstack1l1l111_opy_ (u"ࠣࡶࡼࡴࡪࠨ፤")] = TestFramework.bstack1ll111ll1ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lllll11111_opy_.PRE:
                bstack1l11l1ll1l1_opy_[bstack1l1l111_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ፥")] = uuid4().__str__()
                bstack1l11l1ll1l1_opy_[PytestBDDFramework.bstack1l11ll1l1l1_opy_] = bstack1l11lll11ll_opy_
            elif test_hook_state == bstack1lllll11111_opy_.POST:
                bstack1l11l1ll1l1_opy_[PytestBDDFramework.bstack1l11l1llll1_opy_] = bstack1l11lll11ll_opy_
            if bstack1l1l11l1l1l_opy_ in bstack1l1l11l1111_opy_:
                bstack1l1l11l1111_opy_[bstack1l1l11l1l1l_opy_].update(bstack1l11l1ll1l1_opy_)
                self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦ፦") + str(bstack1l1l11l1111_opy_[bstack1l1l11l1l1l_opy_]) + bstack1l1l111_opy_ (u"ࠦࠧ፧"))
            else:
                bstack1l1l11l1111_opy_[bstack1l1l11l1l1l_opy_] = bstack1l11l1ll1l1_opy_
                self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣ፨") + str(len(bstack1l1l11l1111_opy_)) + bstack1l1l111_opy_ (u"ࠨࠢ፩"))
        TestFramework.bstack1111lllll1_opy_(instance, PytestBDDFramework.bstack1l11l1lll11_opy_, bstack1l1l11l1111_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢ፪") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠣࠤ፫"))
        return instance
    def __1l1l111l111_opy_(
        self,
        context: bstack1l11l1lllll_opy_,
        test_framework_state: bstack111111l111_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack11111llll1_opy_.create_context(target)
        ob = bstack1111111l1l_opy_(ctx, self.bstack1lll1111l1l_opy_, self.bstack1l11ll111ll_opy_, test_framework_state)
        TestFramework.bstack1l11lll1l1l_opy_(ob, {
            TestFramework.bstack1ll1lllll1l_opy_: context.test_framework_name,
            TestFramework.bstack1ll11l1l11l_opy_: context.test_framework_version,
            TestFramework.bstack1l11ll1ll1l_opy_: [],
            PytestBDDFramework.bstack1l11l1lll11_opy_: {},
            PytestBDDFramework.bstack1l11l1ll1ll_opy_: {},
            PytestBDDFramework.bstack1l1l11111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111lllll1_opy_(ob, TestFramework.bstack1l11l1lll1l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111lllll1_opy_(ob, TestFramework.bstack1ll1llll111_opy_, context.platform_index)
        TestFramework.bstack1111lll11l_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤ፬") + str(TestFramework.bstack1111lll11l_opy_.keys()) + bstack1l1l111_opy_ (u"ࠥࠦ፭"))
        return ob
    @staticmethod
    def __1l11llllll1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1l111_opy_ (u"ࠫ࡮ࡪࠧ፮"): id(step),
                bstack1l1l111_opy_ (u"ࠬࡺࡥࡹࡶࠪ፯"): step.name,
                bstack1l1l111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧ፰"): step.keyword,
            })
        meta = {
            bstack1l1l111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨ፱"): {
                bstack1l1l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭፲"): feature.name,
                bstack1l1l111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ፳"): feature.filename,
                bstack1l1l111_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨ፴"): feature.description
            },
            bstack1l1l111_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭፵"): {
                bstack1l1l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ፶"): scenario.name
            },
            bstack1l1l111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ፷"): steps,
            bstack1l1l111_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩ፸"): PytestBDDFramework.__1l1l1111lll_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l11ll11l11_opy_: meta
            }
        )
    @staticmethod
    def __1l1l11l1lll_opy_(instance, args):
        request, bstack1l11lllll11_opy_ = args
        bstack1l1l11ll111_opy_ = id(bstack1l11lllll11_opy_)
        bstack1l1l11l1ll1_opy_ = instance.data[TestFramework.bstack1l11ll11l11_opy_]
        step = next(filter(lambda st: st[bstack1l1l111_opy_ (u"ࠨ࡫ࡧࠫ፹")] == bstack1l1l11ll111_opy_, bstack1l1l11l1ll1_opy_[bstack1l1l111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ፺")]), None)
        step.update({
            bstack1l1l111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ፻"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1l1l11l1ll1_opy_[bstack1l1l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ፼")]) if st[bstack1l1l111_opy_ (u"ࠬ࡯ࡤࠨ፽")] == step[bstack1l1l111_opy_ (u"࠭ࡩࡥࠩ፾")]), None)
        if index is not None:
            bstack1l1l11l1ll1_opy_[bstack1l1l111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭፿")][index] = step
        instance.data[TestFramework.bstack1l11ll11l11_opy_] = bstack1l1l11l1ll1_opy_
    @staticmethod
    def __1l1l11ll1l1_opy_(instance, args):
        bstack1l1l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡽࡨࡦࡰࠣࡰࡪࡴࠠࡢࡴࡪࡷࠥ࡯ࡳࠡ࠴࠯ࠤ࡮ࡺࠠࡴ࡫ࡪࡲ࡮࡬ࡩࡦࡵࠣࡸ࡭࡫ࡲࡦࠢ࡬ࡷࠥࡴ࡯ࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࡹࠠࡢࡴࡨࠤ࠲࡛ࠦࡳࡧࡴࡹࡪࡹࡴ࠭ࠢࡶࡸࡪࡶ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡧࡲࡨࡵࠣࡥࡷ࡫ࠠ࠴ࠢࡷ࡬ࡪࡴࠠࡵࡪࡨࠤࡱࡧࡳࡵࠢࡹࡥࡱࡻࡥࠡ࡫ࡶࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᎀ")
        bstack1l1l11lll11_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l11lllll11_opy_ = args[1]
        bstack1l1l11ll111_opy_ = id(bstack1l11lllll11_opy_)
        bstack1l1l11l1ll1_opy_ = instance.data[TestFramework.bstack1l11ll11l11_opy_]
        step = None
        if bstack1l1l11ll111_opy_ is not None and bstack1l1l11l1ll1_opy_.get(bstack1l1l111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᎁ")):
            step = next(filter(lambda st: st[bstack1l1l111_opy_ (u"ࠪ࡭ࡩ࠭ᎂ")] == bstack1l1l11ll111_opy_, bstack1l1l11l1ll1_opy_[bstack1l1l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᎃ")]), None)
            step.update({
                bstack1l1l111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᎄ"): bstack1l1l11lll11_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l1l111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᎅ"): bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᎆ"),
                bstack1l1l111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᎇ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l1l111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᎈ"): bstack1l1l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᎉ"),
                })
        index = next((i for i, st in enumerate(bstack1l1l11l1ll1_opy_[bstack1l1l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᎊ")]) if st[bstack1l1l111_opy_ (u"ࠬ࡯ࡤࠨᎋ")] == step[bstack1l1l111_opy_ (u"࠭ࡩࡥࠩᎌ")]), None)
        if index is not None:
            bstack1l1l11l1ll1_opy_[bstack1l1l111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᎍ")][index] = step
        instance.data[TestFramework.bstack1l11ll11l11_opy_] = bstack1l1l11l1ll1_opy_
    @staticmethod
    def __1l1l1111lll_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l1l111_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᎎ")):
                examples = list(node.callspec.params[bstack1l1l111_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᎏ")].values())
            return examples
        except:
            return []
    def bstack1ll11lll11l_opy_(self, instance: bstack1111111l1l_opy_, bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_]):
        bstack1l11ll111l1_opy_ = (
            PytestBDDFramework.bstack1l11ll1llll_opy_
            if bstack11111l1l1l_opy_[1] == bstack1lllll11111_opy_.PRE
            else PytestBDDFramework.bstack1l1l11l11ll_opy_
        )
        hook = PytestBDDFramework.bstack1l11ll11ll1_opy_(instance, bstack1l11ll111l1_opy_)
        entries = hook.get(TestFramework.bstack1l1l111l1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1l11ll1ll1l_opy_, []))
        return entries
    def bstack1ll111ll1l1_opy_(self, instance: bstack1111111l1l_opy_, bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_]):
        bstack1l11ll111l1_opy_ = (
            PytestBDDFramework.bstack1l11ll1llll_opy_
            if bstack11111l1l1l_opy_[1] == bstack1lllll11111_opy_.PRE
            else PytestBDDFramework.bstack1l1l11l11ll_opy_
        )
        PytestBDDFramework.bstack1l1l111ll11_opy_(instance, bstack1l11ll111l1_opy_)
        TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1l11ll1ll1l_opy_, []).clear()
    @staticmethod
    def bstack1l11ll11ll1_opy_(instance: bstack1111111l1l_opy_, bstack1l11ll111l1_opy_: str):
        bstack1l11lll1ll1_opy_ = (
            PytestBDDFramework.bstack1l11l1ll1ll_opy_
            if bstack1l11ll111l1_opy_ == PytestBDDFramework.bstack1l1l11l11ll_opy_
            else PytestBDDFramework.bstack1l1l11111ll_opy_
        )
        bstack1l11llll1ll_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1l11ll111l1_opy_, None)
        bstack1l1l1111ll1_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1l11lll1ll1_opy_, None) if bstack1l11llll1ll_opy_ else None
        return (
            bstack1l1l1111ll1_opy_[bstack1l11llll1ll_opy_][-1]
            if isinstance(bstack1l1l1111ll1_opy_, dict) and len(bstack1l1l1111ll1_opy_.get(bstack1l11llll1ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l1l111ll11_opy_(instance: bstack1111111l1l_opy_, bstack1l11ll111l1_opy_: str):
        hook = PytestBDDFramework.bstack1l11ll11ll1_opy_(instance, bstack1l11ll111l1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1l111l1ll_opy_, []).clear()
    @staticmethod
    def __1l1l11l11l1_opy_(instance: bstack1111111l1l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1l111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡦࡳࡷࡪࡳࠣ᎐"), None)):
            return
        if os.getenv(bstack1l1l111_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡐࡔࡍࡓࠣ᎑"), bstack1l1l111_opy_ (u"ࠧ࠷ࠢ᎒")) != bstack1l1l111_opy_ (u"ࠨ࠱ࠣ᎓"):
            PytestBDDFramework.logger.warning(bstack1l1l111_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡯࡮ࡨࠢࡦࡥࡵࡲ࡯ࡨࠤ᎔"))
            return
        bstack1l11ll11l1l_opy_ = {
            bstack1l1l111_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ᎕"): (PytestBDDFramework.bstack1l11ll1llll_opy_, PytestBDDFramework.bstack1l1l11111ll_opy_),
            bstack1l1l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦ᎖"): (PytestBDDFramework.bstack1l1l11l11ll_opy_, PytestBDDFramework.bstack1l11l1ll1ll_opy_),
        }
        for when in (bstack1l1l111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ᎗"), bstack1l1l111_opy_ (u"ࠦࡨࡧ࡬࡭ࠤ᎘"), bstack1l1l111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ᎙")):
            bstack1l1l111llll_opy_ = args[1].get_records(when)
            if not bstack1l1l111llll_opy_:
                continue
            records = [
                bstack1lllll111ll_opy_(
                    kind=TestFramework.bstack1ll1111ll11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1l111_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠤ᎚")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1l111_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࠣ᎛")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1l111llll_opy_
                if isinstance(getattr(r, bstack1l1l111_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤ᎜"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l1l11ll11l_opy_, bstack1l11lll1ll1_opy_ = bstack1l11ll11l1l_opy_.get(when, (None, None))
            bstack1l11lll1l11_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1l1l11ll11l_opy_, None) if bstack1l1l11ll11l_opy_ else None
            bstack1l1l1111ll1_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1l11lll1ll1_opy_, None) if bstack1l11lll1l11_opy_ else None
            if isinstance(bstack1l1l1111ll1_opy_, dict) and len(bstack1l1l1111ll1_opy_.get(bstack1l11lll1l11_opy_, [])) > 0:
                hook = bstack1l1l1111ll1_opy_[bstack1l11lll1l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l1l111l1ll_opy_ in hook:
                    hook[TestFramework.bstack1l1l111l1ll_opy_].extend(records)
                    continue
            logs = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1l11ll1ll1l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l1l111ll1l_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        bstack111111111_opy_ = request.node.nodeid
        test_name = PytestBDDFramework.__1l11lll111l_opy_(request.node, scenario)
        bstack1l11l1ll11l_opy_ = feature.filename
        if not bstack111111111_opy_ or not test_name or not bstack1l11l1ll11l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1ll1ll1ll11_opy_: uuid4().__str__(),
            TestFramework.bstack1l1l111l1l1_opy_: bstack111111111_opy_,
            TestFramework.bstack1ll1l1l1ll1_opy_: test_name,
            TestFramework.bstack1l1llll1l1l_opy_: bstack111111111_opy_,
            TestFramework.bstack1l1l111lll1_opy_: bstack1l11l1ll11l_opy_,
            TestFramework.bstack1l11ll11111_opy_: PytestBDDFramework.__1l11l1ll111_opy_(feature, scenario),
            TestFramework.bstack1l11ll1lll1_opy_: code,
            TestFramework.bstack1l1ll11llll_opy_: TestFramework.bstack1l1l1111l1l_opy_,
            TestFramework.bstack1l1l1ll111l_opy_: test_name
        }
    @staticmethod
    def __1l11lll111l_opy_(node, scenario):
        if hasattr(node, bstack1l1l111_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫ᎝")):
            parts = node.nodeid.rsplit(bstack1l1l111_opy_ (u"ࠥ࡟ࠧ᎞"))
            params = parts[-1]
            return bstack1l1l111_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦ᎟").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1l11l1ll111_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1l1l111_opy_ (u"ࠬࡺࡡࡨࡵࠪᎠ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1l1l111_opy_ (u"࠭ࡴࡢࡩࡶࠫᎡ")) else [])
    @staticmethod
    def __1l1l11lll1l_opy_(location):
        return bstack1l1l111_opy_ (u"ࠢ࠻࠼ࠥᎢ").join(filter(lambda x: isinstance(x, str), location))