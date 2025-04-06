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
from datetime import datetime, timezone
import os
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import bstack1111ll11ll_opy_, bstack11111l11l1_opy_, bstack1111llll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1llll111lll_opy_ import bstack1lll1lll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111l111_opy_, bstack1111111l1l_opy_, bstack1lllll11111_opy_, bstack1lllll111ll_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1ll111111l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1ll11lll111_opy_ = [bstack1l1l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᅰ"), bstack1l1l111_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᅱ"), bstack1l1l111_opy_ (u"ࠢࡤࡱࡱࡪ࡮࡭ࠢᅲ"), bstack1l1l111_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࠤᅳ"), bstack1l1l111_opy_ (u"ࠤࡳࡥࡹ࡮ࠢᅴ")]
bstack1ll11l11111_opy_ = {
    bstack1l1l111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡍࡹ࡫࡭ࠣᅵ"): bstack1ll11lll111_opy_,
    bstack1l1l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡕࡧࡣ࡬ࡣࡪࡩࠧᅶ"): bstack1ll11lll111_opy_,
    bstack1l1l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡓ࡯ࡥࡷ࡯ࡩࠧᅷ"): bstack1ll11lll111_opy_,
    bstack1l1l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡃ࡭ࡣࡶࡷࠧᅸ"): bstack1ll11lll111_opy_,
    bstack1l1l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡇࡷࡱࡧࡹ࡯࡯࡯ࠤᅹ"): bstack1ll11lll111_opy_
    + [
        bstack1l1l111_opy_ (u"ࠣࡱࡵ࡭࡬࡯࡮ࡢ࡮ࡱࡥࡲ࡫ࠢᅺ"),
        bstack1l1l111_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦᅻ"),
        bstack1l1l111_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨ࡭ࡳ࡬࡯ࠣᅼ"),
        bstack1l1l111_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᅽ"),
        bstack1l1l111_opy_ (u"ࠧࡩࡡ࡭࡮ࡶࡴࡪࡩࠢᅾ"),
        bstack1l1l111_opy_ (u"ࠨࡣࡢ࡮࡯ࡳࡧࡰࠢᅿ"),
        bstack1l1l111_opy_ (u"ࠢࡴࡶࡤࡶࡹࠨᆀ"),
        bstack1l1l111_opy_ (u"ࠣࡵࡷࡳࡵࠨᆁ"),
        bstack1l1l111_opy_ (u"ࠤࡧࡹࡷࡧࡴࡪࡱࡱࠦᆂ"),
        bstack1l1l111_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᆃ"),
    ],
    bstack1l1l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡩ࡯࠰ࡖࡩࡸࡹࡩࡰࡰࠥᆄ"): [bstack1l1l111_opy_ (u"ࠧࡹࡴࡢࡴࡷࡴࡦࡺࡨࠣᆅ"), bstack1l1l111_opy_ (u"ࠨࡴࡦࡵࡷࡷ࡫ࡧࡩ࡭ࡧࡧࠦᆆ"), bstack1l1l111_opy_ (u"ࠢࡵࡧࡶࡸࡸࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣᆇ"), bstack1l1l111_opy_ (u"ࠣ࡫ࡷࡩࡲࡹࠢᆈ")],
    bstack1l1l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡦࡳࡳ࡬ࡩࡨ࠰ࡆࡳࡳ࡬ࡩࡨࠤᆉ"): [bstack1l1l111_opy_ (u"ࠥ࡭ࡳࡼ࡯ࡤࡣࡷ࡭ࡴࡴ࡟ࡱࡣࡵࡥࡲࡹࠢᆊ"), bstack1l1l111_opy_ (u"ࠦࡦࡸࡧࡴࠤᆋ")],
    bstack1l1l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡇ࡫ࡻࡸࡺࡸࡥࡅࡧࡩࠦᆌ"): [bstack1l1l111_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᆍ"), bstack1l1l111_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᆎ"), bstack1l1l111_opy_ (u"ࠣࡨࡸࡲࡨࠨᆏ"), bstack1l1l111_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᆐ"), bstack1l1l111_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᆑ"), bstack1l1l111_opy_ (u"ࠦ࡮ࡪࡳࠣᆒ")],
    bstack1l1l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡔࡷࡥࡖࡪࡷࡵࡦࡵࡷࠦᆓ"): [bstack1l1l111_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᆔ"), bstack1l1l111_opy_ (u"ࠢࡱࡣࡵࡥࡲࠨᆕ"), bstack1l1l111_opy_ (u"ࠣࡲࡤࡶࡦࡳ࡟ࡪࡰࡧࡩࡽࠨᆖ")],
    bstack1l1l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡵࡹࡳࡴࡥࡳ࠰ࡆࡥࡱࡲࡉ࡯ࡨࡲࠦᆗ"): [bstack1l1l111_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᆘ"), bstack1l1l111_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࠦᆙ")],
    bstack1l1l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡏࡱࡧࡩࡐ࡫ࡹࡸࡱࡵࡨࡸࠨᆚ"): [bstack1l1l111_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᆛ"), bstack1l1l111_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᆜ")],
    bstack1l1l111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡑࡦࡸ࡫ࠣᆝ"): [bstack1l1l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆞ"), bstack1l1l111_opy_ (u"ࠥࡥࡷ࡭ࡳࠣᆟ"), bstack1l1l111_opy_ (u"ࠦࡰࡽࡡࡳࡩࡶࠦᆠ")],
}
class bstack1lll1l11111_opy_(bstack1lllll1l111_opy_):
    bstack1ll11l11ll1_opy_ = bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡪ࡬ࡥࡳࡴࡨࡨࠧᆡ")
    bstack1ll11lll1l1_opy_ = bstack1l1l111_opy_ (u"ࠨࡉࡏࡈࡒࠦᆢ")
    bstack1ll11ll1111_opy_ = bstack1l1l111_opy_ (u"ࠢࡆࡔࡕࡓࡗࠨᆣ")
    bstack1ll11l11l11_opy_: Callable
    bstack1ll11l1l1ll_opy_: Callable
    def __init__(self, bstack1lllll1lll1_opy_, bstack111111lll1_opy_):
        super().__init__()
        self.bstack1ll1l1l1l1l_opy_ = bstack111111lll1_opy_
        if os.getenv(bstack1l1l111_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡐ࠳࠴࡝ࠧᆤ"), bstack1l1l111_opy_ (u"ࠤ࠴ࠦᆥ")) != bstack1l1l111_opy_ (u"ࠥ࠵ࠧᆦ") or not self.is_enabled():
            self.logger.warning(bstack1l1l111_opy_ (u"ࠦࠧᆧ") + str(self.__class__.__name__) + bstack1l1l111_opy_ (u"ࠧࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠣᆨ"))
            return
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), self.bstack1ll1l1ll111_opy_)
        for event in bstack111111l111_opy_:
            for state in bstack1lllll11111_opy_:
                TestFramework.bstack1ll1ll1ll1l_opy_((event, state), self.bstack1ll111111ll_opy_)
        bstack1lllll1lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.POST), self.bstack1ll11ll11ll_opy_)
        self.bstack1ll11l11l11_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1ll111l111l_opy_(bstack1lll1l11111_opy_.bstack1ll11lll1l1_opy_, self.bstack1ll11l11l11_opy_)
        self.bstack1ll11l1l1ll_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1ll111l111l_opy_(bstack1lll1l11111_opy_.bstack1ll11ll1111_opy_, self.bstack1ll11l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll111111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll111l1lll_opy_() and instance:
            bstack1ll11l1l1l1_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack11111l1l1l_opy_
            if test_framework_state == bstack111111l111_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack111111l111_opy_.LOG:
                bstack1111ll11_opy_ = datetime.now()
                entries = f.bstack1ll11lll11l_opy_(instance, bstack11111l1l1l_opy_)
                if entries:
                    self.bstack1ll11l111l1_opy_(instance, entries)
                    instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࠨᆩ"), datetime.now() - bstack1111ll11_opy_)
                    f.bstack1ll111ll1l1_opy_(instance, bstack11111l1l1l_opy_)
                instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᆪ"), datetime.now() - bstack1ll11l1l1l1_opy_)
                return # bstack1ll11ll1lll_opy_ not send this event with the bstack1ll11l1lll1_opy_ bstack1ll11ll1ll1_opy_
            elif (
                test_framework_state == bstack111111l111_opy_.TEST
                and test_hook_state == bstack1lllll11111_opy_.POST
                and not f.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll111lll11_opy_)
            ):
                self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡦࡵࡳࡵࡶࡩ࡯ࡩࠣࡨࡺ࡫ࠠࡵࡱࠣࡰࡦࡩ࡫ࠡࡱࡩࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࠨᆫ") + str(TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll111lll11_opy_)) + bstack1l1l111_opy_ (u"ࠤࠥᆬ"))
                f.bstack1111lllll1_opy_(instance, bstack1lll1l11111_opy_.bstack1ll11l11ll1_opy_, True)
                return # bstack1ll11ll1lll_opy_ not send this event bstack1ll11ll1l11_opy_ bstack1ll111lll1l_opy_
            elif (
                f.bstack1111l111l1_opy_(instance, bstack1lll1l11111_opy_.bstack1ll11l11ll1_opy_, False)
                and test_framework_state == bstack111111l111_opy_.LOG_REPORT
                and test_hook_state == bstack1lllll11111_opy_.POST
                and f.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll111lll11_opy_)
            ):
                self.logger.warning(bstack1l1l111_opy_ (u"ࠥ࡭ࡳࡰࡥࡤࡶ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲࡙ࡋࡓࡕ࠮ࠣࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡔࡔ࡙ࡔࠡࠤᆭ") + str(TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll111lll11_opy_)) + bstack1l1l111_opy_ (u"ࠦࠧᆮ"))
                self.bstack1ll111111ll_opy_(f, instance, (bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), *args, **kwargs)
            bstack1111ll11_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1ll1111l1l1_opy_ = sorted(
                filter(lambda x: x.get(bstack1l1l111_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᆯ"), None), data.pop(bstack1l1l111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᆰ"), {}).values()),
                key=lambda x: x[bstack1l1l111_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᆱ")],
            )
            if bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_ in data:
                data.pop(bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_)
            data.update({bstack1l1l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᆲ"): bstack1ll1111l1l1_opy_})
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᆳ"), datetime.now() - bstack1111ll11_opy_)
            bstack1111ll11_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1ll11l1111l_opy_)
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠥ࡮ࡸࡵ࡮࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᆴ"), datetime.now() - bstack1111ll11_opy_)
            self.bstack1ll11ll1ll1_opy_(instance, bstack11111l1l1l_opy_, event_json=event_json)
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᆵ"), datetime.now() - bstack1ll11l1l1l1_opy_)
    def bstack1ll1lll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
        bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1l11lllll1_opy_.value)
        self.bstack1ll1l1l1l1l_opy_.bstack1ll111ll11l_opy_(instance, f, bstack11111l1l1l_opy_, *args, **kwargs)
        bstack1llll11ll11_opy_.end(EVENTS.bstack1l11lllll1_opy_.value, bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᆶ"), bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᆷ"), status=True, failure=None, test_name=None)
    def bstack1ll1l1ll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1ll1l1l1l1l_opy_.bstack1ll1111l11l_opy_(instance, f, bstack11111l1l1l_opy_, *args, **kwargs)
        self.bstack1ll111l11ll_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1ll11ll11l1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1ll111l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡗࡩࡸࡺࡓࡦࡵࡶ࡭ࡴࡴࡅࡷࡧࡱࡸࠥ࡭ࡒࡑࡅࠣࡧࡦࡲ࡬࠻ࠢࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠥᆸ"))
            return
        bstack1111ll11_opy_ = datetime.now()
        try:
            r = self.bstack1llllll1lll_opy_.TestSessionEvent(req)
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡩࡻ࡫࡮ࡵࠤᆹ"), datetime.now() - bstack1111ll11_opy_)
            f.bstack1111lllll1_opy_(instance, self.bstack1ll1l1l1l1l_opy_.bstack1ll1111llll_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l1l111_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᆺ") + str(r) + bstack1l1l111_opy_ (u"ࠥࠦᆻ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᆼ") + str(e) + bstack1l1l111_opy_ (u"ࠧࠨᆽ"))
            traceback.print_exc()
            raise e
    def bstack1ll11ll11ll_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        _driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        _1ll111llll1_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lll1l11lll_opy_.bstack1ll1ll111ll_opy_(method_name):
            return
        if f.bstack1ll1ll1l1ll_opy_(*args) != bstack1lll1l11lll_opy_.bstack1ll111lllll_opy_:
            return
        bstack1ll11l1l1l1_opy_ = datetime.now()
        screenshot = result.get(bstack1l1l111_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᆾ"), None) if isinstance(result, dict) else None
        if not isinstance(screenshot, str) or len(screenshot) <= 0:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠥ࡯࡭ࡢࡩࡨࠤࡧࡧࡳࡦ࠸࠷ࠤࡸࡺࡲࠣᆿ"))
            return
        bstack1ll11l11lll_opy_ = self.bstack1ll11111ll1_opy_(instance)
        if bstack1ll11l11lll_opy_:
            entry = bstack1lllll111ll_opy_(TestFramework.bstack1ll11l1ll11_opy_, screenshot)
            self.bstack1ll11l111l1_opy_(bstack1ll11l11lll_opy_, [entry])
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡧࡻࡩࡨࡻࡴࡦࠤᇀ"), datetime.now() - bstack1ll11l1l1l1_opy_)
        else:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠤࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶࡨࡷࡹࠦࡦࡰࡴࠣࡻ࡭࡯ࡣࡩࠢࡷ࡬࡮ࡹࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤࡼࡧࡳࠡࡶࡤ࡯ࡪࡴࠠࡣࡻࠣࡨࡷ࡯ࡶࡦࡴࡀࠦᇁ") + str(instance.ref()) + bstack1l1l111_opy_ (u"ࠥࠦᇂ"))
    @measure(event_name=EVENTS.bstack1ll1111ll1l_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1ll11l111l1_opy_(
        self,
        bstack1ll11l11lll_opy_: bstack1111111l1l_opy_,
        entries: List[bstack1lllll111ll_opy_],
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1111l111l1_opy_(bstack1ll11l11lll_opy_, TestFramework.bstack1ll1llll111_opy_)
        req.execution_context.hash = str(bstack1ll11l11lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l11lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l11lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack1111l111l1_opy_(bstack1ll11l11lll_opy_, TestFramework.bstack1ll1lllll1l_opy_)
            log_entry.test_framework_version = TestFramework.bstack1111l111l1_opy_(bstack1ll11l11lll_opy_, TestFramework.bstack1ll11l1l11l_opy_)
            log_entry.uuid = TestFramework.bstack1111l111l1_opy_(bstack1ll11l11lll_opy_, TestFramework.bstack1ll1ll1ll11_opy_)
            log_entry.test_framework_state = bstack1ll11l11lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1l111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇃ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
        def bstack1ll111l11l1_opy_():
            bstack1111ll11_opy_ = datetime.now()
            try:
                self.bstack1llllll1lll_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1ll11l1ll11_opy_:
                    bstack1ll11l11lll_opy_.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᇄ"), datetime.now() - bstack1111ll11_opy_)
                else:
                    bstack1ll11l11lll_opy_.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥ࡬ࡰࡩࠥᇅ"), datetime.now() - bstack1111ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1l111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᇆ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1111llllll_opy_.enqueue(bstack1ll111l11l1_opy_)
    @measure(event_name=EVENTS.bstack1ll11ll111l_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1ll11ll1ll1_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        event_json=None,
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1llll111_opy_)
        req.test_framework_name = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1lllll1l_opy_)
        req.test_framework_version = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll11l1l11l_opy_)
        req.test_framework_state = bstack11111l1l1l_opy_[0].name
        req.test_hook_state = bstack11111l1l1l_opy_[1].name
        started_at = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll111ll111_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll11l111ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1ll11l1111l_opy_)).encode(bstack1l1l111_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇇ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll111l11l1_opy_():
            bstack1111ll11_opy_ = datetime.now()
            try:
                self.bstack1llllll1lll_opy_.TestFrameworkEvent(req)
                instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡥࡷࡧࡱࡸࠧᇈ"), datetime.now() - bstack1111ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1l111_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᇉ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1111llllll_opy_.enqueue(bstack1ll111l11l1_opy_)
    def bstack1ll111l1111_opy_(self, event_url: str, bstack111ll1l1ll_opy_: dict) -> bool:
        return True # always return True so that old bstack1ll11111l1l_opy_ bstack1ll11l11l1l_opy_'t bstack1ll111l1l11_opy_
    def bstack1ll11111ll1_opy_(self, instance: bstack1111ll11ll_opy_):
        bstack1ll11l1ll1l_opy_ = TestFramework.bstack1111l1ll1l_opy_(instance.context)
        for t in bstack1ll11l1ll1l_opy_:
            bstack1ll11ll1l1l_opy_ = TestFramework.bstack1111l111l1_opy_(t, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
            if any(instance is d[1] for d in bstack1ll11ll1l1l_opy_):
                return t
    def bstack1ll11l1l111_opy_(self, message):
        self.bstack1ll11l11l11_opy_(message + bstack1l1l111_opy_ (u"ࠦࡡࡴࠢᇊ"))
    def log_error(self, message):
        self.bstack1ll11l1l1ll_opy_(message + bstack1l1l111_opy_ (u"ࠧࡢ࡮ࠣᇋ"))
    def bstack1ll111l111l_opy_(self, level, original_func):
        def bstack1ll11111l11_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            bstack1ll11l1ll1l_opy_ = TestFramework.bstack1ll11l1llll_opy_()
            if not bstack1ll11l1ll1l_opy_:
                return return_value
            bstack1ll11l11lll_opy_ = next(
                (
                    instance
                    for instance in bstack1ll11l1ll1l_opy_
                    if TestFramework.bstack1111l1lll1_opy_(instance, TestFramework.bstack1ll1ll1ll11_opy_)
                ),
                None,
            )
            if not bstack1ll11l11lll_opy_:
                return
            entry = bstack1lllll111ll_opy_(TestFramework.bstack1ll1111ll11_opy_, message, level)
            self.bstack1ll11l111l1_opy_(bstack1ll11l11lll_opy_, [entry])
            return return_value
        return bstack1ll11111l11_opy_
class bstack1ll11l1111l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1ll1111lll1_opy_ = set()
        kwargs[bstack1l1l111_opy_ (u"ࠨࡳ࡬࡫ࡳ࡯ࡪࡿࡳࠣᇌ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1ll1111l111_opy_(obj, self.bstack1ll1111lll1_opy_)
def bstack1ll11111lll_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1ll1111l111_opy_(obj, bstack1ll1111lll1_opy_=None, max_depth=3):
    if bstack1ll1111lll1_opy_ is None:
        bstack1ll1111lll1_opy_ = set()
    if id(obj) in bstack1ll1111lll1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1ll1111lll1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1ll111l1ll1_opy_ = TestFramework.bstack1ll111ll1ll_opy_(obj)
    bstack1ll1111l1ll_opy_ = next((k.lower() in bstack1ll111l1ll1_opy_.lower() for k in bstack1ll11l11111_opy_.keys()), None)
    if bstack1ll1111l1ll_opy_:
        obj = TestFramework.bstack1ll111l1l1l_opy_(obj, bstack1ll11l11111_opy_[bstack1ll1111l1ll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l1l111_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥᇍ")):
            keys = getattr(obj, bstack1l1l111_opy_ (u"ࠣࡡࡢࡷࡱࡵࡴࡴࡡࡢࠦᇎ"), [])
        elif hasattr(obj, bstack1l1l111_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦᇏ")):
            keys = getattr(obj, bstack1l1l111_opy_ (u"ࠥࡣࡤࡪࡩࡤࡶࡢࡣࠧᇐ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l1l111_opy_ (u"ࠦࡤࠨᇑ"))}
        if not obj and bstack1ll111l1ll1_opy_ == bstack1l1l111_opy_ (u"ࠧࡶࡡࡵࡪ࡯࡭ࡧ࠴ࡐࡰࡵ࡬ࡼࡕࡧࡴࡩࠤᇒ"):
            obj = {bstack1l1l111_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᇓ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1ll11111lll_opy_(key) or str(key).startswith(bstack1l1l111_opy_ (u"ࠢࡠࠤᇔ")):
            continue
        if value is not None and bstack1ll11111lll_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1ll1111l111_opy_(value, bstack1ll1111lll1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1ll1111l111_opy_(o, bstack1ll1111lll1_opy_, max_depth) for o in value]))
    return result or None