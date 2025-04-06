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
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack1111ll11ll_opy_,
    bstack11111l11ll_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1ll111111l1_opy_, bstack11l1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111l111_opy_, bstack1lllll11111_opy_, bstack1111111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1111ll_opy_ import bstack1ll1l111l11_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11l1lllll1_opy_ import bstack1ll1l1l1l1_opy_, bstack11ll111111_opy_, bstack11l1l1lll1_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1ll11l1_opy_(bstack1ll1l111l11_opy_):
    bstack1l1ll1ll111_opy_ = bstack1l1l111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡸࡩࡷࡧࡵࡷࠧላ")
    bstack1ll1111111l_opy_ = bstack1l1l111_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨሌ")
    bstack1l1ll1l111l_opy_ = bstack1l1l111_opy_ (u"ࠣࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥል")
    bstack1l1ll1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤሎ")
    bstack1l1ll1l1lll_opy_ = bstack1l1l111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡡࡵࡩ࡫ࡹࠢሏ")
    bstack1ll1111llll_opy_ = bstack1l1l111_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥሐ")
    bstack1l1lll11111_opy_ = bstack1l1l111_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣሑ")
    bstack1l1ll1l11ll_opy_ = bstack1l1l111_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡸࡺࡡࡵࡷࡶࠦሒ")
    def __init__(self):
        super().__init__(bstack1ll11lll1ll_opy_=self.bstack1l1ll1ll111_opy_, frameworks=[bstack1lll1l11lll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.BEFORE_EACH, bstack1lllll11111_opy_.POST), self.bstack1l1ll1lll1l_opy_)
        if bstack11l1l1111_opy_():
            TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), self.bstack1ll1lll1l1l_opy_)
        else:
            TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), self.bstack1ll1l1ll111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1ll1lll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1ll11l_opy_ = self.bstack1l1ll1llll1_opy_(instance.context)
        if not bstack1l1ll1ll11l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡵࡧࡧࡦ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧሓ") + str(bstack11111l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠣࠤሔ"))
            return
        f.bstack1111lllll1_opy_(instance, bstack1lll1ll11l1_opy_.bstack1ll1111111l_opy_, bstack1l1ll1ll11l_opy_)
    def bstack1l1ll1llll1_opy_(self, context: bstack11111l11ll_opy_, bstack1l1ll1l1l1l_opy_= True):
        if bstack1l1ll1l1l1l_opy_:
            bstack1l1ll1ll11l_opy_ = self.bstack1ll1l1111l1_opy_(context, reverse=True)
        else:
            bstack1l1ll1ll11l_opy_ = self.bstack1ll1l111ll1_opy_(context, reverse=True)
        return [f for f in bstack1l1ll1ll11l_opy_ if f[1].state != bstack11111l11l1_opy_.QUIT]
    def bstack1ll1lll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll1l_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        if not bstack1ll111111l1_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሕ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠥࠦሖ"))
            return
        bstack1l1ll1ll11l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1ll11l1_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1l1ll1ll11l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሗ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠧࠨመ"))
            return
        if len(bstack1l1ll1ll11l_opy_) > 1:
            self.logger.debug(
                bstack1llllll1111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣሙ"))
        bstack1l1ll1lll11_opy_, bstack1l1lllllll1_opy_ = bstack1l1ll1ll11l_opy_[0]
        page = bstack1l1ll1lll11_opy_()
        if not page:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሚ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠣࠤማ"))
            return
        bstack1ll1l1l11_opy_ = getattr(args[0], bstack1l1l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሜ"), None)
        try:
            page.evaluate(bstack1l1l111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦም"),
                        bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨሞ") + json.dumps(
                            bstack1ll1l1l11_opy_) + bstack1l1l111_opy_ (u"ࠧࢃࡽࠣሟ"))
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦሠ"), e)
    def bstack1ll1l1ll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll1l_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        if not bstack1ll111111l1_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥሡ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠣࠤሢ"))
            return
        bstack1l1ll1ll11l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1ll11l1_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1l1ll1ll11l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሣ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠥࠦሤ"))
            return
        if len(bstack1l1ll1ll11l_opy_) > 1:
            self.logger.debug(
                bstack1llllll1111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨሥ"))
        bstack1l1ll1lll11_opy_, bstack1l1lllllll1_opy_ = bstack1l1ll1ll11l_opy_[0]
        page = bstack1l1ll1lll11_opy_()
        if not page:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሦ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠨࠢሧ"))
            return
        status = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1l1ll11llll_opy_, None)
        if not status:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥረ") + str(bstack11111l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠣࠤሩ"))
            return
        bstack1l1ll1l11l1_opy_ = {bstack1l1l111_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤሪ"): status.lower()}
        bstack1l1ll1lllll_opy_ = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1l1ll1l1l11_opy_, None)
        if status.lower() == bstack1l1l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪራ") and bstack1l1ll1lllll_opy_ is not None:
            bstack1l1ll1l11l1_opy_[bstack1l1l111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫሬ")] = bstack1l1ll1lllll_opy_[0][bstack1l1l111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨር")][0] if isinstance(bstack1l1ll1lllll_opy_, list) else str(bstack1l1ll1lllll_opy_)
        try:
              page.evaluate(
                    bstack1l1l111_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢሮ"),
                    bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࠬሯ")
                    + json.dumps(bstack1l1ll1l11l1_opy_)
                    + bstack1l1l111_opy_ (u"ࠣࡿࠥሰ")
                )
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡻࡾࠤሱ"), e)
    def bstack1ll111ll11l_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        f: TestFramework,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll1l_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        if not bstack1ll111111l1_opy_:
            self.logger.debug(
                bstack1llllll1111_opy_ (u"ࠥࡱࡦࡸ࡫ࡠࡱ࠴࠵ࡾࡥࡳࡺࡰࡦ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦሲ"))
            return
        bstack1l1ll1ll11l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1ll11l1_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1l1ll1ll11l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሳ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠧࠨሴ"))
            return
        if len(bstack1l1ll1ll11l_opy_) > 1:
            self.logger.debug(
                bstack1llllll1111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣስ"))
        bstack1l1ll1lll11_opy_, bstack1l1lllllll1_opy_ = bstack1l1ll1ll11l_opy_[0]
        page = bstack1l1ll1lll11_opy_()
        if not page:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢሶ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠣࠤሷ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l1l111_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢሸ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l1l111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦሹ"),
                bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩሺ").format(
                    json.dumps(
                        {
                            bstack1l1l111_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧሻ"): bstack1l1l111_opy_ (u"ࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣሼ"),
                            bstack1l1l111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥሽ"): {
                                bstack1l1l111_opy_ (u"ࠣࡶࡼࡴࡪࠨሾ"): bstack1l1l111_opy_ (u"ࠤࡄࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠨሿ"),
                                bstack1l1l111_opy_ (u"ࠥࡨࡦࡺࡡࠣቀ"): data,
                                bstack1l1l111_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࠥቁ"): bstack1l1l111_opy_ (u"ࠧࡪࡥࡣࡷࡪࠦቂ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡲ࠵࠶ࡿࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࢁࡽࠣቃ"), e)
    def bstack1ll1111l11l_opy_(
        self,
        instance: bstack1111111l1l_opy_,
        f: TestFramework,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l1ll1lll1l_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        if f.bstack1111l111l1_opy_(instance, bstack1lll1ll11l1_opy_.bstack1ll1111llll_opy_, False):
            return
        self.bstack1ll1llll1l1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1llll111_opy_)
        req.test_framework_name = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1lllll1l_opy_)
        req.test_framework_version = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll11l1l11l_opy_)
        req.test_framework_state = bstack11111l1l1l_opy_[0].name
        req.test_hook_state = bstack11111l1l1l_opy_[1].name
        req.test_uuid = TestFramework.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1ll1ll11_opy_)
        for bstack1l1ll1ll1l1_opy_ in bstack1llll11lll1_opy_.bstack1111lll11l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l1l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨቄ")
                if bstack1ll111111l1_opy_
                else bstack1l1l111_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢቅ")
            )
            session.ref = bstack1l1ll1ll1l1_opy_.ref()
            session.hub_url = bstack1llll11lll1_opy_.bstack1111l111l1_opy_(bstack1l1ll1ll1l1_opy_, bstack1llll11lll1_opy_.bstack1l1llll11l1_opy_, bstack1l1l111_opy_ (u"ࠤࠥቆ"))
            session.framework_name = bstack1l1ll1ll1l1_opy_.framework_name
            session.framework_version = bstack1l1ll1ll1l1_opy_.framework_version
            session.framework_session_id = bstack1llll11lll1_opy_.bstack1111l111l1_opy_(bstack1l1ll1ll1l1_opy_, bstack1llll11lll1_opy_.bstack1l1lll1lll1_opy_, bstack1l1l111_opy_ (u"ࠥࠦቇ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll1l1ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs
    ):
        bstack1l1ll1ll11l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll1ll11l1_opy_.bstack1ll1111111l_opy_, [])
        if not bstack1l1ll1ll11l_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧቈ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠧࠨ቉"))
            return
        if len(bstack1l1ll1ll11l_opy_) > 1:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢቊ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠢࠣቋ"))
        bstack1l1ll1lll11_opy_, bstack1l1lllllll1_opy_ = bstack1l1ll1ll11l_opy_[0]
        page = bstack1l1ll1lll11_opy_()
        if not page:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣቌ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠤࠥቍ"))
            return
        return page
    def bstack1ll1llllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1l1ll1l1ll1_opy_ = {}
        for bstack1l1ll1ll1l1_opy_ in bstack1llll11lll1_opy_.bstack1111lll11l_opy_.values():
            caps = bstack1llll11lll1_opy_.bstack1111l111l1_opy_(bstack1l1ll1ll1l1_opy_, bstack1llll11lll1_opy_.bstack1l1lll11l11_opy_, bstack1l1l111_opy_ (u"ࠥࠦ቎"))
        bstack1l1ll1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ቏")] = caps.get(bstack1l1l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨቐ"), bstack1l1l111_opy_ (u"ࠨࠢቑ"))
        bstack1l1ll1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨቒ")] = caps.get(bstack1l1l111_opy_ (u"ࠣࡱࡶࠦቓ"), bstack1l1l111_opy_ (u"ࠤࠥቔ"))
        bstack1l1ll1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧቕ")] = caps.get(bstack1l1l111_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣቖ"), bstack1l1l111_opy_ (u"ࠧࠨ቗"))
        bstack1l1ll1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢቘ")] = caps.get(bstack1l1l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ቙"), bstack1l1l111_opy_ (u"ࠣࠤቚ"))
        return bstack1l1ll1l1ll1_opy_
    def bstack1ll1lll11ll_opy_(self, page: object, bstack1ll1lll1lll_opy_, args={}):
        try:
            bstack1l1ll1l1111_opy_ = bstack1l1l111_opy_ (u"ࠤࠥࠦ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠩ࠰࠱࠲ࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠭ࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡲࡪࡽࠠࡑࡴࡲࡱ࡮ࡹࡥࠩࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵ࠱ࡴࡺࡹࡨࠩࡴࡨࡷࡴࡲࡶࡦࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡿ࡫ࡴ࡟ࡣࡱࡧࡽࢂࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࢃࠩࠩࡽࡤࡶ࡬ࡥࡪࡴࡱࡱࢁ࠮ࠨࠢࠣቛ")
            bstack1ll1lll1lll_opy_ = bstack1ll1lll1lll_opy_.replace(bstack1l1l111_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨቜ"), bstack1l1l111_opy_ (u"ࠦࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶࠦቝ"))
            script = bstack1l1ll1l1111_opy_.format(fn_body=bstack1ll1lll1lll_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠧࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡋࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵ࠮ࠣࠦ቞") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢ቟"))