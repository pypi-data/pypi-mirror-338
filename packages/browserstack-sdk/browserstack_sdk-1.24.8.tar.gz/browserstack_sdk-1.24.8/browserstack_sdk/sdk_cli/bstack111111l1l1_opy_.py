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
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
    bstack1111ll11ll_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1llll1lllll_opy_ import bstack1llll11lll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1lll1ll1_opy_
from bstack_utils.helper import bstack1ll111111l1_opy_
import threading
import os
import urllib.parse
class bstack1lllllll1ll_opy_(bstack1lllll1l111_opy_):
    def __init__(self, bstack111111lll1_opy_):
        super().__init__()
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1lll_opy_, bstack1111llll11_opy_.PRE), self.bstack1l1llll1111_opy_)
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1lll_opy_, bstack1111llll11_opy_.PRE), self.bstack1l1lll1l1l1_opy_)
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111l1l1ll_opy_, bstack1111llll11_opy_.PRE), self.bstack1l1lll1llll_opy_)
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1ll1_opy_, bstack1111llll11_opy_.PRE), self.bstack1l1lll1111l_opy_)
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.bstack1111ll1lll_opy_, bstack1111llll11_opy_.PRE), self.bstack1l1lll11ll1_opy_)
        bstack1llll11lll1_opy_.bstack1ll1ll1ll1l_opy_((bstack11111l11l1_opy_.QUIT, bstack1111llll11_opy_.PRE), self.on_close)
        self.bstack111111lll1_opy_ = bstack111111lll1_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1l1llll1111_opy_(
        self,
        f: bstack1llll11lll1_opy_,
        bstack1l1lll111ll_opy_: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠥࡰࡦࡻ࡮ࡤࡪࠥᇬ"):
            return
        if not bstack1ll111111l1_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡰࡦࡻ࡮ࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇭ"))
            return
        def wrapped(bstack1l1lll111ll_opy_, launch, *args, **kwargs):
            response = self.bstack1l1lll1l11l_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1l111_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᇮ"): True}).encode(bstack1l1l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇯ")))
            if response is not None and response.capabilities:
                if not bstack1ll111111l1_opy_():
                    browser = launch(bstack1l1lll111ll_opy_)
                    return browser
                bstack1l1llll11ll_opy_ = json.loads(response.capabilities.decode(bstack1l1l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᇰ")))
                if not bstack1l1llll11ll_opy_: # empty caps bstack1l1lll11lll_opy_ bstack1l1llll111l_opy_ bstack1l1lll111l1_opy_ bstack1lll11lll11_opy_ or error in processing
                    return
                bstack1l1lll1ll11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1llll11ll_opy_))
                f.bstack1111lllll1_opy_(instance, bstack1llll11lll1_opy_.bstack1l1llll11l1_opy_, bstack1l1lll1ll11_opy_)
                f.bstack1111lllll1_opy_(instance, bstack1llll11lll1_opy_.bstack1l1lll11l11_opy_, bstack1l1llll11ll_opy_)
                browser = bstack1l1lll111ll_opy_.connect(bstack1l1lll1ll11_opy_)
                return browser
        return wrapped
    def bstack1l1lll1llll_opy_(
        self,
        f: bstack1llll11lll1_opy_,
        Connection: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠣࡦ࡬ࡷࡵࡧࡴࡤࡪࠥᇱ"):
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡦ࡬ࡷࡵࡧࡴࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇲ"))
            return
        if not bstack1ll111111l1_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l1l111_opy_ (u"ࠪࡴࡦࡸࡡ࡮ࡵࠪᇳ"), {}).get(bstack1l1l111_opy_ (u"ࠫࡧࡹࡐࡢࡴࡤࡱࡸ࠭ᇴ")):
                    bstack1l1lll1l1ll_opy_ = args[0][bstack1l1l111_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᇵ")][bstack1l1l111_opy_ (u"ࠨࡢࡴࡒࡤࡶࡦࡳࡳࠣᇶ")]
                    session_id = bstack1l1lll1l1ll_opy_.get(bstack1l1l111_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡊࡦࠥᇷ"))
                    f.bstack1111lllll1_opy_(instance, bstack1llll11lll1_opy_.bstack1l1lll1lll1_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡥ࡫ࡶࡴࡦࡺࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࠦᇸ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1l1lll11ll1_opy_(
        self,
        f: bstack1llll11lll1_opy_,
        bstack1l1lll111ll_opy_: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥᇹ"):
            return
        if not bstack1ll111111l1_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡦࡳࡳࡴࡥࡤࡶࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇺ"))
            return
        def wrapped(bstack1l1lll111ll_opy_, connect, *args, **kwargs):
            response = self.bstack1l1lll1l11l_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1l111_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᇻ"): True}).encode(bstack1l1l111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇼ")))
            if response is not None and response.capabilities:
                bstack1l1llll11ll_opy_ = json.loads(response.capabilities.decode(bstack1l1l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇽ")))
                if not bstack1l1llll11ll_opy_:
                    return
                bstack1l1lll1ll11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1llll11ll_opy_))
                if bstack1l1llll11ll_opy_.get(bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᇾ")):
                    browser = bstack1l1lll111ll_opy_.bstack1l1lll11l1l_opy_(bstack1l1lll1ll11_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1l1lll1ll11_opy_
                    return connect(bstack1l1lll111ll_opy_, *args, **kwargs)
        return wrapped
    def bstack1l1lll1l1l1_opy_(
        self,
        f: bstack1llll11lll1_opy_,
        bstack1ll1l11111l_opy_: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥᇿ"):
            return
        if not bstack1ll111111l1_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡰࡨࡻࡤࡶࡡࡨࡧࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣሀ"))
            return
        def wrapped(bstack1ll1l11111l_opy_, bstack1l1lll1ll1l_opy_, *args, **kwargs):
            contexts = bstack1ll1l11111l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l1l111_opy_ (u"ࠥࡥࡧࡵࡵࡵ࠼ࡥࡰࡦࡴ࡫ࠣሁ") in page.url:
                                    return page
                    else:
                        return bstack1l1lll1ll1l_opy_(bstack1ll1l11111l_opy_)
        return wrapped
    def bstack1l1lll1l11l_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤሂ") + str(req) + bstack1l1l111_opy_ (u"ࠧࠨሃ"))
        try:
            r = self.bstack1llllll1lll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤሄ") + str(r.success) + bstack1l1l111_opy_ (u"ࠢࠣህ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨሆ") + str(e) + bstack1l1l111_opy_ (u"ࠤࠥሇ"))
            traceback.print_exc()
            raise e
    def bstack1l1lll1111l_opy_(
        self,
        f: bstack1llll11lll1_opy_,
        Connection: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠥࡣࡸ࡫࡮ࡥࡡࡰࡩࡸࡹࡡࡨࡧࡢࡸࡴࡥࡳࡦࡴࡹࡩࡷࠨለ"):
            return
        if not bstack1ll111111l1_opy_():
            return
        def wrapped(Connection, bstack1l1lll1l111_opy_, *args, **kwargs):
            return bstack1l1lll1l111_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1llll11lll1_opy_,
        bstack1l1lll111ll_opy_: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1l111_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥሉ"):
            return
        if not bstack1ll111111l1_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡨࡲ࡯ࡴࡧࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣሊ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped