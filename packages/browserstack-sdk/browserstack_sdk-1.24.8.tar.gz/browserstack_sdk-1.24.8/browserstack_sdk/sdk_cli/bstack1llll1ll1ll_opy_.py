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
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack1111ll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1lll1ll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
class bstack1llllll1l11_opy_(bstack1lllll1l111_opy_):
    bstack1l1l1llllll_opy_ = bstack1l1l111_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢበ")
    bstack1l1ll11ll1l_opy_ = bstack1l1l111_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵࠤቡ")
    bstack1l1ll111l11_opy_ = bstack1l1l111_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱࠤቢ")
    def __init__(self, bstack1lll1l1ll1l_opy_):
        super().__init__()
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1lll_opy_, bstack1111llll11_opy_.PRE), self.bstack1l1ll111lll_opy_)
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.PRE), self.bstack1ll1l11l1ll_opy_)
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.POST), self.bstack1l1l1ll1ll1_opy_)
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.POST), self.bstack1l1ll11l1l1_opy_)
        bstack1lll1l11lll_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.QUIT, bstack1111llll11_opy_.POST), self.bstack1l1l1lll1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1ll111lll_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧባ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            self.bstack1l1l1ll1l11_opy_(instance, f, kwargs)
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡦ࠯ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࡿ࠽ࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥቤ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠧࠨብ"))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
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
        instance, method_name = exec
        if f.bstack1111l111l1_opy_(instance, bstack1llllll1l11_opy_.bstack1l1l1llllll_opy_, False):
            return
        if not f.bstack1111l1lll1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_):
            return
        platform_index = f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_)
        if f.bstack1ll1lll1l11_opy_(method_name, *args) and len(args) > 1:
            bstack1111ll11_opy_ = datetime.now()
            hub_url = bstack1lll1l11lll_opy_.hub_url(driver)
            self.logger.warning(bstack1l1l111_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲ࠽ࠣቦ") + str(hub_url) + bstack1l1l111_opy_ (u"ࠢࠣቧ"))
            bstack1l1ll11l1ll_opy_ = args[1][bstack1l1l111_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢቨ")] if isinstance(args[1], dict) and bstack1l1l111_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣቩ") in args[1] else None
            bstack1l1l1lllll1_opy_ = bstack1l1l111_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣቪ")
            if isinstance(bstack1l1ll11l1ll_opy_, dict):
                bstack1111ll11_opy_ = datetime.now()
                r = self.bstack1l1l1ll1lll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤቫ"), datetime.now() - bstack1111ll11_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l1l111_opy_ (u"ࠧࡹ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫࠿ࠦࠢቬ") + str(r) + bstack1l1l111_opy_ (u"ࠨࠢቭ"))
                        return
                    if r.hub_url:
                        f.bstack1l1l1llll11_opy_(instance, driver, r.hub_url)
                        f.bstack1111lllll1_opy_(instance, bstack1llllll1l11_opy_.bstack1l1l1llllll_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l1l111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨቮ"), e)
    def bstack1l1l1ll1ll1_opy_(
        self,
        f: bstack1lll1l11lll_opy_,
        driver: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lll1l11lll_opy_.session_id(driver)
            if session_id:
                bstack1l1l1lll1ll_opy_ = bstack1l1l111_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥቯ").format(session_id)
                bstack1llll11ll11_opy_.mark(bstack1l1l1lll1ll_opy_)
    def bstack1l1ll11l1l1_opy_(
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
        if f.bstack1111l111l1_opy_(instance, bstack1llllll1l11_opy_.bstack1l1ll11ll1l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lll1l11lll_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨተ") + str(hub_url) + bstack1l1l111_opy_ (u"ࠥࠦቱ"))
            return
        framework_session_id = bstack1lll1l11lll_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l1l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢቲ") + str(framework_session_id) + bstack1l1l111_opy_ (u"ࠧࠨታ"))
            return
        if bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args) == bstack1lll1l11lll_opy_.bstack1l1ll11111l_opy_:
            bstack1l1ll11l11l_opy_ = bstack1l1l111_opy_ (u"ࠨࡻࡾ࠼ࡨࡲࡩࠨቴ").format(framework_session_id)
            bstack1l1l1lll1ll_opy_ = bstack1l1l111_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤት").format(framework_session_id)
            bstack1llll11ll11_opy_.end(
                label=bstack1l1l111_opy_ (u"ࠣࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶ࡯ࡴࡶ࠰࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠦቶ"),
                start=bstack1l1l1lll1ll_opy_,
                end=bstack1l1ll11l11l_opy_,
                status=True,
                failure=None
            )
            bstack1111ll11_opy_ = datetime.now()
            r = self.bstack1l1ll11lll1_opy_(
                ref,
                f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣቷ"), datetime.now() - bstack1111ll11_opy_)
            f.bstack1111lllll1_opy_(instance, bstack1llllll1l11_opy_.bstack1l1ll11ll1l_opy_, r.success)
    def bstack1l1l1lll1l1_opy_(
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
        if f.bstack1111l111l1_opy_(instance, bstack1llllll1l11_opy_.bstack1l1ll111l11_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lll1l11lll_opy_.session_id(driver)
        hub_url = bstack1lll1l11lll_opy_.hub_url(driver)
        bstack1111ll11_opy_ = datetime.now()
        r = self.bstack1l1l1lll111_opy_(
            ref,
            f.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣቸ"), datetime.now() - bstack1111ll11_opy_)
        f.bstack1111lllll1_opy_(instance, bstack1llllll1l11_opy_.bstack1l1ll111l11_opy_, r.success)
    @measure(event_name=EVENTS.bstack11l11llll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1l1lll1l11l_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤቹ") + str(req) + bstack1l1l111_opy_ (u"ࠧࠨቺ"))
        try:
            r = self.bstack1llllll1lll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤቻ") + str(r.success) + bstack1l1l111_opy_ (u"ࠢࠣቼ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨች") + str(e) + bstack1l1l111_opy_ (u"ࠤࠥቾ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll111ll1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1l1l1ll1lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧቿ") + str(req) + bstack1l1l111_opy_ (u"ࠦࠧኀ"))
        try:
            r = self.bstack1llllll1lll_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣኁ") + str(r.success) + bstack1l1l111_opy_ (u"ࠨࠢኂ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧኃ") + str(e) + bstack1l1l111_opy_ (u"ࠣࠤኄ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l1ll11ll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1l1ll11lll1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶ࠽ࠤࠧኅ") + str(req) + bstack1l1l111_opy_ (u"ࠥࠦኆ"))
        try:
            r = self.bstack1llllll1lll_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨኇ") + str(r) + bstack1l1l111_opy_ (u"ࠧࠨኈ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦ኉") + str(e) + bstack1l1l111_opy_ (u"ࠢࠣኊ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll111l1l_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1l1l1lll111_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1ll1llll1l1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰ࠻ࠢࠥኋ") + str(req) + bstack1l1l111_opy_ (u"ࠤࠥኌ"))
        try:
            r = self.bstack1llllll1lll_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧኍ") + str(r) + bstack1l1l111_opy_ (u"ࠦࠧ኎"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥ኏") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢነ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l111_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1l1l1ll1l11_opy_(self, instance: bstack1111ll11ll_opy_, f: bstack1lll1l11lll_opy_, kwargs):
        bstack1l1ll11l111_opy_ = version.parse(f.framework_version)
        bstack1l1ll111111_opy_ = kwargs.get(bstack1l1l111_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣኑ"))
        bstack1l1ll11ll11_opy_ = kwargs.get(bstack1l1l111_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣኒ"))
        bstack1l1llll11ll_opy_ = {}
        bstack1l1ll1111ll_opy_ = {}
        bstack1l1l1llll1l_opy_ = None
        bstack1l1l1lll11l_opy_ = {}
        if bstack1l1ll11ll11_opy_ is not None or bstack1l1ll111111_opy_ is not None: # check top level caps
            if bstack1l1ll11ll11_opy_ is not None:
                bstack1l1l1lll11l_opy_[bstack1l1l111_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩና")] = bstack1l1ll11ll11_opy_
            if bstack1l1ll111111_opy_ is not None and callable(getattr(bstack1l1ll111111_opy_, bstack1l1l111_opy_ (u"ࠥࡸࡴࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧኔ"))):
                bstack1l1l1lll11l_opy_[bstack1l1l111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࡤࡧࡳࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧን")] = bstack1l1ll111111_opy_.to_capabilities()
        response = self.bstack1l1lll1l11l_opy_(f.platform_index, instance.ref(), json.dumps(bstack1l1l1lll11l_opy_).encode(bstack1l1l111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦኖ")))
        if response is not None and response.capabilities:
            bstack1l1llll11ll_opy_ = json.loads(response.capabilities.decode(bstack1l1l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧኗ")))
            if not bstack1l1llll11ll_opy_: # empty caps bstack1l1lll11lll_opy_ bstack1l1llll111l_opy_ bstack1l1lll111l1_opy_ bstack1lll11lll11_opy_ or error in processing
                return
            bstack1l1l1llll1l_opy_ = f.bstack1lll1l11l1l_opy_[bstack1l1l111_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦኘ")](bstack1l1llll11ll_opy_)
        if bstack1l1ll111111_opy_ is not None and bstack1l1ll11l111_opy_ >= version.parse(bstack1l1l111_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧኙ")):
            bstack1l1ll1111ll_opy_ = None
        if (
                not bstack1l1ll111111_opy_ and not bstack1l1ll11ll11_opy_
        ) or (
                bstack1l1ll11l111_opy_ < version.parse(bstack1l1l111_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨኚ"))
        ):
            bstack1l1ll1111ll_opy_ = {}
            bstack1l1ll1111ll_opy_.update(bstack1l1llll11ll_opy_)
        self.logger.info(bstack1l1lll1ll1_opy_)
        if os.environ.get(bstack1l1l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨኛ")).lower().__eq__(bstack1l1l111_opy_ (u"ࠦࡹࡸࡵࡦࠤኜ")):
            kwargs.update(
                {
                    bstack1l1l111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣኝ"): f.bstack1l1ll1111l1_opy_,
                }
            )
        if bstack1l1ll11l111_opy_ >= version.parse(bstack1l1l111_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ኞ")):
            if bstack1l1ll11ll11_opy_ is not None:
                del kwargs[bstack1l1l111_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢኟ")]
            kwargs.update(
                {
                    bstack1l1l111_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤአ"): bstack1l1l1llll1l_opy_,
                    bstack1l1l111_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨኡ"): True,
                    bstack1l1l111_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥኢ"): None,
                }
            )
        elif bstack1l1ll11l111_opy_ >= version.parse(bstack1l1l111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪኣ")):
            kwargs.update(
                {
                    bstack1l1l111_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧኤ"): bstack1l1ll1111ll_opy_,
                    bstack1l1l111_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢእ"): bstack1l1l1llll1l_opy_,
                    bstack1l1l111_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦኦ"): True,
                    bstack1l1l111_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣኧ"): None,
                }
            )
        elif bstack1l1ll11l111_opy_ >= version.parse(bstack1l1l111_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩከ")):
            kwargs.update(
                {
                    bstack1l1l111_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥኩ"): bstack1l1ll1111ll_opy_,
                    bstack1l1l111_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣኪ"): True,
                    bstack1l1l111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧካ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l1l111_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨኬ"): bstack1l1ll1111ll_opy_,
                    bstack1l1l111_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦክ"): True,
                    bstack1l1l111_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣኮ"): None,
                }
            )