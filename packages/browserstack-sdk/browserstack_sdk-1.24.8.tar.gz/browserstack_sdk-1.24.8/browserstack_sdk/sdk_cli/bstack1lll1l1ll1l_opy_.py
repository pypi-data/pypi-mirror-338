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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack11111l1111_opy_,
    bstack1111ll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111l111_opy_, bstack1lllll11111_opy_, bstack1111111l1l_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1llll111lll_opy_ import bstack1lll1lll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l1l_opy_ import bstack1lll1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lllll_opy_ import bstack1llll11lll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
import grpc
import traceback
import json
class bstack1lll11lllll_opy_(bstack1lllll1l111_opy_):
    bstack1lll1111l11_opy_ = False
    bstack1ll1l1lll11_opy_ = bstack1l1l111_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤႹ")
    bstack1ll1lll1ll1_opy_ = bstack1l1l111_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣႺ")
    bstack1ll1ll11l11_opy_ = bstack1l1l111_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩ࡯࡫ࡷࠦႻ")
    bstack1ll1ll11ll1_opy_ = bstack1l1l111_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡵࡢࡷࡨࡧ࡮࡯࡫ࡱ࡫ࠧႼ")
    bstack1ll1lllll11_opy_ = bstack1l1l111_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲࡠࡪࡤࡷࡤࡻࡲ࡭ࠤႽ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1lllll1lll1_opy_, bstack111111lll1_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        if not self.is_enabled():
            return
        self.bstack1ll1l1l1l1l_opy_ = bstack111111lll1_opy_
        bstack1lllll1lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.PRE), self.bstack1ll1l1l11ll_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        TestFramework.bstack1ll1ll1ll1l_opy_((bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST), self.bstack1ll1l1ll111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1lll1111ll1_opy_(instance, args)
        test_framework = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1lllll1l_opy_)
        if bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭Ⴞ") in instance.bstack1lll1111l1l_opy_:
            platform_index = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1llll111_opy_)
            self.accessibility = self.bstack1ll1ll1111l_opy_(tags, self.config[bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ⴟ")][platform_index])
        else:
            capabilities = self.bstack1ll1l1l1l1l_opy_.bstack1ll1llllll1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦჀ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠧࠨჁ"))
                return
            self.accessibility = self.bstack1ll1ll1111l_opy_(tags, capabilities)
        if self.bstack1ll1l1l1l1l_opy_.pages and self.bstack1ll1l1l1l1l_opy_.pages.values():
            bstack1ll1l1lllll_opy_ = list(self.bstack1ll1l1l1l1l_opy_.pages.values())
            if bstack1ll1l1lllll_opy_ and isinstance(bstack1ll1l1lllll_opy_[0], (list, tuple)) and bstack1ll1l1lllll_opy_[0]:
                bstack1ll1ll1l11l_opy_ = bstack1ll1l1lllll_opy_[0][0]
                if callable(bstack1ll1ll1l11l_opy_):
                    page = bstack1ll1ll1l11l_opy_()
                    def bstack11llllll_opy_():
                        self.get_accessibility_results(page, bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥჂ"))
                    def bstack1ll1ll1l1l1_opy_():
                        self.get_accessibility_results_summary(page, bstack1l1l111_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦჃ"))
                    setattr(page, bstack1l1l111_opy_ (u"ࠣࡩࡨࡸࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡖࡪࡹࡵ࡭ࡶࡶࠦჄ"), bstack11llllll_opy_)
                    setattr(page, bstack1l1l111_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡗࡺࡳ࡭ࡢࡴࡼࠦჅ"), bstack1ll1ll1l1l1_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷ࡭ࡵࡵ࡭ࡦࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡷࡣ࡯ࡹࡪࡃࠢ჆") + str(self.accessibility) + bstack1l1l111_opy_ (u"ࠦࠧჇ"))
    def bstack1ll1l1l11ll_opy_(
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
            bstack1111ll11_opy_ = datetime.now()
            self.bstack1ll1llll11l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡭ࡳ࡯ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣ჈"), datetime.now() - bstack1111ll11_opy_)
            if (
                not f.bstack1ll1ll111ll_opy_(method_name)
                or f.bstack1ll1ll11111_opy_(method_name, *args)
                or f.bstack1ll1ll1l111_opy_(method_name, *args)
            ):
                return
            if not f.bstack1111l111l1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1ll11l11_opy_, False):
                if not bstack1lll11lllll_opy_.bstack1lll1111l11_opy_:
                    self.logger.warning(bstack1l1l111_opy_ (u"ࠨ࡛ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤ჉") + str(f.platform_index) + bstack1l1l111_opy_ (u"ࠢ࡞ࠢࡤ࠵࠶ࡿࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡨࡢࡸࡨࠤࡳࡵࡴࠡࡤࡨࡩࡳࠦࡳࡦࡶࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠨ჊"))
                    bstack1lll11lllll_opy_.bstack1lll1111l11_opy_ = True
                return
            bstack1ll1lllllll_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1ll1lllllll_opy_:
                platform_index = f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_, 0)
                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨ჋") + str(f.framework_name) + bstack1l1l111_opy_ (u"ࠤࠥ჌"))
                return
            bstack1lll11111ll_opy_ = f.bstack1ll1ll1l1ll_opy_(*args)
            if not bstack1lll11111ll_opy_:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࠧჍ") + str(method_name) + bstack1l1l111_opy_ (u"ࠦࠧ჎"))
                return
            bstack1ll1l1lll1l_opy_ = f.bstack1111l111l1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1lllll11_opy_, False)
            if bstack1lll11111ll_opy_ == bstack1l1l111_opy_ (u"ࠧ࡭ࡥࡵࠤ჏") and not bstack1ll1l1lll1l_opy_:
                f.bstack1111lllll1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1lllll11_opy_, True)
            if not bstack1ll1l1lll1l_opy_:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠨ࡮ࡰࠢࡘࡖࡑࠦ࡬ࡰࡣࡧࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧა") + str(bstack1lll11111ll_opy_) + bstack1l1l111_opy_ (u"ࠢࠣბ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(bstack1lll11111ll_opy_, [])
            if not scripts_to_run:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨგ") + str(bstack1lll11111ll_opy_) + bstack1l1l111_opy_ (u"ࠤࠥდ"))
                return
            self.logger.info(bstack1l1l111_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠤࢀࡲࡥ࡯ࠪࡶࡧࡷ࡯ࡰࡵࡵࡢࡸࡴࡥࡲࡶࡰࠬࢁࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧე") + str(bstack1lll11111ll_opy_) + bstack1l1l111_opy_ (u"ࠦࠧვ"))
            scripts = [(s, bstack1ll1lllllll_opy_[s]) for s in scripts_to_run if s in bstack1ll1lllllll_opy_]
            for bstack1ll1l1ll11l_opy_, bstack1ll1lll1lll_opy_ in scripts:
                try:
                    bstack1111ll11_opy_ = datetime.now()
                    if bstack1ll1l1ll11l_opy_ == bstack1l1l111_opy_ (u"ࠧࡹࡣࡢࡰࠥზ"):
                        result = self.perform_scan(driver, method=bstack1lll11111ll_opy_, framework_name=f.framework_name)
                    instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾ࠧთ") + bstack1ll1l1ll11l_opy_, datetime.now() - bstack1111ll11_opy_)
                    if isinstance(result, dict) and not result.get(bstack1l1l111_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣი"), True):
                        self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡵ࡮࡭ࡵࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡵࡩࡲࡧࡩ࡯࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡸࡀࠠࠣკ") + str(result) + bstack1l1l111_opy_ (u"ࠤࠥლ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1l1l111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡂࢁࡳࡤࡴ࡬ࡴࡹࡥ࡮ࡢ࡯ࡨࢁࠥ࡫ࡲࡳࡱࡵࡁࠧმ") + str(e) + bstack1l1l111_opy_ (u"ࠦࠧნ"))
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦࠢࡨࡶࡷࡵࡲ࠾ࠤო") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢპ"))
    def bstack1ll1l1ll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1111111l1l_opy_,
        bstack11111l1l1l_opy_: Tuple[bstack111111l111_opy_, bstack1lllll11111_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1lll1111ll1_opy_(instance, args)
        capabilities = self.bstack1ll1l1l1l1l_opy_.bstack1ll1llllll1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        self.accessibility = self.bstack1ll1ll1111l_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦჟ"))
            return
        driver = self.bstack1ll1l1l1l1l_opy_.bstack1ll1l1ll1l1_opy_(f, instance, bstack11111l1l1l_opy_, *args, **kwargs)
        test_name = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_)
        if not test_name:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨრ"))
            return
        test_uuid = f.bstack1111l111l1_opy_(instance, TestFramework.bstack1ll1ll1ll11_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢს"))
            return
        if isinstance(self.bstack1ll1l1l1l1l_opy_, bstack1lll1ll11l1_opy_):
            framework_name = bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧტ")
        else:
            framework_name = bstack1l1l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭უ")
        self.bstack11llllllll_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1ll1ll1l1_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࠨფ"))
            return
        bstack1111ll11_opy_ = datetime.now()
        bstack1ll1lll1lll_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l111_opy_ (u"ࠨࡳࡤࡣࡱࠦქ"), None)
        if not bstack1ll1lll1lll_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡧࡦࡴࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢღ") + str(framework_name) + bstack1l1l111_opy_ (u"ࠣࠢࠥყ"))
            return
        instance = bstack11111l1111_opy_.bstack11111l1lll_opy_(driver)
        if instance:
            if not bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1ll11ll1_opy_, False):
                bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1ll11ll1_opy_, True)
            else:
                self.logger.info(bstack1l1l111_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡳࠦࡰࡳࡱࡪࡶࡪࡹࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨშ") + str(method) + bstack1l1l111_opy_ (u"ࠥࠦჩ"))
                return
        self.logger.info(bstack1l1l111_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤ࠾ࠤც") + str(method) + bstack1l1l111_opy_ (u"ࠧࠨძ"))
        if framework_name == bstack1l1l111_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪწ"):
            result = self.bstack1ll1l1l1l1l_opy_.bstack1ll1lll11ll_opy_(driver, bstack1ll1lll1lll_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1lll1lll_opy_, {bstack1l1l111_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢჭ"): method if method else bstack1l1l111_opy_ (u"ࠣࠤხ")})
        bstack1llll11ll11_opy_.end(EVENTS.bstack1ll1ll1l1_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤჯ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣჰ"), True, None, command=method)
        if instance:
            bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1ll11ll1_opy_, False)
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮ࠣჱ"), datetime.now() - bstack1111ll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack11lllll1ll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢჲ"))
            return
        bstack1ll1lll1lll_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l111_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥჳ"), None)
        if not bstack1ll1lll1lll_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨჴ") + str(framework_name) + bstack1l1l111_opy_ (u"ࠣࠤჵ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1111ll11_opy_ = datetime.now()
        if framework_name == bstack1l1l111_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ჶ"):
            result = self.bstack1ll1l1l1l1l_opy_.bstack1ll1lll11ll_opy_(driver, bstack1ll1lll1lll_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1lll1lll_opy_)
        instance = bstack11111l1111_opy_.bstack11111l1lll_opy_(driver)
        if instance:
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࠨჷ"), datetime.now() - bstack1111ll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l1lll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢჸ"))
            return
        bstack1ll1lll1lll_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l111_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠤჹ"), None)
        if not bstack1ll1lll1lll_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧჺ") + str(framework_name) + bstack1l1l111_opy_ (u"ࠢࠣ჻"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1111ll11_opy_ = datetime.now()
        if framework_name == bstack1l1l111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬჼ"):
            result = self.bstack1ll1l1l1l1l_opy_.bstack1ll1lll11ll_opy_(driver, bstack1ll1lll1lll_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1lll1lll_opy_)
        instance = bstack11111l1111_opy_.bstack11111l1lll_opy_(driver)
        if instance:
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࠨჽ"), datetime.now() - bstack1111ll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll1ll1llll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1ll1ll11l1l_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llllll1lll_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧჾ") + str(r) + bstack1l1l111_opy_ (u"ࠦࠧჿ"))
            else:
                self.bstack1lll11111l1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᄀ") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢᄁ"))
            traceback.print_exc()
            raise e
    def bstack1lll11111l1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࡭ࡱࡤࡨࡤࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢᄂ"))
            return False
        if result.accessibility.options:
            options = result.accessibility.options
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1ll1llll1ll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1ll1l1lll11_opy_ and command.module == self.bstack1ll1lll1ll1_opy_:
                        if command.method and not command.method in bstack1ll1llll1ll_opy_:
                            bstack1ll1llll1ll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1ll1llll1ll_opy_[command.method]:
                            bstack1ll1llll1ll_opy_[command.method][command.name] = list()
                        bstack1ll1llll1ll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1ll1llll1ll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1ll1llll11l_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1ll1l1l1l1l_opy_, bstack1lll1ll11l1_opy_) and method_name != bstack1l1l111_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࠩᄃ"):
            return
        if bstack11111l1111_opy_.bstack1111l1lll1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1ll11l11_opy_):
            return
        if not f.bstack1ll1l1l1l11_opy_(instance):
            if not bstack1lll11lllll_opy_.bstack1lll1111l11_opy_:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠤࡤ࠵࠶ࡿࠠࡧ࡮ࡲࡻࠥࡪࡩࡴࡣࡥࡰࡪࡪࠠࡧࡱࡵࠤࡳࡵ࡮࠮ࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠨᄄ"))
                bstack1lll11lllll_opy_.bstack1lll1111l11_opy_ = True
            return
        if f.bstack1ll1lll1l11_opy_(method_name, *args):
            bstack1lll111111l_opy_ = False
            desired_capabilities = f.bstack1ll1ll111l1_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1ll1lll11l1_opy_(instance)
                platform_index = f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_, 0)
                bstack1ll1l1llll1_opy_ = datetime.now()
                r = self.bstack1ll1ll11l1l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣᄅ"), datetime.now() - bstack1ll1l1llll1_opy_)
                bstack1lll111111l_opy_ = r.success
            else:
                self.logger.error(bstack1l1l111_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡪࡥࡴ࡫ࡵࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࡂࠨᄆ") + str(desired_capabilities) + bstack1l1l111_opy_ (u"ࠧࠨᄇ"))
            f.bstack1111lllll1_opy_(instance, bstack1lll11lllll_opy_.bstack1ll1ll11l11_opy_, bstack1lll111111l_opy_)
    def bstack1l1l1l1ll_opy_(self, test_tags):
        bstack1ll1ll11l1l_opy_ = self.config.get(bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᄈ"))
        if not bstack1ll1ll11l1l_opy_:
            return True
        try:
            include_tags = bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᄉ")] if bstack1l1l111_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᄊ") in bstack1ll1ll11l1l_opy_ and isinstance(bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᄋ")], list) else []
            exclude_tags = bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᄌ")] if bstack1l1l111_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᄍ") in bstack1ll1ll11l1l_opy_ and isinstance(bstack1ll1ll11l1l_opy_[bstack1l1l111_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᄎ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨᄏ") + str(error))
        return False
    def bstack1111lll1l_opy_(self, caps):
        try:
            bstack1ll1l1ll1ll_opy_ = caps.get(bstack1l1l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᄐ"), {}).get(bstack1l1l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᄑ"), caps.get(bstack1l1l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩᄒ"), bstack1l1l111_opy_ (u"ࠪࠫᄓ")))
            if bstack1ll1l1ll1ll_opy_:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᄔ"))
                return False
            browser = caps.get(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᄕ"), bstack1l1l111_opy_ (u"࠭ࠧᄖ")).lower()
            if browser != bstack1l1l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᄗ"):
                self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᄘ"))
                return False
            browser_version = caps.get(bstack1l1l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᄙ"))
            if browser_version and browser_version != bstack1l1l111_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪᄚ") and int(browser_version.split(bstack1l1l111_opy_ (u"ࠫ࠳࠭ᄛ"))[0]) <= 98:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦ࠹࠹࠰ࠥᄜ"))
                return False
            bstack1lll1111111_opy_ = caps.get(bstack1l1l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᄝ"), {}).get(bstack1l1l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᄞ"))
            if bstack1lll1111111_opy_ and bstack1l1l111_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬᄟ") in bstack1lll1111111_opy_.get(bstack1l1l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧᄠ"), []):
                self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧᄡ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨᄢ") + str(error))
            return False
    def bstack11llllllll_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1ll11lll_opy_ = None
        try:
            bstack1lll1111lll_opy_ = {
                bstack1l1l111_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬᄣ"): test_uuid,
                bstack1l1l111_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᄤ"): os.environ.get(bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᄥ"), bstack1l1l111_opy_ (u"ࠨࠩᄦ")),
                bstack1l1l111_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ᄧ"): os.environ.get(bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᄨ"), bstack1l1l111_opy_ (u"ࠫࠬᄩ"))
            }
            self.logger.debug(bstack1l1l111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨᄪ") + str(bstack1lll1111lll_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            bstack1ll1lll1lll_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1l111_opy_ (u"ࠨࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠦᄫ"), None)
            if not bstack1ll1lll1lll_opy_:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᄬ") + str(framework_name) + bstack1l1l111_opy_ (u"ࠣࠢࠥᄭ"))
                return
            bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1ll1l1l1lll_opy_.value)
            self.bstack1ll1ll1lll1_opy_(driver, bstack1ll1lll1lll_opy_, bstack1lll1111lll_opy_, framework_name)
            self.logger.info(bstack1l1l111_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧᄮ"))
            bstack1llll11ll11_opy_.end(EVENTS.bstack1ll1l1l1lll_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᄯ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᄰ"), True, None, command=bstack1l1l111_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᄱ"),test_name=name)
        except Exception as bstack1ll1lll111l_opy_:
            self.logger.error(bstack1l1l111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᄲ") + bstack1l1l111_opy_ (u"ࠢࡴࡶࡵࠬࡵࡧࡴࡩࠫࠥᄳ") + bstack1l1l111_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥᄴ") + str(bstack1ll1lll111l_opy_))
            bstack1llll11ll11_opy_.end(EVENTS.bstack1ll1l1l1lll_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᄵ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᄶ"), False, bstack1ll1lll111l_opy_, command=bstack1l1l111_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᄷ"),test_name=name)
    def bstack1ll1ll1lll1_opy_(self, driver, bstack1ll1lll1lll_opy_, bstack1lll1111lll_opy_, framework_name):
        if framework_name == bstack1l1l111_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᄸ"):
            self.bstack1ll1l1l1l1l_opy_.bstack1ll1lll11ll_opy_(driver, bstack1ll1lll1lll_opy_, bstack1lll1111lll_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1ll1lll1lll_opy_, bstack1lll1111lll_opy_))
    def _1lll1111ll1_opy_(self, instance: bstack1111111l1l_opy_, args: Tuple) -> list:
        bstack1l1l111_opy_ (u"ࠨࠢࠣࡇࡻࡸࡷࡧࡣࡵࠢࡷࡥ࡬ࡹࠠࡣࡣࡶࡩࡩࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࠣࠤࠥᄹ")
        if bstack1l1l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᄺ") in instance.bstack1lll1111l1l_opy_:
            return args[2].tags if hasattr(args[2], bstack1l1l111_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᄻ")) else []
        if hasattr(args[0], bstack1l1l111_opy_ (u"ࠩࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠧᄼ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1ll1ll1111l_opy_(self, tags, capabilities):
        return self.bstack1l1l1l1ll_opy_(tags) and self.bstack1111lll1l_opy_(capabilities)