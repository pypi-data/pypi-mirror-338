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
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack11111l1111_opy_,
    bstack1111ll11ll_opy_,
    bstack11111l11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111l111_opy_, bstack1lllll11111_opy_, bstack1111111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1111ll_opy_ import bstack1ll1l111l11_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1ll111111l1_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll1lll1ll_opy_(bstack1ll1l111l11_opy_):
    bstack1l1ll1ll111_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣኯ")
    bstack1ll1111111l_opy_ = bstack1l1l111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤኰ")
    bstack1l1ll1l111l_opy_ = bstack1l1l111_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨ኱")
    bstack1l1ll1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧኲ")
    bstack1l1ll1l1lll_opy_ = bstack1l1l111_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥኳ")
    bstack1ll1111llll_opy_ = bstack1l1l111_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨኴ")
    bstack1l1lll11111_opy_ = bstack1l1l111_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦኵ")
    bstack1l1ll1l11ll_opy_ = bstack1l1l111_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢ኶")
    def __init__(self):
        super().__init__(bstack1ll11lll1ll_opy_=self.bstack1l1ll1ll111_opy_, frameworks=[bstack1lll1l11lll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.BEFORE_EACH, bstack1lllll11111_opy_.POST), self.bstack1l1l1ll11l1_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), self.bstack1ll1l1ll111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1l1ll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        bstack1ll11ll1l1l_opy_ = self.bstack1l1l1l1ll1l_opy_(instance.context)
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨ኷") + str(bstack11111l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠦࠧኸ"))
        f.bstack1111lllll1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, bstack1ll11ll1l1l_opy_)
        bstack1l1l1l1llll_opy_ = self.bstack1l1l1l1ll1l_opy_(instance.context, bstack1l1l1l1l1l1_opy_=False)
        f.bstack1111lllll1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1ll1l111l_opy_, bstack1l1l1l1llll_opy_)
    def bstack1ll1lll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1ll11l1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        if not f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1lll11111_opy_, False):
            self.__1l1l1l1ll11_opy_(f,instance,bstack11111l1l1l_opy_)
    def bstack1ll1l1ll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1ll11l1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        if not f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1lll11111_opy_, False):
            self.__1l1l1l1ll11_opy_(f, instance, bstack11111l1l1l_opy_)
        if not f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1ll1l11ll_opy_, False):
            self.__1l1l1l1l1ll_opy_(f, instance, bstack11111l1l1l_opy_)
    def bstack1l1l1l1lll1_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1ll1l1l1l11_opy_(instance):
            return
        if f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1ll1l11ll_opy_, False):
            return
        driver.execute_script(
            bstack1l1l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥኹ").format(
                json.dumps(
                    {
                        bstack1l1l111_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨኺ"): bstack1l1l111_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥኻ"),
                        bstack1l1l111_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦኼ"): {bstack1l1l111_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤኽ"): result},
                    }
                )
            )
        )
        f.bstack1111lllll1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1ll1l11ll_opy_, True)
    def bstack1l1l1l1ll1l_opy_(self, context: bstack11111l11ll_opy_, bstack1l1l1l1l1l1_opy_= True):
        if bstack1l1l1l1l1l1_opy_:
            bstack1ll11ll1l1l_opy_ = self.bstack1ll1l1111l1_opy_(context, reverse=True)
        else:
            bstack1ll11ll1l1l_opy_ = self.bstack1ll1l111ll1_opy_(context, reverse=True)
        return [f for f in bstack1ll11ll1l1l_opy_ if f[1].state != bstack11111l11l1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11ll111l11_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1l1l1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
    ):
        bstack1ll11ll1l1l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨኾ") + str(bstack11111l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠦࠧ኿"))
            return
        driver = bstack1ll11ll1l1l_opy_[0][0]()
        status = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1l1ll11llll_opy_, None)
        if not status:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢዀ") + str(bstack11111l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠨࠢ዁"))
            return
        bstack1l1ll1l11l1_opy_ = {bstack1l1l111_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢዂ"): status.lower()}
        bstack1l1ll1lllll_opy_ = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1l1ll1l1l11_opy_, None)
        if status.lower() == bstack1l1l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨዃ") and bstack1l1ll1lllll_opy_ is not None:
            bstack1l1ll1l11l1_opy_[bstack1l1l111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩዄ")] = bstack1l1ll1lllll_opy_[0][bstack1l1l111_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ዅ")][0] if isinstance(bstack1l1ll1lllll_opy_, list) else str(bstack1l1ll1lllll_opy_)
        driver.execute_script(
            bstack1l1l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤ዆").format(
                json.dumps(
                    {
                        bstack1l1l111_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧ዇"): bstack1l1l111_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤወ"),
                        bstack1l1l111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥዉ"): bstack1l1ll1l11l1_opy_,
                    }
                )
            )
        )
        f.bstack1111lllll1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1ll1l11ll_opy_, True)
    @measure(event_name=EVENTS.bstack1l11ll11l1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1l1l1l1ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_]
    ):
        test_name = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1l1l1ll111l_opy_, None)
        if not test_name:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢዊ"))
            return
        bstack1ll11ll1l1l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦዋ") + str(bstack11111l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠥࠦዌ"))
            return
        for bstack1l1llll1lll_opy_, bstack1l1l1l1l11l_opy_ in bstack1ll11ll1l1l_opy_:
            if not bstack1lll1l11lll_opy_.bstack1ll1l1l1l11_opy_(bstack1l1l1l1l11l_opy_):
                continue
            driver = bstack1l1llll1lll_opy_()
            if not driver:
                continue
            driver.execute_script(
                bstack1l1l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤው").format(
                    json.dumps(
                        {
                            bstack1l1l111_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧዎ"): bstack1l1l111_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢዏ"),
                            bstack1l1l111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥዐ"): {bstack1l1l111_opy_ (u"ࠣࡰࡤࡱࡪࠨዑ"): test_name},
                        }
                    )
                )
            )
        f.bstack1111lllll1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1lll11111_opy_, True)
    def bstack1ll111ll11l_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        f: TestFramework,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1ll11l1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        bstack1ll11ll1l1l_opy_ = [d for d, _ in f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])]
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤዒ"))
            return
        if not bstack1ll111111l1_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣዓ"))
            return
        for bstack1l1l1l1l111_opy_ in bstack1ll11ll1l1l_opy_:
            driver = bstack1l1l1l1l111_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1l1l111_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤዔ") + str(timestamp)
            driver.execute_script(
                bstack1l1l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥዕ").format(
                    json.dumps(
                        {
                            bstack1l1l111_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨዖ"): bstack1l1l111_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ዗"),
                            bstack1l1l111_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦዘ"): {
                                bstack1l1l111_opy_ (u"ࠤࡷࡽࡵ࡫ࠢዙ"): bstack1l1l111_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢዚ"),
                                bstack1l1l111_opy_ (u"ࠦࡩࡧࡴࡢࠤዛ"): data,
                                bstack1l1l111_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦዜ"): bstack1l1l111_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧዝ")
                            }
                        }
                    )
                )
            )
    def bstack1ll1111l11l_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        f: TestFramework,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1l1ll11l1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        bstack1ll11ll1l1l_opy_ = [d for _, d in f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])] + [d for _, d in f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1l1ll1l111l_opy_, [])]
        keys = [
            bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_,
            bstack1lll1lll1ll_opy_.bstack1l1ll1l111l_opy_,
        ]
        bstack1ll11ll1l1l_opy_ = [
            d for key in keys for _, d in f.bstack1111l111l1_opy_(instance, key, [])
        ]
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡲࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤዞ"))
            return
        if f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111llll_opy_, False):
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡆࡆ࡙ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡤࡴࡨࡥࡹ࡫ࡤࠣዟ"))
            return
        self.bstack1ll1llll1l1_opy_()
        bstack1111ll11_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1llll111_opy_)
        req.test_framework_name = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1lllll1l_opy_)
        req.test_framework_version = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll11l1l11l_opy_)
        req.test_framework_state = bstack11111l1l1l_opy_[0].name
        req.test_hook_state = bstack11111l1l1l_opy_[1].name
        req.test_uuid = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1ll1ll11_opy_)
        for driver in bstack1ll11ll1l1l_opy_:
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l1l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣዠ")
                if bstack1lll1l11lll_opy_.bstack1111l111l1_opy_(driver, bstack1lll1l11lll_opy_.bstack1l1l1ll1111_opy_, False)
                else bstack1l1l111_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤዡ")
            )
            session.ref = driver.ref()
            session.hub_url = bstack1lll1l11lll_opy_.bstack1111l111l1_opy_(driver, bstack1lll1l11lll_opy_.bstack1l1llll11l1_opy_, bstack1l1l111_opy_ (u"ࠦࠧዢ"))
            session.framework_name = driver.framework_name
            session.framework_version = driver.framework_version
            session.framework_session_id = bstack1lll1l11lll_opy_.bstack1111l111l1_opy_(driver, bstack1lll1l11lll_opy_.bstack1l1lll1lll1_opy_, bstack1l1l111_opy_ (u"ࠧࠨዣ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll1llllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs
    ):
        bstack1ll11ll1l1l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤዤ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠢࠣዥ"))
            return {}
        if len(bstack1ll11ll1l1l_opy_) > 1:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦዦ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠤࠥዧ"))
            return {}
        bstack1l1llll1lll_opy_, bstack1l1lllllll1_opy_ = bstack1ll11ll1l1l_opy_[0]
        driver = bstack1l1llll1lll_opy_()
        if not driver:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧየ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠦࠧዩ"))
            return {}
        capabilities = f.bstack1111l111l1_opy_(bstack1l1lllllll1_opy_, bstack1lll1l11lll_opy_.bstack1l1lll11l11_opy_)
        if not capabilities:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧዪ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠨࠢያ"))
            return {}
        return capabilities.get(bstack1l1l111_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧዬ"), {})
    def bstack1ll1l1ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs
    ):
        bstack1ll11ll1l1l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1lll1ll_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1ll11ll1l1l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦይ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠤࠥዮ"))
            return
        if len(bstack1ll11ll1l1l_opy_) > 1:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨዯ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠦࠧደ"))
        bstack1l1llll1lll_opy_, bstack1l1lllllll1_opy_ = bstack1ll11ll1l1l_opy_[0]
        driver = bstack1l1llll1lll_opy_()
        if not driver:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢዱ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠨࠢዲ"))
            return
        return driver