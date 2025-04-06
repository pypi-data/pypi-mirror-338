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
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import (
    bstack11111l1111_opy_,
    bstack1111ll11ll_opy_,
    bstack11111l11l1_opy_,
    bstack1111llll11_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
from bstack_utils.constants import EVENTS
class bstack1lll1l11lll_opy_(bstack11111l1111_opy_):
    bstack1l1l1l11ll1_opy_ = bstack1l1l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥᐜ")
    NAME = bstack1l1l111_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᐝ")
    bstack1l1llll11l1_opy_ = bstack1l1l111_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࠨᐞ")
    bstack1l1lll1lll1_opy_ = bstack1l1l111_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᐟ")
    bstack1l11l11ll1l_opy_ = bstack1l1l111_opy_ (u"ࠢࡪࡰࡳࡹࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᐠ")
    bstack1l1lll11l11_opy_ = bstack1l1l111_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᐡ")
    bstack1l1l1ll1111_opy_ = bstack1l1l111_opy_ (u"ࠤ࡬ࡷࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡭ࡻࡢࠣᐢ")
    bstack1l11l11lll1_opy_ = bstack1l1l111_opy_ (u"ࠥࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᐣ")
    bstack1l11l1l1l11_opy_ = bstack1l1l111_opy_ (u"ࠦࡪࡴࡤࡦࡦࡢࡥࡹࠨᐤ")
    bstack1ll1llll111_opy_ = bstack1l1l111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨᐥ")
    bstack1l1ll11111l_opy_ = bstack1l1l111_opy_ (u"ࠨ࡮ࡦࡹࡶࡩࡸࡹࡩࡰࡰࠥᐦ")
    bstack1l11l1l111l_opy_ = bstack1l1l111_opy_ (u"ࠢࡨࡧࡷࠦᐧ")
    bstack1ll111lllll_opy_ = bstack1l1l111_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᐨ")
    bstack1l1l1l11lll_opy_ = bstack1l1l111_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࠧᐩ")
    bstack1l1l1l11l1l_opy_ = bstack1l1l111_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࡧࡳࡺࡰࡦࠦᐪ")
    bstack1l11l11llll_opy_ = bstack1l1l111_opy_ (u"ࠦࡶࡻࡩࡵࠤᐫ")
    bstack1l11l11ll11_opy_: Dict[str, List[Callable]] = dict()
    bstack1l1ll1111l1_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1l11l1l_opy_: Any
    bstack1l1l1l1111l_opy_: Dict
    def __init__(
        self,
        bstack1l1ll1111l1_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lll1l11l1l_opy_: Dict[str, Any],
        methods=[bstack1l1l111_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢᐬ"), bstack1l1l111_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᐭ"), bstack1l1l111_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᐮ"), bstack1l1l111_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᐯ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1l1ll1111l1_opy_ = bstack1l1ll1111l1_opy_
        self.platform_index = platform_index
        self.bstack11111lllll_opy_(methods)
        self.bstack1lll1l11l1l_opy_ = bstack1lll1l11l1l_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack11111l1111_opy_.get_data(bstack1lll1l11lll_opy_.bstack1l1lll1lll1_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack11111l1111_opy_.get_data(bstack1lll1l11lll_opy_.bstack1l1llll11l1_opy_, target, strict)
    @staticmethod
    def bstack1l11l1l11l1_opy_(target: object, strict=True):
        return bstack11111l1111_opy_.get_data(bstack1lll1l11lll_opy_.bstack1l11l11ll1l_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack11111l1111_opy_.get_data(bstack1lll1l11lll_opy_.bstack1l1lll11l11_opy_, target, strict)
    @staticmethod
    def bstack1ll1l1l1l11_opy_(instance: bstack1111ll11ll_opy_) -> bool:
        return bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1l1l1ll1111_opy_, False)
    @staticmethod
    def bstack1ll1lll11l1_opy_(instance: bstack1111ll11ll_opy_, default_value=None):
        return bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1l1llll11l1_opy_, default_value)
    @staticmethod
    def bstack1ll1ll111l1_opy_(instance: bstack1111ll11ll_opy_, default_value=None):
        return bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, bstack1lll1l11lll_opy_.bstack1l1lll11l11_opy_, default_value)
    @staticmethod
    def bstack1ll1l11l1l1_opy_(hub_url: str, bstack1l11l1l1111_opy_=bstack1l1l111_opy_ (u"ࠤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࠨᐰ")):
        try:
            bstack1l11l11l1ll_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack1l11l11l1ll_opy_.endswith(bstack1l11l1l1111_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1ll1ll111ll_opy_(method_name: str):
        return method_name == bstack1l1l111_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᐱ")
    @staticmethod
    def bstack1ll1lll1l11_opy_(method_name: str, *args):
        return (
            bstack1lll1l11lll_opy_.bstack1ll1ll111ll_opy_(method_name)
            and bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args) == bstack1lll1l11lll_opy_.bstack1l1ll11111l_opy_
        )
    @staticmethod
    def bstack1ll1ll11111_opy_(method_name: str, *args):
        if not bstack1lll1l11lll_opy_.bstack1ll1ll111ll_opy_(method_name):
            return False
        if not bstack1lll1l11lll_opy_.bstack1l1l1l11lll_opy_ in bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args):
            return False
        bstack1ll1l1l11l1_opy_ = bstack1lll1l11lll_opy_.bstack1ll1l11lll1_opy_(*args)
        return bstack1ll1l1l11l1_opy_ and bstack1l1l111_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᐲ") in bstack1ll1l1l11l1_opy_ and bstack1l1l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᐳ") in bstack1ll1l1l11l1_opy_[bstack1l1l111_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᐴ")]
    @staticmethod
    def bstack1ll1ll1l111_opy_(method_name: str, *args):
        if not bstack1lll1l11lll_opy_.bstack1ll1ll111ll_opy_(method_name):
            return False
        if not bstack1lll1l11lll_opy_.bstack1l1l1l11lll_opy_ in bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args):
            return False
        bstack1ll1l1l11l1_opy_ = bstack1lll1l11lll_opy_.bstack1ll1l11lll1_opy_(*args)
        return (
            bstack1ll1l1l11l1_opy_
            and bstack1l1l111_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᐵ") in bstack1ll1l1l11l1_opy_
            and bstack1l1l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸࡩࡲࡪࡲࡷࠦᐶ") in bstack1ll1l1l11l1_opy_[bstack1l1l111_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᐷ")]
        )
    @staticmethod
    def bstack1l1l1ll1l1l_opy_(*args):
        return str(bstack1lll1l11lll_opy_.bstack1ll1ll1l1ll_opy_(*args)).lower()
    @staticmethod
    def bstack1ll1ll1l1ll_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll1l11lll1_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11l1l1llll_opy_(driver):
        command_executor = getattr(driver, bstack1l1l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᐸ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1l1l111_opy_ (u"ࠦࡤࡻࡲ࡭ࠤᐹ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1l1l111_opy_ (u"ࠧࡥࡣ࡭࡫ࡨࡲࡹࡥࡣࡰࡰࡩ࡭࡬ࠨᐺ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1l1l111_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡥࡳࡦࡴࡹࡩࡷࡥࡡࡥࡦࡵࠦᐻ"), None)
        return hub_url
    def bstack1l1l1llll11_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1l1l111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᐼ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1l1l111_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᐽ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1l1l111_opy_ (u"ࠤࡢࡹࡷࡲࠢᐾ")):
                setattr(command_executor, bstack1l1l111_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᐿ"), hub_url)
                result = True
        if result:
            self.bstack1l1ll1111l1_opy_ = hub_url
            bstack1lll1l11lll_opy_.bstack1111lllll1_opy_(instance, bstack1lll1l11lll_opy_.bstack1l1llll11l1_opy_, hub_url)
            bstack1lll1l11lll_opy_.bstack1111lllll1_opy_(
                instance, bstack1lll1l11lll_opy_.bstack1l1l1ll1111_opy_, bstack1lll1l11lll_opy_.bstack1ll1l11l1l1_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_]):
        return bstack1l1l111_opy_ (u"ࠦ࠿ࠨᑀ").join((bstack11111l11l1_opy_(bstack11111l1l1l_opy_[0]).name, bstack1111llll11_opy_(bstack11111l1l1l_opy_[1]).name))
    @staticmethod
    def bstack1ll1ll1ll1l_opy_(bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_], callback: Callable):
        bstack1l1l11lllll_opy_ = bstack1lll1l11lll_opy_.bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_)
        if not bstack1l1l11lllll_opy_ in bstack1lll1l11lll_opy_.bstack1l11l11ll11_opy_:
            bstack1lll1l11lll_opy_.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_] = []
        bstack1lll1l11lll_opy_.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_].append(callback)
    def bstack11111ll1l1_opy_(self, instance: bstack1111ll11ll_opy_, method_name: str, bstack1111l1llll_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1l1l111_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᑁ")):
            return
        cmd = args[0] if method_name == bstack1l1l111_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᑂ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack1l11l1l11ll_opy_ = bstack1l1l111_opy_ (u"ࠢ࠻ࠤᑃ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠤᑄ") + bstack1l11l1l11ll_opy_, bstack1111l1llll_opy_)
    def bstack1111ll1111_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111ll11ll_opy_, str],
        bstack11111l1l1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1111llll11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1111ll1l11_opy_, bstack1l1l1l11111_opy_ = bstack11111l1l1l_opy_
        bstack1l1l11lllll_opy_ = bstack1lll1l11lll_opy_.bstack1l1l1l111l1_opy_(bstack11111l1l1l_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡲࡲࡤ࡮࡯ࡰ࡭࠽ࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᑅ") + str(kwargs) + bstack1l1l111_opy_ (u"ࠥࠦᑆ"))
        if bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.QUIT:
            if bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.PRE:
                bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1ll1lll1111_opy_(EVENTS.bstack1lllll1l11_opy_.value)
                bstack11111l1111_opy_.bstack1111lllll1_opy_(instance, EVENTS.bstack1lllll1l11_opy_.value, bstack1ll1ll11lll_opy_)
                self.logger.debug(bstack1l1l111_opy_ (u"ࠦ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠡࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠣᑇ").format(instance, method_name, bstack1111ll1l11_opy_, bstack1l1l1l11111_opy_))
        if bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.bstack1111ll1lll_opy_:
            if bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.POST and not bstack1lll1l11lll_opy_.bstack1l1lll1lll1_opy_ in instance.data:
                session_id = getattr(target, bstack1l1l111_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᑈ"), None)
                if session_id:
                    instance.data[bstack1lll1l11lll_opy_.bstack1l1lll1lll1_opy_] = session_id
        elif (
            bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.bstack1111ll1ll1_opy_
            and bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args) == bstack1lll1l11lll_opy_.bstack1l1ll11111l_opy_
        ):
            if bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.PRE:
                hub_url = bstack1lll1l11lll_opy_.bstack11l1l1llll_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lll1l11lll_opy_.bstack1l1llll11l1_opy_: hub_url,
                            bstack1lll1l11lll_opy_.bstack1l1l1ll1111_opy_: bstack1lll1l11lll_opy_.bstack1ll1l11l1l1_opy_(hub_url),
                            bstack1lll1l11lll_opy_.bstack1ll1llll111_opy_: int(
                                os.environ.get(bstack1l1l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᑉ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1ll1l1l11l1_opy_ = bstack1lll1l11lll_opy_.bstack1ll1l11lll1_opy_(*args)
                bstack1l11l1l11l1_opy_ = bstack1ll1l1l11l1_opy_.get(bstack1l1l111_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᑊ"), None) if bstack1ll1l1l11l1_opy_ else None
                if isinstance(bstack1l11l1l11l1_opy_, dict):
                    instance.data[bstack1lll1l11lll_opy_.bstack1l11l11ll1l_opy_] = copy.deepcopy(bstack1l11l1l11l1_opy_)
                    instance.data[bstack1lll1l11lll_opy_.bstack1l1lll11l11_opy_] = bstack1l11l1l11l1_opy_
            elif bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1l1l111_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢᑋ"), dict()).get(bstack1l1l111_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡌࡨࠧᑌ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lll1l11lll_opy_.bstack1l1lll1lll1_opy_: framework_session_id,
                                bstack1lll1l11lll_opy_.bstack1l11l11lll1_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.bstack1111ll1ll1_opy_
            and bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args) == bstack1lll1l11lll_opy_.bstack1l11l11llll_opy_
            and bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.POST
        ):
            instance.data[bstack1lll1l11lll_opy_.bstack1l11l1l1l11_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1l11lllll_opy_ in bstack1lll1l11lll_opy_.bstack1l11l11ll11_opy_:
            bstack1l1l11llll1_opy_ = None
            for callback in bstack1lll1l11lll_opy_.bstack1l11l11ll11_opy_[bstack1l1l11lllll_opy_]:
                try:
                    bstack1l1l1l11l11_opy_ = callback(self, target, exec, bstack11111l1l1l_opy_, result, *args, **kwargs)
                    if bstack1l1l11llll1_opy_ == None:
                        bstack1l1l11llll1_opy_ = bstack1l1l1l11l11_opy_
                except Exception as e:
                    self.logger.error(bstack1l1l111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢ࡬ࡲࡻࡵ࡫ࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࠣᑍ") + str(e) + bstack1l1l111_opy_ (u"ࠦࠧᑎ"))
                    traceback.print_exc()
            if bstack1111ll1l11_opy_ == bstack11111l11l1_opy_.QUIT:
                if bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.POST:
                    bstack1ll1ll11lll_opy_ = bstack11111l1111_opy_.bstack1111l111l1_opy_(instance, EVENTS.bstack1lllll1l11_opy_.value)
                    if bstack1ll1ll11lll_opy_!=None:
                        bstack1llll11ll11_opy_.end(EVENTS.bstack1lllll1l11_opy_.value, bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᑏ"), bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᑐ"), True, None)
            if bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.PRE and callable(bstack1l1l11llll1_opy_):
                return bstack1l1l11llll1_opy_
            elif bstack1l1l1l11111_opy_ == bstack1111llll11_opy_.POST and bstack1l1l11llll1_opy_:
                return bstack1l1l11llll1_opy_
    def bstack1111llll1l_opy_(
        self, method_name, previous_state: bstack11111l11l1_opy_, *args, **kwargs
    ) -> bstack11111l11l1_opy_:
        if method_name == bstack1l1l111_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤᑑ") or method_name == bstack1l1l111_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣᑒ"):
            return bstack11111l11l1_opy_.bstack1111ll1lll_opy_
        if method_name == bstack1l1l111_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᑓ"):
            return bstack11111l11l1_opy_.QUIT
        if method_name == bstack1l1l111_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᑔ"):
            if previous_state != bstack11111l11l1_opy_.NONE:
                bstack1lll11111ll_opy_ = bstack1lll1l11lll_opy_.bstack1l1l1ll1l1l_opy_(*args)
                if bstack1lll11111ll_opy_ == bstack1lll1l11lll_opy_.bstack1l1ll11111l_opy_:
                    return bstack11111l11l1_opy_.bstack1111ll1lll_opy_
            return bstack11111l11l1_opy_.bstack1111ll1ll1_opy_
        return bstack11111l11l1_opy_.NONE