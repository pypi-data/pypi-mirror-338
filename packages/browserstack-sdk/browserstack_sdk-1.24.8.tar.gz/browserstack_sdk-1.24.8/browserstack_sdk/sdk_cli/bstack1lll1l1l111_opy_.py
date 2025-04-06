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
from bstack_utils.bstack11l11ll1ll_opy_ import bstack1l1lll1lll_opy_
class bstack1llllllll1l_opy_(TestFramework):
    bstack1l11l1lll11_opy_ = bstack1l1l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᎣ")
    bstack1l1l11111ll_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࠢᎤ")
    bstack1l11l1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᎥ")
    bstack1l11ll1llll_opy_ = bstack1l1l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࠨᎦ")
    bstack1l1l11l11ll_opy_ = bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᎧ")
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
        bstack1lll1111l1l_opy_: List[str]=[bstack1l1l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᎨ")],
    ):
        super().__init__(bstack1lll1111l1l_opy_, bstack1l11ll111ll_opy_)
        self.bstack1l11ll1111l_opy_ = any(bstack1l1l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᎩ") in item.lower() for item in bstack1lll1111l1l_opy_)
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
            self.logger.warning(bstack1l1l111_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࠤᎪ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠤࠥᎫ"))
            return
        if not self.bstack1l11ll1111l_opy_:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡀࠦᎬ") + str(str(self.bstack1lll1111l1l_opy_)) + bstack1l1l111_opy_ (u"ࠦࠧᎭ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᎮ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠨࠢᎯ"))
            return
        instance = self.__1l11lllllll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡢࡴࡪࡷࡂࠨᎰ") + str(args) + bstack1l1l111_opy_ (u"ࠣࠤᎱ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1llllllll1l_opy_.bstack1l1l1111l11_opy_ and test_hook_state == bstack1lllll11111_opy_.PRE:
                bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack11llll11ll_opy_.value)
                name = str(EVENTS.bstack11llll11ll_opy_.name)+bstack1l1l111_opy_ (u"ࠤ࠽ࠦᎲ")+str(test_framework_state.name)
                TestFramework.bstack1l1l111l11l_opy_(instance, name, bstack1ll1ll11lll_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࠦࡰࡳࡧ࠽ࠤࢀࢃࠢᎳ").format(e))
        try:
            if not TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1l1l111l1l1_opy_) and test_hook_state == bstack1lllll11111_opy_.PRE:
                test = bstack1llllllll1l_opy_.__1l1l111ll1l_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡱࡵࡡࡥࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᎴ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠧࠨᎵ"))
            if test_framework_state == bstack111111l111_opy_.TEST:
                if test_hook_state == bstack1lllll11111_opy_.PRE and not TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll111ll111_opy_):
                    TestFramework.bstack1111lllll1_opy_(instance, TestFramework.bstack1ll111ll111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡵࡷࡥࡷࡺࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᎶ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠢࠣᎷ"))
                elif test_hook_state == bstack1lllll11111_opy_.POST and not TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll11l111ll_opy_):
                    TestFramework.bstack1111lllll1_opy_(instance, TestFramework.bstack1ll11l111ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡩࡳࡪࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᎸ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠤࠥᎹ"))
            elif test_framework_state == bstack111111l111_opy_.LOG and test_hook_state == bstack1lllll11111_opy_.POST:
                bstack1llllllll1l_opy_.__1l1l11l11l1_opy_(instance, *args)
            elif test_framework_state == bstack111111l111_opy_.LOG_REPORT and test_hook_state == bstack1lllll11111_opy_.POST:
                self.__1l11l1l1lll_opy_(instance, *args)
            elif test_framework_state in bstack1llllllll1l_opy_.bstack1l1l1111l11_opy_:
                self.__1l11llll11l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᎺ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠦࠧᎻ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1l11ll1ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1llllllll1l_opy_.bstack1l1l1111l11_opy_ and test_hook_state == bstack1lllll11111_opy_.POST:
                name = str(EVENTS.bstack11llll11ll_opy_.name)+bstack1l1l111_opy_ (u"ࠧࡀࠢᎼ")+str(test_framework_state.name)
                bstack1ll1ll11lll_opy_ = TestFramework.bstack1l11lll1111_opy_(instance, name)
                bstack1llll11ll11_opy_.end(EVENTS.bstack11llll11ll_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᎽ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᎾ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᎿ").format(e))
    def bstack1ll111l1lll_opy_(self):
        return self.bstack1l11ll1111l_opy_
    def __1l11ll1l111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1l111_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨᏀ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111l1l1l_opy_(rep, [bstack1l1l111_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᏁ"), bstack1l1l111_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᏂ"), bstack1l1l111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧᏃ"), bstack1l1l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᏄ"), bstack1l1l111_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠣᏅ"), bstack1l1l111_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢᏆ")])
        return None
    def __1l11l1l1lll_opy_(self, instance: bstack1111111l1l_opy_, *args):
        result = self.__1l11ll1l111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111l111ll1_opy_ = None
        if result.get(bstack1l1l111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᏇ"), None) == bstack1l1l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᏈ") and len(args) > 1 and getattr(args[1], bstack1l1l111_opy_ (u"ࠦࡪࡾࡣࡪࡰࡩࡳࠧᏉ"), None) is not None:
            failure = [{bstack1l1l111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᏊ"): [args[1].excinfo.exconly(), result.get(bstack1l1l111_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᏋ"), None)]}]
            bstack111l111ll1_opy_ = bstack1l1l111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᏌ") if bstack1l1l111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᏍ") in getattr(args[1].excinfo, bstack1l1l111_opy_ (u"ࠤࡷࡽࡵ࡫࡮ࡢ࡯ࡨࠦᏎ"), bstack1l1l111_opy_ (u"ࠥࠦᏏ")) else bstack1l1l111_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᏐ")
        bstack1l1l11l1l11_opy_ = result.get(bstack1l1l111_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᏑ"), TestFramework.bstack1l1l1111l1l_opy_)
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
            target = None # bstack1l1l1111111_opy_ bstack1l1l11l111l_opy_ this to be bstack1l1l111_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᏒ")
            if test_framework_state == bstack111111l111_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1l111l111_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack111111l111_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1l111_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᏓ"), None), bstack1l1l111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᏔ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᏕ"), None):
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
        bstack1l11llll111_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1llllllll1l_opy_.bstack1l1l11111ll_opy_, {})
        if not key in bstack1l11llll111_opy_:
            bstack1l11llll111_opy_[key] = []
        bstack1l11ll11lll_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1llllllll1l_opy_.bstack1l11l1ll1ll_opy_, {})
        if not key in bstack1l11ll11lll_opy_:
            bstack1l11ll11lll_opy_[key] = []
        bstack1l11ll1l1ll_opy_ = {
            bstack1llllllll1l_opy_.bstack1l1l11111ll_opy_: bstack1l11llll111_opy_,
            bstack1llllllll1l_opy_.bstack1l11l1ll1ll_opy_: bstack1l11ll11lll_opy_,
        }
        if test_hook_state == bstack1lllll11111_opy_.PRE:
            hook = {
                bstack1l1l111_opy_ (u"ࠥ࡯ࡪࡿࠢᏖ"): key,
                TestFramework.bstack1l11lll11l1_opy_: uuid4().__str__(),
                TestFramework.bstack1l11lllll1l_opy_: TestFramework.bstack1l1l11111l1_opy_,
                TestFramework.bstack1l11ll1l1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1l111l1ll_opy_: [],
                TestFramework.bstack1l11ll1ll11_opy_: args[1] if len(args) > 1 else bstack1l1l111_opy_ (u"ࠫࠬᏗ")
            }
            bstack1l11llll111_opy_[key].append(hook)
            bstack1l11ll1l1ll_opy_[bstack1llllllll1l_opy_.bstack1l11ll1llll_opy_] = key
        elif test_hook_state == bstack1lllll11111_opy_.POST:
            bstack1l1l111111l_opy_ = bstack1l11llll111_opy_.get(key, [])
            hook = bstack1l1l111111l_opy_.pop() if bstack1l1l111111l_opy_ else None
            if hook:
                result = self.__1l11ll1l111_opy_(*args)
                if result:
                    bstack1l11ll1l11l_opy_ = result.get(bstack1l1l111_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᏘ"), TestFramework.bstack1l1l11111l1_opy_)
                    if bstack1l11ll1l11l_opy_ != TestFramework.bstack1l1l11111l1_opy_:
                        hook[TestFramework.bstack1l11lllll1l_opy_] = bstack1l11ll1l11l_opy_
                hook[TestFramework.bstack1l11l1llll1_opy_] = datetime.now(tz=timezone.utc)
                bstack1l11ll11lll_opy_[key].append(hook)
                bstack1l11ll1l1ll_opy_[bstack1llllllll1l_opy_.bstack1l1l11l11ll_opy_] = key
        TestFramework.bstack1l11lll1l1l_opy_(instance, bstack1l11ll1l1ll_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡮࡯ࡰ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁ࡫ࡦࡻࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤ࠾ࡽ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡁࠧᏙ") + str(bstack1l11ll11lll_opy_) + bstack1l1l111_opy_ (u"ࠢࠣᏚ"))
    def __1l11lll1lll_opy_(
        self,
        context: bstack1l11l1lllll_opy_,
        test_framework_state: bstack111111l111_opy_,
        test_hook_state: bstack1lllll11111_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111l1l1l_opy_(args[0], [bstack1l1l111_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᏛ"), bstack1l1l111_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥᏜ"), bstack1l1l111_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᏝ"), bstack1l1l111_opy_ (u"ࠦ࡮ࡪࡳࠣᏞ"), bstack1l1l111_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢᏟ"), bstack1l1l111_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨᏠ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1l1l111_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᏡ")) else fixturedef.get(bstack1l1l111_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᏢ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1l111_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢᏣ")) else None
        node = request.node if hasattr(request, bstack1l1l111_opy_ (u"ࠥࡲࡴࡪࡥࠣᏤ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1l111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᏥ")) else None
        baseid = fixturedef.get(bstack1l1l111_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧᏦ"), None) or bstack1l1l111_opy_ (u"ࠨࠢᏧ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1l111_opy_ (u"ࠢࡠࡲࡼࡪࡺࡴࡣࡪࡶࡨࡱࠧᏨ")):
            target = bstack1llllllll1l_opy_.__1l1l11lll1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1l111_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥᏩ")) else None
            if target and not TestFramework.bstack11111l1lll_opy_(target):
                self.__1l1l111l111_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡳࡵࡤࡦ࠿ࡾࡲࡴࡪࡥࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᏪ") + str(test_hook_state) + bstack1l1l111_opy_ (u"ࠥࠦᏫ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤᏬ") + str(target) + bstack1l1l111_opy_ (u"ࠧࠨᏭ"))
            return None
        instance = TestFramework.bstack11111l1lll_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡨࡡࡴࡧ࡬ࡨࡂࢁࡢࡢࡵࡨ࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣᏮ") + str(target) + bstack1l1l111_opy_ (u"ࠢࠣᏯ"))
            return None
        bstack1l1l11l1111_opy_ = TestFramework.bstack1111l111l1_opy_(instance, bstack1llllllll1l_opy_.bstack1l11l1lll11_opy_, {})
        if os.getenv(bstack1l1l111_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡇࡋ࡛ࡘ࡚ࡘࡅࡔࠤᏰ"), bstack1l1l111_opy_ (u"ࠤ࠴ࠦᏱ")) == bstack1l1l111_opy_ (u"ࠥ࠵ࠧᏲ"):
            bstack1l1l11l1l1l_opy_ = bstack1l1l111_opy_ (u"ࠦ࠿ࠨᏳ").join((scope, fixturename))
            bstack1l11lll11ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1l11l1ll1l1_opy_ = {
                bstack1l1l111_opy_ (u"ࠧࡱࡥࡺࠤᏴ"): bstack1l1l11l1l1l_opy_,
                bstack1l1l111_opy_ (u"ࠨࡴࡢࡩࡶࠦᏵ"): bstack1llllllll1l_opy_.__1l11l1ll111_opy_(request.node),
                bstack1l1l111_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࠣ᏶"): fixturedef,
                bstack1l1l111_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢ᏷"): scope,
                bstack1l1l111_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᏸ"): None,
            }
            try:
                if test_hook_state == bstack1lllll11111_opy_.POST and callable(getattr(args[-1], bstack1l1l111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᏹ"), None)):
                    bstack1l11l1ll1l1_opy_[bstack1l1l111_opy_ (u"ࠦࡹࡿࡰࡦࠤᏺ")] = TestFramework.bstack1ll111ll1ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lllll11111_opy_.PRE:
                bstack1l11l1ll1l1_opy_[bstack1l1l111_opy_ (u"ࠧࡻࡵࡪࡦࠥᏻ")] = uuid4().__str__()
                bstack1l11l1ll1l1_opy_[bstack1llllllll1l_opy_.bstack1l11ll1l1l1_opy_] = bstack1l11lll11ll_opy_
            elif test_hook_state == bstack1lllll11111_opy_.POST:
                bstack1l11l1ll1l1_opy_[bstack1llllllll1l_opy_.bstack1l11l1llll1_opy_] = bstack1l11lll11ll_opy_
            if bstack1l1l11l1l1l_opy_ in bstack1l1l11l1111_opy_:
                bstack1l1l11l1111_opy_[bstack1l1l11l1l1l_opy_].update(bstack1l11l1ll1l1_opy_)
                self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࠢᏼ") + str(bstack1l1l11l1111_opy_[bstack1l1l11l1l1l_opy_]) + bstack1l1l111_opy_ (u"ࠢࠣᏽ"))
            else:
                bstack1l1l11l1111_opy_[bstack1l1l11l1l1l_opy_] = bstack1l11l1ll1l1_opy_
                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࢃࠠࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࠦ᏾") + str(len(bstack1l1l11l1111_opy_)) + bstack1l1l111_opy_ (u"ࠤࠥ᏿"))
        TestFramework.bstack1111lllll1_opy_(instance, bstack1llllllll1l_opy_.bstack1l11l1lll11_opy_, bstack1l1l11l1111_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࢀࡲࡥ࡯ࠪࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷ࠮ࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥ᐀") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠦࠧᐁ"))
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
            bstack1llllllll1l_opy_.bstack1l11l1lll11_opy_: {},
            bstack1llllllll1l_opy_.bstack1l11l1ll1ll_opy_: {},
            bstack1llllllll1l_opy_.bstack1l1l11111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111lllll1_opy_(ob, TestFramework.bstack1l11l1lll1l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111lllll1_opy_(ob, TestFramework.bstack1ll1llll111_opy_, context.platform_index)
        TestFramework.bstack1111lll11l_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡣࡵࡺ࠱࡭ࡩࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᐂ") + str(TestFramework.bstack1111lll11l_opy_.keys()) + bstack1l1l111_opy_ (u"ࠨࠢᐃ"))
        return ob
    def bstack1ll11lll11l_opy_(self, instance: bstack1111111l1l_opy_, bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_]):
        bstack1l11ll111l1_opy_ = (
            bstack1llllllll1l_opy_.bstack1l11ll1llll_opy_
            if bstack11111l1l1l_opy_[1] == bstack1lllll11111_opy_.PRE
            else bstack1llllllll1l_opy_.bstack1l1l11l11ll_opy_
        )
        hook = bstack1llllllll1l_opy_.bstack1l11ll11ll1_opy_(instance, bstack1l11ll111l1_opy_)
        entries = hook.get(TestFramework.bstack1l1l111l1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1l11ll1ll1l_opy_, []))
        return entries
    def bstack1ll111ll1l1_opy_(self, instance: bstack1111111l1l_opy_, bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_]):
        bstack1l11ll111l1_opy_ = (
            bstack1llllllll1l_opy_.bstack1l11ll1llll_opy_
            if bstack11111l1l1l_opy_[1] == bstack1lllll11111_opy_.PRE
            else bstack1llllllll1l_opy_.bstack1l1l11l11ll_opy_
        )
        bstack1llllllll1l_opy_.bstack1l1l111ll11_opy_(instance, bstack1l11ll111l1_opy_)
        TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1l11ll1ll1l_opy_, []).clear()
    @staticmethod
    def bstack1l11ll11ll1_opy_(instance: bstack1111111l1l_opy_, bstack1l11ll111l1_opy_: str):
        bstack1l11lll1ll1_opy_ = (
            bstack1llllllll1l_opy_.bstack1l11l1ll1ll_opy_
            if bstack1l11ll111l1_opy_ == bstack1llllllll1l_opy_.bstack1l1l11l11ll_opy_
            else bstack1llllllll1l_opy_.bstack1l1l11111ll_opy_
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
        hook = bstack1llllllll1l_opy_.bstack1l11ll11ll1_opy_(instance, bstack1l11ll111l1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1l111l1ll_opy_, []).clear()
    @staticmethod
    def __1l1l11l11l1_opy_(instance: bstack1111111l1l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1l111_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡣࡰࡴࡧࡷࠧᐄ"), None)):
            return
        if os.getenv(bstack1l1l111_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡍࡑࡊࡗࠧᐅ"), bstack1l1l111_opy_ (u"ࠤ࠴ࠦᐆ")) != bstack1l1l111_opy_ (u"ࠥ࠵ࠧᐇ"):
            bstack1llllllll1l_opy_.logger.warning(bstack1l1l111_opy_ (u"ࠦ࡮࡭࡮ࡰࡴ࡬ࡲ࡬ࠦࡣࡢࡲ࡯ࡳ࡬ࠨᐈ"))
            return
        bstack1l11ll11l1l_opy_ = {
            bstack1l1l111_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᐉ"): (bstack1llllllll1l_opy_.bstack1l11ll1llll_opy_, bstack1llllllll1l_opy_.bstack1l1l11111ll_opy_),
            bstack1l1l111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᐊ"): (bstack1llllllll1l_opy_.bstack1l1l11l11ll_opy_, bstack1llllllll1l_opy_.bstack1l11l1ll1ll_opy_),
        }
        for when in (bstack1l1l111_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᐋ"), bstack1l1l111_opy_ (u"ࠣࡥࡤࡰࡱࠨᐌ"), bstack1l1l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᐍ")):
            bstack1l1l111llll_opy_ = args[1].get_records(when)
            if not bstack1l1l111llll_opy_:
                continue
            records = [
                bstack1lllll111ll_opy_(
                    kind=TestFramework.bstack1ll1111ll11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1l111_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࡰࡤࡱࡪࠨᐎ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1l111_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࠧᐏ")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1l111llll_opy_
                if isinstance(getattr(r, bstack1l1l111_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨᐐ"), None), str) and r.message.strip()
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
    def __1l1l111ll1l_opy_(test) -> Dict[str, Any]:
        bstack111111111_opy_ = bstack1llllllll1l_opy_.__1l1l11lll1l_opy_(test.location) if hasattr(test, bstack1l1l111_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᐑ")) else getattr(test, bstack1l1l111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᐒ"), None)
        test_name = test.name if hasattr(test, bstack1l1l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᐓ")) else None
        bstack1l11l1ll11l_opy_ = test.fspath.strpath if hasattr(test, bstack1l1l111_opy_ (u"ࠤࡩࡷࡵࡧࡴࡩࠤᐔ")) and test.fspath else None
        if not bstack111111111_opy_ or not test_name or not bstack1l11l1ll11l_opy_:
            return None
        code = None
        if hasattr(test, bstack1l1l111_opy_ (u"ࠥࡳࡧࡰࠢᐕ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack1l11l1l1l1l_opy_ = []
        try:
            bstack1l11l1l1l1l_opy_ = bstack1l1lll1lll_opy_.bstack11l111111l_opy_(test)
        except:
            bstack1llllllll1l_opy_.logger.warning(bstack1l1l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡥࡴࡶࠣࡷࡨࡵࡰࡦࡵ࠯ࠤࡹ࡫ࡳࡵࠢࡶࡧࡴࡶࡥࡴࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡶࡪࡹ࡯࡭ࡸࡨࡨࠥ࡯࡮ࠡࡅࡏࡍࠧᐖ"))
        return {
            TestFramework.bstack1ll1ll1ll11_opy_: uuid4().__str__(),
            TestFramework.bstack1l1l111l1l1_opy_: bstack111111111_opy_,
            TestFramework.bstack1ll1l1l1ll1_opy_: test_name,
            TestFramework.bstack1l1llll1l1l_opy_: getattr(test, bstack1l1l111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᐗ"), None),
            TestFramework.bstack1l1l111lll1_opy_: bstack1l11l1ll11l_opy_,
            TestFramework.bstack1l11ll11111_opy_: bstack1llllllll1l_opy_.__1l11l1ll111_opy_(test),
            TestFramework.bstack1l11ll1lll1_opy_: code,
            TestFramework.bstack1l1ll11llll_opy_: TestFramework.bstack1l1l1111l1l_opy_,
            TestFramework.bstack1l1l1ll111l_opy_: bstack111111111_opy_,
            TestFramework.bstack1l11l1l1ll1_opy_: bstack1l11l1l1l1l_opy_
        }
    @staticmethod
    def __1l11l1ll111_opy_(test) -> List[str]:
        return (
            [getattr(f, bstack1l1l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐘ"), None) for f in test.own_markers if getattr(f, bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᐙ"), None)]
            if isinstance(getattr(test, bstack1l1l111_opy_ (u"ࠣࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸࠨᐚ"), None), list)
            else []
        )
    @staticmethod
    def __1l1l11lll1l_opy_(location):
        return bstack1l1l111_opy_ (u"ࠤ࠽࠾ࠧᐛ").join(filter(lambda x: isinstance(x, str), location))