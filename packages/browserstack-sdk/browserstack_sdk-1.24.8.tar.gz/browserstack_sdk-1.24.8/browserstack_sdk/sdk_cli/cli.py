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
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111llllll_opy_ import bstack111l11111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1ll1l_opy_ import bstack1lll11lllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1111_opy_ import bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll11l_opy_ import bstack1lll11l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllll1l11_opy_
from browserstack_sdk.sdk_cli.bstack1llll111lll_opy_ import bstack1lll1lll1ll_opy_
from browserstack_sdk.sdk_cli.bstack111111l1l1_opy_ import bstack1lllllll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l1l_opy_ import bstack1lll1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll1l11111_opy_
from browserstack_sdk.sdk_cli.bstack11lll1l1_opy_ import bstack11lll1l1_opy_, bstack1llll1lll1_opy_, bstack1l11111111_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1llllllll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import bstack11111l1111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lllll_opy_ import bstack1llll11lll1_opy_
from bstack_utils.helper import Notset, bstack1llllllll11_opy_, get_cli_dir, bstack1lll1lll1l1_opy_, bstack11l1l1111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from bstack_utils.helper import Notset, bstack1llllllll11_opy_, get_cli_dir, bstack1lll1lll1l1_opy_, bstack11l1l1111_opy_, bstack1l1l1lll_opy_, bstack11ll1111_opy_, bstack11ll1l11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack111111l111_opy_, bstack1111111l1l_opy_, bstack1lllll11111_opy_, bstack1lllll111ll_opy_
from browserstack_sdk.sdk_cli.bstack1111l1l111_opy_ import bstack1111ll11ll_opy_, bstack11111l11l1_opy_, bstack1111llll11_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1111ll11l_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l1l1ll111_opy_, bstack11ll1ll11l_opy_
logger = bstack1111ll11l_opy_.get_logger(__name__, bstack1111ll11l_opy_.bstack11111111l1_opy_())
def bstack1lll11llll1_opy_(bs_config):
    bstack1lll1ll1l11_opy_ = None
    bstack1llllll111l_opy_ = None
    try:
        bstack1llllll111l_opy_ = get_cli_dir()
        bstack1lll1ll1l11_opy_ = bstack1lll1lll1l1_opy_(bstack1llllll111l_opy_)
        bstack1lll1ll1lll_opy_ = bstack1llllllll11_opy_(bstack1lll1ll1l11_opy_, bstack1llllll111l_opy_, bs_config)
        bstack1lll1ll1l11_opy_ = bstack1lll1ll1lll_opy_ if bstack1lll1ll1lll_opy_ else bstack1lll1ll1l11_opy_
        if not bstack1lll1ll1l11_opy_:
            raise ValueError(bstack1l1l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠨ࿥"))
    except Exception as ex:
        logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡰࡦࡺࡥࡴࡶࠣࡦ࡮ࡴࡡࡳࡻࠣࡿࢂࠨ࿦").format(ex))
        bstack1lll1ll1l11_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠢ࿧"))
        if bstack1lll1ll1l11_opy_:
            logger.debug(bstack1l1l111_opy_ (u"ࠧࡌࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࡀࠠࠣ࿨") + str(bstack1lll1ll1l11_opy_) + bstack1l1l111_opy_ (u"ࠨࠢ࿩"))
        else:
            logger.debug(bstack1l1l111_opy_ (u"ࠢࡏࡱࠣࡺࡦࡲࡩࡥࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸࡀࠦࡳࡦࡶࡸࡴࠥࡳࡡࡺࠢࡥࡩࠥ࡯࡮ࡤࡱࡰࡴࡱ࡫ࡴࡦ࠰ࠥ࿪"))
    return bstack1lll1ll1l11_opy_, bstack1llllll111l_opy_
bstack1lllllll11l_opy_ = bstack1l1l111_opy_ (u"ࠣ࠻࠼࠽࠾ࠨ࿫")
bstack1llllllllll_opy_ = bstack1l1l111_opy_ (u"ࠤࡵࡩࡦࡪࡹࠣ࿬")
bstack1lll11l1l11_opy_ = bstack1l1l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢ࿭")
bstack1llll1l11ll_opy_ = bstack1l1l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡑࡏࡓࡕࡇࡑࡣࡆࡊࡄࡓࠤ࿮")
bstack11llll11l_opy_ = bstack1l1l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣ࿯")
bstack1lll11l11l1_opy_ = re.compile(bstack1l1l111_opy_ (u"ࡸࠢࠩࡁ࡬࠭࠳࠰ࠨࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࢂࡂࡔࠫ࠱࠮ࠧ࿰"))
bstack1llll1lll1l_opy_ = bstack1l1l111_opy_ (u"ࠢࡥࡧࡹࡩࡱࡵࡰ࡮ࡧࡱࡸࠧ࿱")
bstack1lll1lll111_opy_ = [
    bstack1llll1lll1_opy_.bstack1ll111ll11_opy_,
    bstack1llll1lll1_opy_.CONNECT,
    bstack1llll1lll1_opy_.bstack11ll11l1_opy_,
]
class SDKCLI:
    _1lll1ll11ll_opy_ = None
    process: Union[None, Any]
    bstack1lll1l1llll_opy_: bool
    bstack111111ll1l_opy_: bool
    bstack1llll111l11_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1lll1l1111l_opy_: Union[None, grpc.Channel]
    bstack1lllllllll1_opy_: str
    test_framework: TestFramework
    bstack1111l1l111_opy_: bstack11111l1111_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1llll1l1lll_opy_: bstack1lll1l11111_opy_
    accessibility: bstack1lll11lllll_opy_
    ai: bstack1lllll11l11_opy_
    bstack111111llll_opy_: bstack1lll11l1ll1_opy_
    bstack111111111l_opy_: List[bstack1lllll1l111_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1lllll1111l_opy_: Any
    bstack1llll11l111_opy_: Dict[str, timedelta]
    bstack1llll111ll1_opy_: str
    bstack1111llllll_opy_: bstack111l11111l_opy_
    def __new__(cls):
        if not cls._1lll1ll11ll_opy_:
            cls._1lll1ll11ll_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1lll1ll11ll_opy_
    def __init__(self):
        self.process = None
        self.bstack1lll1l1llll_opy_ = False
        self.bstack1lll1l1111l_opy_ = None
        self.bstack1llllll1lll_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1llll1l11ll_opy_, None)
        self.bstack1lllll1l11l_opy_ = os.environ.get(bstack1lll11l1l11_opy_, bstack1l1l111_opy_ (u"ࠣࠤ࿲")) == bstack1l1l111_opy_ (u"ࠤࠥ࿳")
        self.bstack111111ll1l_opy_ = False
        self.bstack1llll111l11_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1lllll1111l_opy_ = None
        self.test_framework = None
        self.bstack1111l1l111_opy_ = None
        self.bstack1lllllllll1_opy_=bstack1l1l111_opy_ (u"ࠥࠦ࿴")
        self.session_framework = None
        self.logger = bstack1111ll11l_opy_.get_logger(self.__class__.__name__, bstack1111ll11l_opy_.bstack11111111l1_opy_())
        self.bstack1llll11l111_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1111llllll_opy_ = bstack111l11111l_opy_()
        self.bstack1lllll1lll1_opy_ = None
        self.bstack111111lll1_opy_ = None
        self.bstack1llll1l1lll_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack111111111l_opy_ = []
    def bstack111l111l1_opy_(self):
        return os.environ.get(bstack11llll11l_opy_).lower().__eq__(bstack1l1l111_opy_ (u"ࠦࡹࡸࡵࡦࠤ࿵"))
    def is_enabled(self, config):
        if bstack1l1l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ࿶") in config and str(config[bstack1l1l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿷")]).lower() != bstack1l1l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭࿸"):
            return False
        bstack1111111111_opy_ = [bstack1l1l111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ࿹"), bstack1l1l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨ࿺")]
        bstack1lllll1llll_opy_ = config.get(bstack1l1l111_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ࿻")) in bstack1111111111_opy_ or os.environ.get(bstack1l1l111_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬ࿼")) in bstack1111111111_opy_
        os.environ[bstack1l1l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣ࿽")] = str(bstack1lllll1llll_opy_) # bstack1lll1llll11_opy_ bstack1lll1l1ll11_opy_ VAR to bstack11111111ll_opy_ is binary running
        return bstack1lllll1llll_opy_
    def bstack1ll11ll11l_opy_(self):
        for event in bstack1lll1lll111_opy_:
            bstack11lll1l1_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack11lll1l1_opy_.logger.debug(bstack1l1l111_opy_ (u"ࠨࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠥࡃ࠾ࠡࡽࡤࡶ࡬ࡹࡽࠡࠤ࿾") + str(kwargs) + bstack1l1l111_opy_ (u"ࠢࠣ࿿"))
            )
        bstack11lll1l1_opy_.register(bstack1llll1lll1_opy_.bstack1ll111ll11_opy_, self.__1lll1l1l1ll_opy_)
        bstack11lll1l1_opy_.register(bstack1llll1lll1_opy_.CONNECT, self.__1llllll1ll1_opy_)
        bstack11lll1l1_opy_.register(bstack1llll1lll1_opy_.bstack11ll11l1_opy_, self.__1lll1llllll_opy_)
        bstack11lll1l1_opy_.register(bstack1llll1lll1_opy_.bstack1l1l1ll1ll_opy_, self.__1lllll11ll1_opy_)
    def bstack1lll1ll1l_opy_(self):
        return not self.bstack1lllll1l11l_opy_ and os.environ.get(bstack1lll11l1l11_opy_, bstack1l1l111_opy_ (u"ࠣࠤက")) != bstack1l1l111_opy_ (u"ࠤࠥခ")
    def is_running(self):
        if self.bstack1lllll1l11l_opy_:
            return self.bstack1lll1l1llll_opy_
        else:
            return bool(self.bstack1lll1l1111l_opy_)
    def bstack1llll11ll1l_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack111111111l_opy_) and cli.is_running()
    def __1lllll111l1_opy_(self, bstack1lllllll111_opy_=10):
        if self.bstack1llllll1lll_opy_:
            return
        bstack1111ll11_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1llll1l11ll_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠥ࡟ࠧဂ") + str(id(self)) + bstack1l1l111_opy_ (u"ࠦࡢࠦࡣࡰࡰࡱࡩࡨࡺࡩ࡯ࡩࠥဃ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1l1l111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠱ࡩࡳࡧࡢ࡭ࡧࡢ࡬ࡹࡺࡰࡠࡲࡵࡳࡽࡿࠢင"), 0), (bstack1l1l111_opy_ (u"ࠨࡧࡳࡲࡦ࠲ࡪࡴࡡࡣ࡮ࡨࡣ࡭ࡺࡴࡱࡵࡢࡴࡷࡵࡸࡺࠤစ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1lllllll111_opy_)
        self.bstack1lll1l1111l_opy_ = channel
        self.bstack1llllll1lll_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1lll1l1111l_opy_)
        self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡩ࡯࡯ࡰࡨࡧࡹࠨဆ"), datetime.now() - bstack1111ll11_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1llll1l11ll_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1l1l111_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦ࠽ࠤ࡮ࡹ࡟ࡤࡪ࡬ࡰࡩࡥࡰࡳࡱࡦࡩࡸࡹ࠽ࠣဇ") + str(self.bstack1lll1ll1l_opy_()) + bstack1l1l111_opy_ (u"ࠤࠥဈ"))
    def __1lll1llllll_opy_(self, event_name):
        if self.bstack1lll1ll1l_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡸࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡃࡍࡋࠥဉ"))
        self.__1lll11ll111_opy_()
    def __1lllll11ll1_opy_(self, event_name, bstack1lll1l1l1l1_opy_ = None, bstack11ll1lll1_opy_=1):
        if bstack11ll1lll1_opy_ == 1:
            self.logger.error(bstack1l1l111_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠦည"))
        bstack1111111lll_opy_ = Path(bstack1llllll1111_opy_ (u"ࠧࢁࡳࡦ࡮ࡩ࠲ࡨࡲࡩࡠࡦ࡬ࡶࢂ࠵ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࡳ࠯࡬ࡶࡳࡳࠨဋ"))
        if self.bstack1llllll111l_opy_ and bstack1111111lll_opy_.exists():
            with open(bstack1111111lll_opy_, bstack1l1l111_opy_ (u"࠭ࡲࠨဌ"), encoding=bstack1l1l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ဍ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠨࡒࡒࡗ࡙࠭ဎ"), bstack11ll1111_opy_(bstack1ll1llllll_opy_), data, {
                        bstack1l1l111_opy_ (u"ࠩࡤࡹࡹ࡮ࠧဏ"): (self.config[bstack1l1l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬတ")], self.config[bstack1l1l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧထ")])
                    })
                except Exception as e:
                    logger.debug(bstack11ll1ll11l_opy_.format(str(e)))
            bstack1111111lll_opy_.unlink()
        sys.exit(bstack11ll1lll1_opy_)
    @measure(event_name=EVENTS.bstack1lllllll1l1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1lll1l1l1ll_opy_(self, event_name: str, data):
        from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
        self.bstack1lllllllll1_opy_, self.bstack1llllll111l_opy_ = bstack1lll11llll1_opy_(data.bs_config)
        os.environ[bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡜ࡘࡉࡕࡃࡅࡐࡊࡥࡄࡊࡔࠪဒ")] = self.bstack1llllll111l_opy_
        if not self.bstack1lllllllll1_opy_ or not self.bstack1llllll111l_opy_:
            raise ValueError(bstack1l1l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡵࡪࡨࠤࡘࡊࡋࠡࡅࡏࡍࠥࡨࡩ࡯ࡣࡵࡽࠧဓ"))
        if self.bstack1lll1ll1l_opy_():
            self.__1llllll1ll1_opy_(event_name, bstack1l11111111_opy_())
            return
        try:
            bstack1llll11ll11_opy_.end(EVENTS.bstack1l111ll1_opy_.value, EVENTS.bstack1l111ll1_opy_.value + bstack1l1l111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢန"), EVENTS.bstack1l111ll1_opy_.value + bstack1l1l111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨပ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1l1l111_opy_ (u"ࠤࡆࡳࡲࡶ࡬ࡦࡶࡨࠤࡘࡊࡋࠡࡕࡨࡸࡺࡶ࠮ࠣဖ"))
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࢀࢃࠢဗ").format(e))
        start = datetime.now()
        is_started = self.__1llll1111l1_opy_()
        self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦࡸࡶࡡࡸࡰࡢࡸ࡮ࡳࡥࠣဘ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1lllll111l1_opy_()
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࡥࡴࡪ࡯ࡨࠦမ"), datetime.now() - start)
            start = datetime.now()
            self.__1lll1lllll1_opy_(data)
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦယ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1lll11ll11l_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1llllll1ll1_opy_(self, event_name: str, data: bstack1l11111111_opy_):
        if not self.bstack1lll1ll1l_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴ࡮ࡦࡥࡷ࠾ࠥࡴ࡯ࡵࠢࡤࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࠦရ"))
            return
        bin_session_id = os.environ.get(bstack1lll11l1l11_opy_)
        start = datetime.now()
        self.__1lllll111l1_opy_()
        self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢလ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1l1l111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨࠥࡺ࡯ࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡇࡑࡏࠠࠣဝ") + str(bin_session_id) + bstack1l1l111_opy_ (u"ࠥࠦသ"))
        start = datetime.now()
        self.__1lll11l1lll_opy_()
        self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤဟ"), datetime.now() - start)
    def __1llll1l1l1l_opy_(self):
        if not self.bstack1llllll1lll_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࠡ࡯ࡲࡨࡺࡲࡥࡴࠤဠ"))
            return
        bstack1llll111l1l_opy_ = {
            bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥအ"): (bstack1lllllll1ll_opy_, bstack1lll1ll11l1_opy_, bstack1llll11lll1_opy_),
            bstack1l1l111_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤဢ"): (bstack1llllll1l11_opy_, bstack1lll1lll1ll_opy_, bstack1lll1l11lll_opy_),
        }
        if not self.bstack1lllll1lll1_opy_ and self.session_framework in bstack1llll111l1l_opy_:
            bstack1lll1l1l11l_opy_, bstack1lllll1l1l1_opy_, bstack1llll1l1ll1_opy_ = bstack1llll111l1l_opy_[self.session_framework]
            bstack1llll1lll11_opy_ = bstack1lllll1l1l1_opy_()
            self.bstack111111lll1_opy_ = bstack1llll1lll11_opy_
            self.bstack1lllll1lll1_opy_ = bstack1llll1l1ll1_opy_
            self.bstack111111111l_opy_.append(bstack1llll1lll11_opy_)
            self.bstack111111111l_opy_.append(bstack1lll1l1l11l_opy_(self.bstack111111lll1_opy_))
        if not self.bstack1llll1l1lll_opy_ and self.config_observability and self.config_observability.success: # bstack1lll11lll11_opy_
            self.bstack1llll1l1lll_opy_ = bstack1lll1l11111_opy_(self.bstack1lllll1lll1_opy_, self.bstack111111lll1_opy_) # bstack1llll11111l_opy_
            self.bstack111111111l_opy_.append(self.bstack1llll1l1lll_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1lll11lllll_opy_(self.bstack1lllll1lll1_opy_, self.bstack111111lll1_opy_)
            self.bstack111111111l_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1l1l111_opy_ (u"ࠣࡵࡨࡰ࡫ࡎࡥࡢ࡮ࠥဣ"), False) == True:
            self.ai = bstack1lllll11l11_opy_()
            self.bstack111111111l_opy_.append(self.ai)
        if not self.percy and self.bstack1lllll1111l_opy_ and self.bstack1lllll1111l_opy_.success:
            self.percy = bstack1lll11l1ll1_opy_(self.bstack1lllll1111l_opy_)
            self.bstack111111111l_opy_.append(self.percy)
        for mod in self.bstack111111111l_opy_:
            if not mod.bstack1llll11l1l1_opy_():
                mod.configure(self.bstack1llllll1lll_opy_, self.config, self.cli_bin_session_id, self.bstack1111llllll_opy_)
    def __1111111ll1_opy_(self):
        for mod in self.bstack111111111l_opy_:
            if mod.bstack1llll11l1l1_opy_():
                mod.configure(self.bstack1llllll1lll_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack111111ll11_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1lll1lllll1_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack111111ll1l_opy_:
            return
        self.__1lll11ll1ll_opy_(data)
        bstack1111ll11_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1l1l111_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤဤ")
        req.sdk_language = bstack1l1l111_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥဥ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1lll11l11l1_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡠࠨဦ") + str(id(self)) + bstack1l1l111_opy_ (u"ࠧࡣࠠ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦဧ"))
            r = self.bstack1llllll1lll_opy_.StartBinSession(req)
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺࡡࡳࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣဨ"), datetime.now() - bstack1111ll11_opy_)
            os.environ[bstack1lll11l1l11_opy_] = r.bin_session_id
            self.__1lllll11l1l_opy_(r)
            self.__1llll1l1l1l_opy_()
            self.bstack1111llllll_opy_.start()
            self.bstack111111ll1l_opy_ = True
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࡜ࠤဩ") + str(id(self)) + bstack1l1l111_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨဪ"))
        except grpc.bstack1llll1111ll_opy_ as bstack1111111l11_opy_:
            self.logger.error(bstack1l1l111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦါ") + str(bstack1111111l11_opy_) + bstack1l1l111_opy_ (u"ࠥࠦာ"))
            traceback.print_exc()
            raise bstack1111111l11_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣိ") + str(e) + bstack1l1l111_opy_ (u"ࠧࠨီ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1ll11l_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1lll11l1lll_opy_(self):
        if not self.bstack1lll1ll1l_opy_() or not self.cli_bin_session_id or self.bstack1llll111l11_opy_:
            return
        bstack1111ll11_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ု"), bstack1l1l111_opy_ (u"ࠧ࠱ࠩူ")))
        try:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣ࡝ࠥေ") + str(id(self)) + bstack1l1l111_opy_ (u"ࠤࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦဲ"))
            r = self.bstack1llllll1lll_opy_.ConnectBinSession(req)
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢဳ"), datetime.now() - bstack1111ll11_opy_)
            self.__1lllll11l1l_opy_(r)
            self.__1llll1l1l1l_opy_()
            self.bstack1111llllll_opy_.start()
            self.bstack1llll111l11_opy_ = True
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡠࠨဴ") + str(id(self)) + bstack1l1l111_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠦဵ"))
        except grpc.bstack1llll1111ll_opy_ as bstack1111111l11_opy_:
            self.logger.error(bstack1l1l111_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡺࡩ࡮ࡧࡲࡩࡺࡺ࠭ࡦࡴࡵࡳࡷࡀࠠࠣံ") + str(bstack1111111l11_opy_) + bstack1l1l111_opy_ (u"့ࠢࠣ"))
            traceback.print_exc()
            raise bstack1111111l11_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧး") + str(e) + bstack1l1l111_opy_ (u"ࠤ္ࠥ"))
            traceback.print_exc()
            raise e
    def __1lllll11l1l_opy_(self, r):
        self.bstack1llll11llll_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1l1l111_opy_ (u"ࠥࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡴࡧࡵࡺࡪࡸࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤ်") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1l1l111_opy_ (u"ࠦࡪࡳࡰࡵࡻࠣࡧࡴࡴࡦࡪࡩࠣࡪࡴࡻ࡮ࡥࠤျ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1l1l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡩࡷࡩࡹࠡ࡫ࡶࠤࡸ࡫࡮ࡵࠢࡲࡲࡱࡿࠠࡢࡵࠣࡴࡦࡸࡴࠡࡱࡩࠤࡹ࡮ࡥࠡࠤࡆࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠲ࠢࠡࡣࡱࡨࠥࡺࡨࡪࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡣ࡯ࡷࡴࠦࡵࡴࡧࡧࠤࡧࡿࠠࡔࡶࡤࡶࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࡳࡧࡩࡳࡷ࡫ࠬࠡࡐࡲࡲࡪࠦࡨࡢࡰࡧࡰ࡮ࡴࡧࠡ࡫ࡶࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢြ")
        self.bstack1lllll1111l_opy_ = getattr(r, bstack1l1l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬွ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫှ")] = self.config_testhub.jwt
        os.environ[bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ဿ")] = self.config_testhub.build_hashed_id
    def bstack1llll1l1111_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1lll1l1llll_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1llllll11ll_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1llllll11ll_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1llll1l1111_opy_(event_name=EVENTS.bstack1lll1ll1111_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1llll1111l1_opy_(self, bstack1lllllll111_opy_=10):
        if self.bstack1lll1l1llll_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡶࡸࡦࡸࡴ࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡶࡺࡴ࡮ࡪࡰࡪࠦ၀"))
            return True
        self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤ၁"))
        if os.getenv(bstack1l1l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡆࡐ࡙ࠦ၂")) == bstack1llll1lll1l_opy_:
            self.cli_bin_session_id = bstack1llll1lll1l_opy_
            self.cli_listen_addr = bstack1l1l111_opy_ (u"ࠧࡻ࡮ࡪࡺ࠽࠳ࡹࡳࡰ࠰ࡵࡧ࡯࠲ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࠦࡵ࠱ࡷࡴࡩ࡫ࠣ၃") % (self.cli_bin_session_id)
            self.bstack1lll1l1llll_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1lllllllll1_opy_, bstack1l1l111_opy_ (u"ࠨࡳࡥ࡭ࠥ၄")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1lll11lll1l_opy_ compat for text=True in bstack1llll111111_opy_ python
            encoding=bstack1l1l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ၅"),
            bufsize=1,
            close_fds=True,
        )
        bstack111111l11l_opy_ = threading.Thread(target=self.__1lllll11lll_opy_, args=(bstack1lllllll111_opy_,))
        bstack111111l11l_opy_.start()
        bstack111111l11l_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡴࡲࡤࡻࡳࡀࠠࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࡁࢀࡹࡥ࡭ࡨ࠱ࡴࡷࡵࡣࡦࡵࡶ࠲ࡷ࡫ࡴࡶࡴࡱࡧࡴࡪࡥࡾࠢࡲࡹࡹࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡳࡵࡦࡲࡹࡹ࠴ࡲࡦࡣࡧࠬ࠮ࢃࠠࡦࡴࡵࡁࠧ၆") + str(self.process.stderr.read()) + bstack1l1l111_opy_ (u"ࠤࠥ၇"))
        if not self.bstack1lll1l1llll_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥ࡟ࠧ၈") + str(id(self)) + bstack1l1l111_opy_ (u"ࠦࡢࠦࡣ࡭ࡧࡤࡲࡺࡶࠢ၉"))
            self.__1lll11ll111_opy_()
        self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡵࡸ࡯ࡤࡧࡶࡷࡤࡸࡥࡢࡦࡼ࠾ࠥࠨ၊") + str(self.bstack1lll1l1llll_opy_) + bstack1l1l111_opy_ (u"ࠨࠢ။"))
        return self.bstack1lll1l1llll_opy_
    def __1lllll11lll_opy_(self, bstack1llll1ll111_opy_=10):
        bstack1lll1l1lll1_opy_ = time.time()
        while self.process and time.time() - bstack1lll1l1lll1_opy_ < bstack1llll1ll111_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1l1l111_opy_ (u"ࠢࡪࡦࡀࠦ၌") in line:
                    self.cli_bin_session_id = line.split(bstack1l1l111_opy_ (u"ࠣ࡫ࡧࡁࠧ၍"))[-1:][0].strip()
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠤࡦࡰ࡮ࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠺ࠣ၎") + str(self.cli_bin_session_id) + bstack1l1l111_opy_ (u"ࠥࠦ၏"))
                    continue
                if bstack1l1l111_opy_ (u"ࠦࡱ࡯ࡳࡵࡧࡱࡁࠧၐ") in line:
                    self.cli_listen_addr = line.split(bstack1l1l111_opy_ (u"ࠧࡲࡩࡴࡶࡨࡲࡂࠨၑ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡣ࡭࡫ࡢࡰ࡮ࡹࡴࡦࡰࡢࡥࡩࡪࡲ࠻ࠤၒ") + str(self.cli_listen_addr) + bstack1l1l111_opy_ (u"ࠢࠣၓ"))
                    continue
                if bstack1l1l111_opy_ (u"ࠣࡲࡲࡶࡹࡃࠢၔ") in line:
                    port = line.split(bstack1l1l111_opy_ (u"ࠤࡳࡳࡷࡺ࠽ࠣၕ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡴࡴࡸࡴ࠻ࠤၖ") + str(port) + bstack1l1l111_opy_ (u"ࠦࠧၗ"))
                    continue
                if line.strip() == bstack1llllllllll_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1l1l111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡎࡕ࡟ࡔࡖࡕࡉࡆࡓࠢၘ"), bstack1l1l111_opy_ (u"ࠨ࠱ࠣၙ")) == bstack1l1l111_opy_ (u"ࠢ࠲ࠤၚ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1lll1l1llll_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡧࡵࡶࡴࡸ࠺ࠡࠤၛ") + str(e) + bstack1l1l111_opy_ (u"ࠤࠥၜ"))
        return False
    @measure(event_name=EVENTS.bstack1llll1ll1l1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def __1lll11ll111_opy_(self):
        if self.bstack1lll1l1111l_opy_:
            self.bstack1111llllll_opy_.stop()
            start = datetime.now()
            if self.bstack1lll1ll111l_opy_():
                self.cli_bin_session_id = None
                if self.bstack1llll111l11_opy_:
                    self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠥࡷࡹࡵࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢၝ"), datetime.now() - start)
                else:
                    self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦࡸࡺ࡯ࡱࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣၞ"), datetime.now() - start)
            self.__1111111ll1_opy_()
            start = datetime.now()
            self.bstack1lll1l1111l_opy_.close()
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠧࡪࡩࡴࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢၟ"), datetime.now() - start)
            self.bstack1lll1l1111l_opy_ = None
        if self.process:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡳࡵࡱࡳࠦၠ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠢ࡬࡫࡯ࡰࡤࡺࡩ࡮ࡧࠥၡ"), datetime.now() - start)
            self.process = None
            if self.bstack1lllll1l11l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l1l111ll_opy_()
                self.logger.info(
                    bstack1l1l111_opy_ (u"ࠣࡘ࡬ࡷ࡮ࡺࠠࡩࡶࡷࡴࡸࡀ࠯࠰ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠦၢ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1l1l111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨၣ")] = self.config_testhub.build_hashed_id
        self.bstack1lll1l1llll_opy_ = False
    def __1lll11ll1ll_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1l1l111_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧၤ")] = selenium.__version__
            data.frameworks.append(bstack1l1l111_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨၥ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1l1l111_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤၦ")] = __version__
            data.frameworks.append(bstack1l1l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥၧ"))
        except:
            pass
    def bstack1lll1llll1l_opy_(self, hub_url: str, platform_index: int, bstack1l1l1l11l_opy_: Any):
        if self.bstack1111l1l111_opy_:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࡥࡱࡸࡥࡢࡦࡼࠤࡸ࡫ࡴࠡࡷࡳࠦၨ"))
            return
        try:
            bstack1111ll11_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1l1l111_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥၩ")
            self.bstack1111l1l111_opy_ = bstack1lll1l11lll_opy_(
                hub_url,
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lll1l11l1l_opy_={bstack1l1l111_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨၪ"): bstack1l1l1l11l_opy_}
            )
            def bstack1lll11l11ll_opy_(self):
                return
            if self.config.get(bstack1l1l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠧၫ"), True):
                Service.start = bstack1lll11l11ll_opy_
                Service.stop = bstack1lll11l11ll_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠧၬ"), datetime.now() - bstack1111ll11_opy_)
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠼ࠣࠦၭ") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢၮ"))
    def bstack1lll1ll1ll1_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1l1lll111_opy_
            self.bstack1111l1l111_opy_ = bstack1llll11lll1_opy_(
                platform_index,
                framework_name=bstack1l1l111_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦၯ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠺ࠡࠤၰ") + str(e) + bstack1l1l111_opy_ (u"ࠤࠥၱ"))
            pass
    def bstack1lllll1l1ll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡴࡾࡺࡥࡴࡶ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡹࡥࡵࠢࡸࡴࠧၲ"))
            return
        if bstack11l1l1111_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1l1l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦၳ"): pytest.__version__ }, [bstack1l1l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤၴ")])
            return
        try:
            import pytest
            self.test_framework = bstack1llllllll1l_opy_({ bstack1l1l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨၵ"): pytest.__version__ }, [bstack1l1l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢၶ")])
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡾࡺࡥࡴࡶ࠽ࠤࠧၷ") + str(e) + bstack1l1l111_opy_ (u"ࠤࠥၸ"))
        self.bstack1llll1l11l1_opy_()
    def bstack1llll1l11l1_opy_(self):
        if not self.bstack111l111l1_opy_():
            return
        bstack1ll11l1l_opy_ = None
        def bstack1ll1llll11_opy_(config, startdir):
            return bstack1l1l111_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣၹ").format(bstack1l1l111_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥၺ"))
        def bstack11llll1l11_opy_():
            return
        def bstack1l1l11ll1_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1l1l111_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬၻ"):
                return bstack1l1l111_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧၼ")
            else:
                return bstack1ll11l1l_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1ll11l1l_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1ll1llll11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11llll1l11_opy_
            Config.getoption = bstack1l1l11ll1_opy_
        except Exception as e:
            self.logger.error(bstack1l1l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡺࡣࡩࠢࡳࡽࡹ࡫ࡳࡵࠢࡶࡩࡱ࡫࡮ࡪࡷࡰࠤ࡫ࡵࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠺ࠡࠤၽ") + str(e) + bstack1l1l111_opy_ (u"ࠣࠤၾ"))
    def bstack1lll1l111ll_opy_(self):
        bstack1lllll1ll11_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1lllll1ll11_opy_, dict):
            if cli.config_observability:
                bstack1lllll1ll11_opy_.update(
                    {bstack1l1l111_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤၿ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1l1l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࡤࡺ࡯ࡠࡹࡵࡥࡵࠨႀ") in accessibility.get(bstack1l1l111_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧႁ"), {}):
                    bstack1llllll11l1_opy_ = accessibility.get(bstack1l1l111_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨႂ"))
                    bstack1llllll11l1_opy_.update({ bstack1l1l111_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠢႃ"): bstack1llllll11l1_opy_.pop(bstack1l1l111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥႄ")) })
                bstack1lllll1ll11_opy_.update({bstack1l1l111_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣႅ"): accessibility })
        return bstack1lllll1ll11_opy_
    @measure(event_name=EVENTS.bstack1lll1l111l1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
    def bstack1lll1ll111l_opy_(self, bstack1llll1llll1_opy_: str = None, bstack1llll11l11l_opy_: str = None, bstack11ll1lll1_opy_: int = None):
        if not self.cli_bin_session_id or not self.bstack1llllll1lll_opy_:
            return
        bstack1111ll11_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if bstack11ll1lll1_opy_:
            req.bstack11ll1lll1_opy_ = bstack11ll1lll1_opy_
        if bstack1llll1llll1_opy_:
            req.bstack1llll1llll1_opy_ = bstack1llll1llll1_opy_
        if bstack1llll11l11l_opy_:
            req.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
        try:
            r = self.bstack1llllll1lll_opy_.StopBinSession(req)
            self.bstack11ll1llll_opy_(bstack1l1l111_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡲࡴࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥႆ"), datetime.now() - bstack1111ll11_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11ll1llll_opy_(self, key: str, value: timedelta):
        tag = bstack1l1l111_opy_ (u"ࠥࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࠥႇ") if self.bstack1lll1ll1l_opy_() else bstack1l1l111_opy_ (u"ࠦࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵࠥႈ")
        self.bstack1llll11l111_opy_[bstack1l1l111_opy_ (u"ࠧࡀࠢႉ").join([tag + bstack1l1l111_opy_ (u"ࠨ࠭ࠣႊ") + str(id(self)), key])] += value
    def bstack1l1l111ll_opy_(self):
        if not os.getenv(bstack1l1l111_opy_ (u"ࠢࡅࡇࡅ࡙ࡌࡥࡐࡆࡔࡉࠦႋ"), bstack1l1l111_opy_ (u"ࠣ࠲ࠥႌ")) == bstack1l1l111_opy_ (u"ࠤ࠴ႍࠦ"):
            return
        bstack1lll11l111l_opy_ = dict()
        bstack1111lll11l_opy_ = []
        if self.test_framework:
            bstack1111lll11l_opy_.extend(list(self.test_framework.bstack1111lll11l_opy_.values()))
        if self.bstack1111l1l111_opy_:
            bstack1111lll11l_opy_.extend(list(self.bstack1111l1l111_opy_.bstack1111lll11l_opy_.values()))
        for instance in bstack1111lll11l_opy_:
            if not instance.platform_index in bstack1lll11l111l_opy_:
                bstack1lll11l111l_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1lll11l111l_opy_[instance.platform_index]
            for k, v in instance.bstack1llll1l111l_opy_().items():
                report[k] += v
                report[k.split(bstack1l1l111_opy_ (u"ࠥ࠾ࠧႎ"))[0]] += v
        bstack1lllll1ll1l_opy_ = sorted([(k, v) for k, v in self.bstack1llll11l111_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1lll1l11ll1_opy_ = 0
        for r in bstack1lllll1ll1l_opy_:
            bstack1lll11l1l1l_opy_ = r[1].total_seconds()
            bstack1lll1l11ll1_opy_ += bstack1lll11l1l1l_opy_
            self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡨࡲࡩ࠻ࡽࡵ࡟࠵ࡣࡽ࠾ࠤႏ") + str(bstack1lll11l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠧࠨ႐"))
        self.logger.debug(bstack1l1l111_opy_ (u"ࠨ࠭࠮ࠤ႑"))
        bstack111111l1ll_opy_ = []
        for platform_index, report in bstack1lll11l111l_opy_.items():
            bstack111111l1ll_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack111111l1ll_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1l1l11l111_opy_ = set()
        bstack1llllll1l1l_opy_ = 0
        for r in bstack111111l1ll_opy_:
            bstack1lll11l1l1l_opy_ = r[2].total_seconds()
            bstack1llllll1l1l_opy_ += bstack1lll11l1l1l_opy_
            bstack1l1l11l111_opy_.add(r[0])
            self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡵࡧࡶࡸ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࡼࡴ࡞࠴ࡢࢃ࠺ࡼࡴ࡞࠵ࡢࢃ࠽ࠣ႒") + str(bstack1lll11l1l1l_opy_) + bstack1l1l111_opy_ (u"ࠣࠤ႓"))
        if self.bstack1lll1ll1l_opy_():
            self.logger.debug(bstack1l1l111_opy_ (u"ࠤ࠰࠱ࠧ႔"))
            self.logger.debug(bstack1l1l111_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺ࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠽ࡼࡶࡲࡸࡦࡲ࡟ࡤ࡮࡬ࢁࠥࡺࡥࡴࡶ࠽ࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠳ࡻࡴࡶࡵࠬࡵࡲࡡࡵࡨࡲࡶࡲࡹࠩࡾ࠿ࠥ႕") + str(bstack1llllll1l1l_opy_) + bstack1l1l111_opy_ (u"ࠦࠧ႖"))
        else:
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠾ࠤ႗") + str(bstack1lll1l11ll1_opy_) + bstack1l1l111_opy_ (u"ࠨࠢ႘"))
        self.logger.debug(bstack1l1l111_opy_ (u"ࠢ࠮࠯ࠥ႙"))
    def bstack1llll11llll_opy_(self, r):
        if r is not None and getattr(r, bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࠩႚ"), None) and getattr(r.testhub, bstack1l1l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩႛ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1l1l111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤႜ")))
            for bstack1llll11l1ll_opy_, err in errors.items():
                if err[bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩႝ")] == bstack1l1l111_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ႞"):
                    self.logger.info(err[bstack1l1l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ႟")])
                else:
                    self.logger.error(err[bstack1l1l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨႠ")])
cli = SDKCLI()