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
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack1111ll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1lllll11l11_opy_(bstack1lllll1l111_opy_):
    bstack1lll1111l11_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.PRE), self.bstack1ll1l11l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1l11l1ll_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1l11l1l1_opy_(hub_url):
            if not bstack1lllll11l11_opy_.bstack1lll1111l11_opy_:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡰࡴࡩࡡ࡭ࠢࡶࡩࡱ࡬࠭ࡩࡧࡤࡰࠥ࡬࡬ࡰࡹࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡ࡫ࡱࡪࡷࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦᄽ") + str(hub_url) + bstack1l1l111_opy_ (u"ࠦࠧᄾ"))
                bstack1lllll11l11_opy_.bstack1lll1111l11_opy_ = True
            return
        bstack1lll11111ll_opy_ = f.bstack1ll1ll1l1ll_opy_(*args)
        bstack1ll1l1l11l1_opy_ = f.bstack1ll1l11lll1_opy_(*args)
        if bstack1lll11111ll_opy_ and bstack1lll11111ll_opy_.lower() == bstack1l1l111_opy_ (u"ࠧ࡬ࡩ࡯ࡦࡨࡰࡪࡳࡥ࡯ࡶࠥᄿ") and bstack1ll1l1l11l1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1ll1l1l11l1_opy_.get(bstack1l1l111_opy_ (u"ࠨࡵࡴ࡫ࡱ࡫ࠧᅀ"), None), bstack1ll1l1l11l1_opy_.get(bstack1l1l111_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨᅁ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡽࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࡾ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡻࡳࡪࡰࡪࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡵࡲࠡࡣࡵ࡫ࡸ࠴ࡶࡢ࡮ࡸࡩࡂࠨᅂ") + str(locator_value) + bstack1l1l111_opy_ (u"ࠤࠥᅃ"))
                return
            def bstack1111lll1l1_opy_(driver, bstack1ll1l11ll1l_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1ll1l11ll1l_opy_(driver, *args, **kwargs)
                    response = self.bstack1ll1l1l111l_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1l1l111_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨᅄ") + str(locator_value) + bstack1l1l111_opy_ (u"ࠦࠧᅅ"))
                    else:
                        self.logger.warning(bstack1l1l111_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸ࠳࡮ࡰ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠽ࠣᅆ") + str(response) + bstack1l1l111_opy_ (u"ࠨࠢᅇ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1ll1l11llll_opy_(
                        driver, bstack1ll1l11ll1l_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1111lll1l1_opy_.__name__ = bstack1lll11111ll_opy_
            return bstack1111lll1l1_opy_
    def __1ll1l11llll_opy_(
        self,
        driver,
        bstack1ll1l11ll1l_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1ll1l1l111l_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1l1l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡷࡶ࡮࡭ࡧࡦࡴࡨࡨ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࠢᅈ") + str(locator_value) + bstack1l1l111_opy_ (u"ࠣࠤᅉ"))
                bstack1ll1l11l11l_opy_ = self.bstack1ll1l1l1111_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1l1l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡩࡧࡤࡰ࡮ࡴࡧࡠࡴࡨࡷࡺࡲࡴ࠾ࠤᅊ") + str(bstack1ll1l11l11l_opy_) + bstack1l1l111_opy_ (u"ࠥࠦᅋ"))
                if bstack1ll1l11l11l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1l1l111_opy_ (u"ࠦࡺࡹࡩ࡯ࡩࠥᅌ"): bstack1ll1l11l11l_opy_.locator_type,
                            bstack1l1l111_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᅍ"): bstack1ll1l11l11l_opy_.locator_value,
                        }
                    )
                    return bstack1ll1l11ll1l_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1l1l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡉࡠࡆࡈࡆ࡚ࡍࠢᅎ"), False):
                    self.logger.info(bstack1llllll1111_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠯ࡰ࡭ࡸࡹࡩ࡯ࡩ࠽ࠤࡸࡲࡥࡦࡲࠫ࠷࠵࠯ࠠ࡭ࡧࡷࡸ࡮ࡴࡧࠡࡻࡲࡹࠥ࡯࡮ࡴࡲࡨࡧࡹࠦࡴࡩࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࠠ࡭ࡱࡪࡷࠧᅏ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦᅐ") + str(response) + bstack1l1l111_opy_ (u"ࠤࠥᅑ"))
        except Exception as err:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠿ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢᅒ") + str(err) + bstack1l1l111_opy_ (u"ࠦࠧᅓ"))
        raise exception
    @measure(event_name=EVENTS.bstack1ll1l11ll11_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1ll1l1l111l_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1l1l111_opy_ (u"ࠧ࠶ࠢᅔ"),
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1l1l111_opy_ (u"ࠨࠢᅕ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llllll1lll_opy_.AISelfHealStep(req)
            self.logger.info(bstack1l1l111_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᅖ") + str(r) + bstack1l1l111_opy_ (u"ࠣࠤᅗ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᅘ") + str(e) + bstack1l1l111_opy_ (u"ࠥࠦᅙ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1l11l111_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1ll1l1l1111_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1l1l111_opy_ (u"ࠦ࠵ࠨᅚ")):
        self.bstack1ll1llll1l1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llllll1lll_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1l1l111_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᅛ") + str(r) + bstack1l1l111_opy_ (u"ࠨࠢᅜ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᅝ") + str(e) + bstack1l1l111_opy_ (u"ࠣࠤᅞ"))
            traceback.print_exc()
            raise e