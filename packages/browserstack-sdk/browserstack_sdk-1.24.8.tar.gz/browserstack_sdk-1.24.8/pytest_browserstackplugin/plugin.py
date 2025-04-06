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
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1111l1ll1_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack111l11l1_opy_, bstack1llllll1l1_opy_, update, bstack1l1l1l11l_opy_,
                                       bstack1ll1llll11_opy_, bstack11llll1l11_opy_, bstack11ll1l1ll1_opy_, bstack1l11l11ll_opy_,
                                       bstack11l111l1_opy_, bstack11l1l1ll1_opy_, bstack1l111111l1_opy_, bstack11l1111ll_opy_,
                                       bstack1ll1ll111l_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11llll111l_opy_)
from browserstack_sdk.bstack11llll111_opy_ import bstack1l11l111_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1111ll11l_opy_
from bstack_utils.capture import bstack11l11lll1l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack11ll11l11l_opy_, bstack1lllll11l1_opy_, bstack1l1l1111ll_opy_, \
    bstack1l1l11ll11_opy_
from bstack_utils.helper import bstack1l11ll111l_opy_, bstack11ll11lllll_opy_, bstack111ll1111l_opy_, bstack1ll111lll1_opy_, bstack1ll111111l1_opy_, bstack1ll11l1ll1_opy_, \
    bstack11ll1l1ll11_opy_, \
    bstack11lllll1l1l_opy_, bstack11l1lllll_opy_, bstack11l1l1llll_opy_, bstack11lllll111l_opy_, bstack11l1l1111_opy_, Notset, \
    bstack1lll1l1l1_opy_, bstack11llll1ll1l_opy_, bstack11ll1l1l1l1_opy_, Result, bstack11lll11ll1l_opy_, bstack11lll11l1l1_opy_, bstack111lllll1l_opy_, \
    bstack1ll1l1l1l_opy_, bstack111l111ll_opy_, bstack11l1l1l1l1_opy_, bstack11lllll1ll1_opy_
from bstack_utils.bstack11ll11ll111_opy_ import bstack11ll11l111l_opy_
from bstack_utils.messages import bstack1l1llllll1_opy_, bstack1ll1l1l11l_opy_, bstack1l1lll1ll1_opy_, bstack11l1111l1_opy_, bstack11ll1111l1_opy_, \
    bstack11111l1ll_opy_, bstack1l1111l1_opy_, bstack1ll111l1l_opy_, bstack11ll11llll_opy_, bstack1l1lll11l_opy_, \
    bstack1l111lll_opy_, bstack1l111111l_opy_
from bstack_utils.proxy import bstack11lll11l_opy_, bstack1l11ll1l_opy_
from bstack_utils.bstack1l1l1lll11_opy_ import bstack11l1111ll11_opy_, bstack11l11111lll_opy_, bstack11l11111l11_opy_, bstack11l1111l1ll_opy_, \
    bstack11l111111l1_opy_, bstack11l11111ll1_opy_, bstack11l1111lll1_opy_, bstack111llll11_opy_, bstack11l11111l1l_opy_
from bstack_utils.bstack11lll1l1l1_opy_ import bstack1l1l11111l_opy_
from bstack_utils.bstack11l1lllll1_opy_ import bstack1ll1l1l1l1_opy_, bstack1ll1ll1ll1_opy_, bstack1l1l1ll11l_opy_, \
    bstack11ll111111_opy_, bstack11l1l1lll1_opy_
from bstack_utils.bstack11l11lllll_opy_ import bstack11l1l11l1l_opy_
from bstack_utils.bstack11l11ll1ll_opy_ import bstack1l1lll1lll_opy_
import bstack_utils.accessibility as bstack11l1l1lll_opy_
from bstack_utils.bstack11l11l1l1l_opy_ import bstack1l11l11lll_opy_
from bstack_utils.bstack11l1l1ll1l_opy_ import bstack11l1l1ll1l_opy_
from browserstack_sdk.__init__ import bstack1lll11llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll1l11111_opy_
from browserstack_sdk.sdk_cli.bstack11lll1l1_opy_ import bstack11lll1l1_opy_, bstack1llll1lll1_opy_, bstack1l11111111_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1l11l1lllll_opy_, bstack111111l111_opy_, bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11lll1l1_opy_ import bstack11lll1l1_opy_, bstack1llll1lll1_opy_, bstack1l11111111_opy_
bstack11lllllll_opy_ = None
bstack11lll1ll1l_opy_ = None
bstack1ll11l111l_opy_ = None
bstack1l1llll1_opy_ = None
bstack11ll11ll11_opy_ = None
bstack11l1lll1l_opy_ = None
bstack1lllll1ll1_opy_ = None
bstack1l1l1l1l_opy_ = None
bstack1ll1lll1l_opy_ = None
bstack1ll1l111l1_opy_ = None
bstack1ll11l1l_opy_ = None
bstack1lllllll11_opy_ = None
bstack1ll11lll11_opy_ = None
bstack111l111l_opy_ = bstack1l1l111_opy_ (u"ࠪࠫḬ")
CONFIG = {}
bstack1l11l1l11l_opy_ = False
bstack11l1llll_opy_ = bstack1l1l111_opy_ (u"ࠫࠬḭ")
bstack1111ll1l_opy_ = bstack1l1l111_opy_ (u"ࠬ࠭Ḯ")
bstack1ll1l1lll_opy_ = False
bstack1111l11l1_opy_ = []
bstack111ll1l1_opy_ = bstack11ll11l11l_opy_
bstack111l1l1l111_opy_ = bstack1l1l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ḯ")
bstack111l1l1l1_opy_ = {}
bstack11ll111l1l_opy_ = None
bstack1l11ll1l1_opy_ = False
logger = bstack1111ll11l_opy_.get_logger(__name__, bstack111ll1l1_opy_)
store = {
    bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫḰ"): []
}
bstack111l1l1lll1_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_111ll11ll1_opy_ = {}
current_test_uuid = None
cli_context = bstack1l11l1lllll_opy_(
    test_framework_name=bstack1l11llll11_opy_[bstack1l1l111_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔ࠮ࡄࡇࡈࠬḱ")] if bstack11l1l1111_opy_() else bstack1l11llll11_opy_[bstack1l1l111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩḲ")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1l111l111_opy_(page, bstack1l1l1l11_opy_):
    try:
        page.evaluate(bstack1l1l111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦḳ"),
                      bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨḴ") + json.dumps(
                          bstack1l1l1l11_opy_) + bstack1l1l111_opy_ (u"ࠧࢃࡽࠣḵ"))
    except Exception as e:
        print(bstack1l1l111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦḶ"), e)
def bstack1ll1l1ll1l_opy_(page, message, level):
    try:
        page.evaluate(bstack1l1l111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣḷ"), bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭Ḹ") + json.dumps(
            message) + bstack1l1l111_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬḹ") + json.dumps(level) + bstack1l1l111_opy_ (u"ࠪࢁࢂ࠭Ḻ"))
    except Exception as e:
        print(bstack1l1l111_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢḻ"), e)
def pytest_configure(config):
    global bstack11l1llll_opy_
    global CONFIG
    bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
    config.args = bstack1l1lll1lll_opy_.bstack111l1ll111l_opy_(config.args)
    bstack111l11l1l_opy_.bstack11llll1ll_opy_(bstack11l1l1l1l1_opy_(config.getoption(bstack1l1l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩḼ"))))
    try:
        bstack1111ll11l_opy_.bstack11ll11111l1_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack11lll1l1_opy_.invoke(bstack1llll1lll1_opy_.CONNECT, bstack1l11111111_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ḽ"), bstack1l1l111_opy_ (u"ࠧ࠱ࠩḾ")))
        config = json.loads(os.environ.get(bstack1l1l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠢḿ"), bstack1l1l111_opy_ (u"ࠤࡾࢁࠧṀ")))
        cli.bstack1lll1llll1l_opy_(bstack11l1l1llll_opy_(bstack11l1llll_opy_, CONFIG), cli_context.platform_index, bstack1l1l1l11l_opy_)
    if cli.bstack1llll11ll1l_opy_(bstack1lll1l11111_opy_):
        cli.bstack1lllll1l1ll_opy_()
        logger.debug(bstack1l1l111_opy_ (u"ࠥࡇࡑࡏࠠࡪࡵࠣࡥࡨࡺࡩࡷࡧࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤṁ") + str(cli_context.platform_index) + bstack1l1l111_opy_ (u"ࠦࠧṂ"))
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.BEFORE_ALL, bstack1lllll11111_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack1l1l111_opy_ (u"ࠧࡽࡨࡦࡰࠥṃ"), None)
    if cli.is_running() and when == bstack1l1l111_opy_ (u"ࠨࡣࡢ࡮࡯ࠦṄ"):
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.LOG_REPORT, bstack1lllll11111_opy_.PRE, item, call)
    outcome = yield
    if cli.is_running():
        if when == bstack1l1l111_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨṅ"):
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.BEFORE_EACH, bstack1lllll11111_opy_.POST, item, call, outcome)
        elif when == bstack1l1l111_opy_ (u"ࠣࡥࡤࡰࡱࠨṆ"):
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.LOG_REPORT, bstack1lllll11111_opy_.POST, item, call, outcome)
        elif when == bstack1l1l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦṇ"):
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.AFTER_EACH, bstack1lllll11111_opy_.POST, item, call, outcome)
        return # skip all existing bstack111l1l1l1ll_opy_
    bstack111l1l11l1l_opy_ = item.config.getoption(bstack1l1l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬṈ"))
    plugins = item.config.getoption(bstack1l1l111_opy_ (u"ࠦࡵࡲࡵࡨ࡫ࡱࡷࠧṉ"))
    report = outcome.get_result()
    bstack111l1l11lll_opy_(item, call, report)
    if bstack1l1l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠥṊ") not in plugins or bstack11l1l1111_opy_():
        return
    summary = []
    driver = getattr(item, bstack1l1l111_opy_ (u"ࠨ࡟ࡥࡴ࡬ࡺࡪࡸࠢṋ"), None)
    page = getattr(item, bstack1l1l111_opy_ (u"ࠢࡠࡲࡤ࡫ࡪࠨṌ"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack111l11ll11l_opy_(item, report, summary, bstack111l1l11l1l_opy_)
    if (page is not None):
        bstack111l11lll1l_opy_(item, report, summary, bstack111l1l11l1l_opy_)
def bstack111l11ll11l_opy_(item, report, summary, bstack111l1l11l1l_opy_):
    if report.when == bstack1l1l111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧṍ") and report.skipped:
        bstack11l11111l1l_opy_(report)
    if report.when in [bstack1l1l111_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣṎ"), bstack1l1l111_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧṏ")]:
        return
    if not bstack1ll111111l1_opy_():
        return
    try:
        if (str(bstack111l1l11l1l_opy_).lower() != bstack1l1l111_opy_ (u"ࠫࡹࡸࡵࡦࠩṐ") and not cli.is_running()):
            item._driver.execute_script(
                bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪṑ") + json.dumps(
                    report.nodeid) + bstack1l1l111_opy_ (u"࠭ࡽࡾࠩṒ"))
        os.environ[bstack1l1l111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪṓ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1l1l111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧ࠽ࠤࢀ࠶ࡽࠣṔ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1l111_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦṕ")))
    bstack1ll1lll1ll_opy_ = bstack1l1l111_opy_ (u"ࠥࠦṖ")
    bstack11l11111l1l_opy_(report)
    if not passed:
        try:
            bstack1ll1lll1ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1l1l111_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦṗ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll1lll1ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1l1l111_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢṘ")))
        bstack1ll1lll1ll_opy_ = bstack1l1l111_opy_ (u"ࠨࠢṙ")
        if not passed:
            try:
                bstack1ll1lll1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1l111_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢṚ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll1lll1ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬṛ")
                    + json.dumps(bstack1l1l111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠣࠥṜ"))
                    + bstack1l1l111_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨṝ")
                )
            else:
                item._driver.execute_script(
                    bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩṞ")
                    + json.dumps(str(bstack1ll1lll1ll_opy_))
                    + bstack1l1l111_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣṟ")
                )
        except Exception as e:
            summary.append(bstack1l1l111_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡦࡴ࡮ࡰࡶࡤࡸࡪࡀࠠࡼ࠲ࢀࠦṠ").format(e))
def bstack111l11lll11_opy_(test_name, error_message):
    try:
        bstack111l11l11l1_opy_ = []
        bstack1l11ll11l_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧṡ"), bstack1l1l111_opy_ (u"ࠨ࠲ࠪṢ"))
        bstack11ll11ll1_opy_ = {bstack1l1l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧṣ"): test_name, bstack1l1l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩṤ"): error_message, bstack1l1l111_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪṥ"): bstack1l11ll11l_opy_}
        bstack111l11llll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠬࡶࡷࡠࡲࡼࡸࡪࡹࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪṦ"))
        if os.path.exists(bstack111l11llll1_opy_):
            with open(bstack111l11llll1_opy_) as f:
                bstack111l11l11l1_opy_ = json.load(f)
        bstack111l11l11l1_opy_.append(bstack11ll11ll1_opy_)
        with open(bstack111l11llll1_opy_, bstack1l1l111_opy_ (u"࠭ࡷࠨṧ")) as f:
            json.dump(bstack111l11l11l1_opy_, f)
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡩࡷࡹࡩࡴࡶ࡬ࡲ࡬ࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡴࡾࡺࡥࡴࡶࠣࡩࡷࡸ࡯ࡳࡵ࠽ࠤࠬṨ") + str(e))
def bstack111l11lll1l_opy_(item, report, summary, bstack111l1l11l1l_opy_):
    if report.when in [bstack1l1l111_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢṩ"), bstack1l1l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦṪ")]:
        return
    if (str(bstack111l1l11l1l_opy_).lower() != bstack1l1l111_opy_ (u"ࠪࡸࡷࡻࡥࠨṫ")):
        bstack1l111l111_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1l111_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨṬ")))
    bstack1ll1lll1ll_opy_ = bstack1l1l111_opy_ (u"ࠧࠨṭ")
    bstack11l11111l1l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1ll1lll1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1l111_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨṮ").format(e)
                )
        try:
            if passed:
                bstack11l1l1lll1_opy_(getattr(item, bstack1l1l111_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭ṯ"), None), bstack1l1l111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣṰ"))
            else:
                error_message = bstack1l1l111_opy_ (u"ࠩࠪṱ")
                if bstack1ll1lll1ll_opy_:
                    bstack1ll1l1ll1l_opy_(item._page, str(bstack1ll1lll1ll_opy_), bstack1l1l111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤṲ"))
                    bstack11l1l1lll1_opy_(getattr(item, bstack1l1l111_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪṳ"), None), bstack1l1l111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧṴ"), str(bstack1ll1lll1ll_opy_))
                    error_message = str(bstack1ll1lll1ll_opy_)
                else:
                    bstack11l1l1lll1_opy_(getattr(item, bstack1l1l111_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬṵ"), None), bstack1l1l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢṶ"))
                bstack111l11lll11_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1l1l111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽ࠳ࢁࠧṷ").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack1l1l111_opy_ (u"ࠤ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨṸ"), default=bstack1l1l111_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤṹ"), help=bstack1l1l111_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡩࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠥṺ"))
    parser.addoption(bstack1l1l111_opy_ (u"ࠧ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦṻ"), default=bstack1l1l111_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧṼ"), help=bstack1l1l111_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡥࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠨṽ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1l1l111_opy_ (u"ࠣ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠥṾ"), action=bstack1l1l111_opy_ (u"ࠤࡶࡸࡴࡸࡥࠣṿ"), default=bstack1l1l111_opy_ (u"ࠥࡧ࡭ࡸ࡯࡮ࡧࠥẀ"),
                         help=bstack1l1l111_opy_ (u"ࠦࡉࡸࡩࡷࡧࡵࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵࠥẁ"))
def bstack11l1l111l1_opy_(log):
    if not (log[bstack1l1l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ẃ")] and log[bstack1l1l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧẃ")].strip()):
        return
    active = bstack11l11l1ll1_opy_()
    log = {
        bstack1l1l111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭Ẅ"): log[bstack1l1l111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧẅ")],
        bstack1l1l111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬẆ"): bstack111ll1111l_opy_().isoformat() + bstack1l1l111_opy_ (u"ࠪ࡞ࠬẇ"),
        bstack1l1l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬẈ"): log[bstack1l1l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ẉ")],
    }
    if active:
        if active[bstack1l1l111_opy_ (u"࠭ࡴࡺࡲࡨࠫẊ")] == bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࠬẋ"):
            log[bstack1l1l111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨẌ")] = active[bstack1l1l111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩẍ")]
        elif active[bstack1l1l111_opy_ (u"ࠪࡸࡾࡶࡥࠨẎ")] == bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࠩẏ"):
            log[bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬẐ")] = active[bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ẑ")]
    bstack1l11l11lll_opy_.bstack11l11lll1_opy_([log])
def bstack11l11l1ll1_opy_():
    if len(store[bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫẒ")]) > 0 and store[bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬẓ")][-1]:
        return {
            bstack1l1l111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧẔ"): bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨẕ"),
            bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫẖ"): store[bstack1l1l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩẗ")][-1]
        }
    if store.get(bstack1l1l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪẘ"), None):
        return {
            bstack1l1l111_opy_ (u"ࠧࡵࡻࡳࡩࠬẙ"): bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹ࠭ẚ"),
            bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩẛ"): store[bstack1l1l111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧẜ")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.INIT_TEST, bstack1lllll11111_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.INIT_TEST, bstack1lllll11111_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._111l11ll1l1_opy_ = True
        bstack1ll1111l1_opy_ = bstack11l1l1lll_opy_.bstack1l1l1l1ll_opy_(bstack11lllll1l1l_opy_(item.own_markers))
        if not cli.bstack1llll11ll1l_opy_(bstack1lll1l11111_opy_):
            item._a11y_test_case = bstack1ll1111l1_opy_
            if bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪẝ"), None):
                driver = getattr(item, bstack1l1l111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ẞ"), None)
                item._a11y_started = bstack11l1l1lll_opy_.bstack1l111ll11l_opy_(driver, bstack1ll1111l1_opy_)
        if not bstack1l11l11lll_opy_.on() or bstack111l1l1l111_opy_ != bstack1l1l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ẟ"):
            return
        global current_test_uuid #, bstack11l11l1111_opy_
        bstack111lll1l11_opy_ = {
            bstack1l1l111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬẠ"): uuid4().__str__(),
            bstack1l1l111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬạ"): bstack111ll1111l_opy_().isoformat() + bstack1l1l111_opy_ (u"ࠩ࡝ࠫẢ")
        }
        current_test_uuid = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨả")]
        store[bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨẤ")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠬࡻࡵࡪࡦࠪấ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _111ll11ll1_opy_[item.nodeid] = {**_111ll11ll1_opy_[item.nodeid], **bstack111lll1l11_opy_}
        bstack111l1l1ll1l_opy_(item, _111ll11ll1_opy_[item.nodeid], bstack1l1l111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧẦ"))
    except Exception as err:
        print(bstack1l1l111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡤࡣ࡯ࡰ࠿ࠦࡻࡾࠩầ"), str(err))
def pytest_runtest_setup(item):
    store[bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬẨ")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.BEFORE_EACH, bstack1lllll11111_opy_.PRE, item, bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨẩ"))
        return # skip all existing bstack111l1l1l1ll_opy_
    global bstack111l1l1lll1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11lllll111l_opy_():
        atexit.register(bstack1ll111l11l_opy_)
        if not bstack111l1l1lll1_opy_:
            try:
                bstack111l11l1l11_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11lllll1ll1_opy_():
                    bstack111l11l1l11_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack111l11l1l11_opy_:
                    signal.signal(s, bstack111l11lllll_opy_)
                bstack111l1l1lll1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡨ࡫ࡶࡸࡪࡸࠠࡴ࡫ࡪࡲࡦࡲࠠࡩࡣࡱࡨࡱ࡫ࡲࡴ࠼ࠣࠦẪ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l1111ll11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1l1l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫẫ")
    try:
        if not bstack1l11l11lll_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack111lll1l11_opy_ = {
            bstack1l1l111_opy_ (u"ࠬࡻࡵࡪࡦࠪẬ"): uuid,
            bstack1l1l111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪậ"): bstack111ll1111l_opy_().isoformat() + bstack1l1l111_opy_ (u"࡛ࠧࠩẮ"),
            bstack1l1l111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ắ"): bstack1l1l111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧẰ"),
            bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ằ"): bstack1l1l111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩẲ"),
            bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨẳ"): bstack1l1l111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬẴ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫẵ")] = item
        store[bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬẶ")] = [uuid]
        if not _111ll11ll1_opy_.get(item.nodeid, None):
            _111ll11ll1_opy_[item.nodeid] = {bstack1l1l111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨặ"): [], bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬẸ"): []}
        _111ll11ll1_opy_[item.nodeid][bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪẹ")].append(bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠬࡻࡵࡪࡦࠪẺ")])
        _111ll11ll1_opy_[item.nodeid + bstack1l1l111_opy_ (u"࠭࠭ࡴࡧࡷࡹࡵ࠭ẻ")] = bstack111lll1l11_opy_
        bstack111l1l111ll_opy_(item, bstack111lll1l11_opy_, bstack1l1l111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨẼ"))
    except Exception as err:
        print(bstack1l1l111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫẽ"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.AFTER_EACH, bstack1lllll11111_opy_.PRE, item, bstack1l1l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫẾ"))
        return # skip all existing bstack111l1l1l1ll_opy_
    try:
        global bstack111l1l1l1_opy_
        bstack1l11ll11l_opy_ = 0
        if bstack1ll1l1lll_opy_ is True:
            bstack1l11ll11l_opy_ = int(os.environ.get(bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪế")))
        if bstack1lll1l1l1l_opy_.bstack1llll11lll_opy_() == bstack1l1l111_opy_ (u"ࠦࡹࡸࡵࡦࠤỀ"):
            if bstack1lll1l1l1l_opy_.bstack11llllll1_opy_() == bstack1l1l111_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢề"):
                bstack111l1l111l1_opy_ = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩỂ"), None)
                bstack1l1lll1l_opy_ = bstack111l1l111l1_opy_ + bstack1l1l111_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥể")
                driver = getattr(item, bstack1l1l111_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩỄ"), None)
                bstack1l1lll11ll_opy_ = getattr(item, bstack1l1l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧễ"), None)
                bstack1l1111ll_opy_ = getattr(item, bstack1l1l111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨỆ"), None)
                PercySDK.screenshot(driver, bstack1l1lll1l_opy_, bstack1l1lll11ll_opy_=bstack1l1lll11ll_opy_, bstack1l1111ll_opy_=bstack1l1111ll_opy_, bstack1l111l1ll1_opy_=bstack1l11ll11l_opy_)
        if not cli.bstack1llll11ll1l_opy_(bstack1lll1l11111_opy_):
            if getattr(item, bstack1l1l111_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡧࡲࡵࡧࡧࠫệ"), False):
                bstack1l11l111_opy_.bstack111ll1lll_opy_(getattr(item, bstack1l1l111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭Ỉ"), None), bstack111l1l1l1_opy_, logger, item)
        if not bstack1l11l11lll_opy_.on():
            return
        bstack111lll1l11_opy_ = {
            bstack1l1l111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫỉ"): uuid4().__str__(),
            bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫỊ"): bstack111ll1111l_opy_().isoformat() + bstack1l1l111_opy_ (u"ࠨ࡜ࠪị"),
            bstack1l1l111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧỌ"): bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨọ"),
            bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧỎ"): bstack1l1l111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩỏ"),
            bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩỐ"): bstack1l1l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩố")
        }
        _111ll11ll1_opy_[item.nodeid + bstack1l1l111_opy_ (u"ࠨ࠯ࡷࡩࡦࡸࡤࡰࡹࡱࠫỒ")] = bstack111lll1l11_opy_
        bstack111l1l111ll_opy_(item, bstack111lll1l11_opy_, bstack1l1l111_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪồ"))
    except Exception as err:
        print(bstack1l1l111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲ࠿ࠦࡻࡾࠩỔ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l1111l1ll_opy_(fixturedef.argname):
        store[bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪổ")] = request.node
    elif bstack11l111111l1_opy_(fixturedef.argname):
        store[bstack1l1l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪỖ")] = request.node
    if not bstack1l11l11lll_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.SETUP_FIXTURE, bstack1lllll11111_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.SETUP_FIXTURE, bstack1lllll11111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack111l1l1l1ll_opy_
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.SETUP_FIXTURE, bstack1lllll11111_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.SETUP_FIXTURE, bstack1lllll11111_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack111l1l1l1ll_opy_
    try:
        fixture = {
            bstack1l1l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫỗ"): fixturedef.argname,
            bstack1l1l111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧỘ"): bstack11ll1l1ll11_opy_(outcome),
            bstack1l1l111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪộ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1l1l111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭Ớ")]
        if not _111ll11ll1_opy_.get(current_test_item.nodeid, None):
            _111ll11ll1_opy_[current_test_item.nodeid] = {bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬớ"): []}
        _111ll11ll1_opy_[current_test_item.nodeid][bstack1l1l111_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭Ờ")].append(fixture)
    except Exception as err:
        logger.debug(bstack1l1l111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨờ"), str(err))
if bstack11l1l1111_opy_() and bstack1l11l11lll_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.STEP, bstack1lllll11111_opy_.PRE, request, step)
            return
        try:
            _111ll11ll1_opy_[request.node.nodeid][bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩỞ")].bstack1ll1l1ll1_opy_(id(step))
        except Exception as err:
            print(bstack1l1l111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬở"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.STEP, bstack1lllll11111_opy_.POST, request, step, exception)
            return
        try:
            _111ll11ll1_opy_[request.node.nodeid][bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫỠ")].bstack11l11l1lll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1l1l111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭ỡ"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_.STEP, bstack1lllll11111_opy_.POST, request, step)
            return
        try:
            bstack11l11lllll_opy_: bstack11l1l11l1l_opy_ = _111ll11ll1_opy_[request.node.nodeid][bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭Ợ")]
            bstack11l11lllll_opy_.bstack11l11l1lll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1l1l111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨợ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack111l1l1l111_opy_
        try:
            if not bstack1l11l11lll_opy_.on() or bstack111l1l1l111_opy_ != bstack1l1l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩỤ"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack111111l111_opy_.TEST, bstack1lllll11111_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬụ"), None)
            if not _111ll11ll1_opy_.get(request.node.nodeid, None):
                _111ll11ll1_opy_[request.node.nodeid] = {}
            bstack11l11lllll_opy_ = bstack11l1l11l1l_opy_.bstack111lll11l1l_opy_(
                scenario, feature, request.node,
                name=bstack11l11111ll1_opy_(request.node, scenario),
                started_at=bstack1ll11l1ll1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1l1l111_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩỦ"),
                tags=bstack11l1111lll1_opy_(feature, scenario),
                bstack11l111llll_opy_=bstack1l11l11lll_opy_.bstack11l111ll1l_opy_(driver) if driver and driver.session_id else {}
            )
            _111ll11ll1_opy_[request.node.nodeid][bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫủ")] = bstack11l11lllll_opy_
            bstack111l1l11111_opy_(bstack11l11lllll_opy_.uuid)
            bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪỨ"), bstack11l11lllll_opy_)
        except Exception as err:
            print(bstack1l1l111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬứ"), str(err))
def bstack111l11l11ll_opy_(bstack11l1l111ll_opy_):
    if bstack11l1l111ll_opy_ in store[bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨỪ")]:
        store[bstack1l1l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩừ")].remove(bstack11l1l111ll_opy_)
def bstack111l1l11111_opy_(test_uuid):
    store[bstack1l1l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪỬ")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l11l11lll_opy_.bstack111ll1ll1l1_opy_
def bstack111l1l11lll_opy_(item, call, report):
    logger.debug(bstack1l1l111_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡲࡵࠩử"))
    global bstack111l1l1l111_opy_
    bstack111l11111_opy_ = bstack1ll11l1ll1_opy_()
    if hasattr(report, bstack1l1l111_opy_ (u"ࠨࡵࡷࡳࡵ࠭Ữ")):
        bstack111l11111_opy_ = bstack11lll11ll1l_opy_(report.stop)
    elif hasattr(report, bstack1l1l111_opy_ (u"ࠩࡶࡸࡦࡸࡴࠨữ")):
        bstack111l11111_opy_ = bstack11lll11ll1l_opy_(report.start)
    try:
        if getattr(report, bstack1l1l111_opy_ (u"ࠪࡻ࡭࡫࡮ࠨỰ"), bstack1l1l111_opy_ (u"ࠫࠬự")) == bstack1l1l111_opy_ (u"ࠬࡩࡡ࡭࡮ࠪỲ"):
            logger.debug(bstack1l1l111_opy_ (u"࠭ࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡶࡸࡦࡺࡥࠡ࠯ࠣࡿࢂ࠲ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࠱ࠥࢁࡽࠨỳ").format(getattr(report, bstack1l1l111_opy_ (u"ࠧࡸࡪࡨࡲࠬỴ"), bstack1l1l111_opy_ (u"ࠨࠩỵ")).__str__(), bstack111l1l1l111_opy_))
            if bstack111l1l1l111_opy_ == bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩỶ"):
                _111ll11ll1_opy_[item.nodeid][bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨỷ")] = bstack111l11111_opy_
                bstack111l1l1ll1l_opy_(item, _111ll11ll1_opy_[item.nodeid], bstack1l1l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ỹ"), report, call)
                store[bstack1l1l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩỹ")] = None
            elif bstack111l1l1l111_opy_ == bstack1l1l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥỺ"):
                bstack11l11lllll_opy_ = _111ll11ll1_opy_[item.nodeid][bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪỻ")]
                bstack11l11lllll_opy_.set(hooks=_111ll11ll1_opy_[item.nodeid].get(bstack1l1l111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧỼ"), []))
                exception, bstack11l11l11ll_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11l11l11ll_opy_ = [call.excinfo.exconly(), getattr(report, bstack1l1l111_opy_ (u"ࠩ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠨỽ"), bstack1l1l111_opy_ (u"ࠪࠫỾ"))]
                bstack11l11lllll_opy_.stop(time=bstack111l11111_opy_, result=Result(result=getattr(report, bstack1l1l111_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬỿ"), bstack1l1l111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬἀ")), exception=exception, bstack11l11l11ll_opy_=bstack11l11l11ll_opy_))
                bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨἁ"), _111ll11ll1_opy_[item.nodeid][bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪἂ")])
        elif getattr(report, bstack1l1l111_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ἃ"), bstack1l1l111_opy_ (u"ࠩࠪἄ")) in [bstack1l1l111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩἅ"), bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ἆ")]:
            logger.debug(bstack1l1l111_opy_ (u"ࠬ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡵࡷࡥࡹ࡫ࠠ࠮ࠢࡾࢁ࠱ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࠰ࠤࢀࢃࠧἇ").format(getattr(report, bstack1l1l111_opy_ (u"࠭ࡷࡩࡧࡱࠫἈ"), bstack1l1l111_opy_ (u"ࠧࠨἉ")).__str__(), bstack111l1l1l111_opy_))
            bstack11l1l1111l_opy_ = item.nodeid + bstack1l1l111_opy_ (u"ࠨ࠯ࠪἊ") + getattr(report, bstack1l1l111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧἋ"), bstack1l1l111_opy_ (u"ࠪࠫἌ"))
            if getattr(report, bstack1l1l111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬἍ"), False):
                hook_type = bstack1l1l111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪἎ") if getattr(report, bstack1l1l111_opy_ (u"࠭ࡷࡩࡧࡱࠫἏ"), bstack1l1l111_opy_ (u"ࠧࠨἐ")) == bstack1l1l111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧἑ") else bstack1l1l111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ἒ")
                _111ll11ll1_opy_[bstack11l1l1111l_opy_] = {
                    bstack1l1l111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨἓ"): uuid4().__str__(),
                    bstack1l1l111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨἔ"): bstack111l11111_opy_,
                    bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨἕ"): hook_type
                }
            _111ll11ll1_opy_[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ἖")] = bstack111l11111_opy_
            bstack111l11l11ll_opy_(_111ll11ll1_opy_[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ἗")])
            bstack111l1l111ll_opy_(item, _111ll11ll1_opy_[bstack11l1l1111l_opy_], bstack1l1l111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪἘ"), report, call)
            if getattr(report, bstack1l1l111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧἙ"), bstack1l1l111_opy_ (u"ࠪࠫἚ")) == bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪἛ"):
                if getattr(report, bstack1l1l111_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭Ἔ"), bstack1l1l111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ἕ")) == bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ἞"):
                    bstack111lll1l11_opy_ = {
                        bstack1l1l111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭἟"): uuid4().__str__(),
                        bstack1l1l111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ἠ"): bstack1ll11l1ll1_opy_(),
                        bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨἡ"): bstack1ll11l1ll1_opy_()
                    }
                    _111ll11ll1_opy_[item.nodeid] = {**_111ll11ll1_opy_[item.nodeid], **bstack111lll1l11_opy_}
                    bstack111l1l1ll1l_opy_(item, _111ll11ll1_opy_[item.nodeid], bstack1l1l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬἢ"))
                    bstack111l1l1ll1l_opy_(item, _111ll11ll1_opy_[item.nodeid], bstack1l1l111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧἣ"), report, call)
    except Exception as err:
        print(bstack1l1l111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡽࢀࠫἤ"), str(err))
def bstack111l1l1ll11_opy_(test, bstack111lll1l11_opy_, result=None, call=None, bstack1l11ll1111_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11l11lllll_opy_ = {
        bstack1l1l111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἥ"): bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ἦ")],
        bstack1l1l111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧἧ"): bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࠨἨ"),
        bstack1l1l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἩ"): test.name,
        bstack1l1l111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪἪ"): {
            bstack1l1l111_opy_ (u"࠭࡬ࡢࡰࡪࠫἫ"): bstack1l1l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧἬ"),
            bstack1l1l111_opy_ (u"ࠨࡥࡲࡨࡪ࠭Ἥ"): inspect.getsource(test.obj)
        },
        bstack1l1l111_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭Ἦ"): test.name,
        bstack1l1l111_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩἯ"): test.name,
        bstack1l1l111_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫἰ"): bstack1l1lll1lll_opy_.bstack11l111111l_opy_(test),
        bstack1l1l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨἱ"): file_path,
        bstack1l1l111_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨἲ"): file_path,
        bstack1l1l111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧἳ"): bstack1l1l111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩἴ"),
        bstack1l1l111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧἵ"): file_path,
        bstack1l1l111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧἶ"): bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨἷ")],
        bstack1l1l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨἸ"): bstack1l1l111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭Ἱ"),
        bstack1l1l111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪἺ"): {
            bstack1l1l111_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬἻ"): test.nodeid
        },
        bstack1l1l111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧἼ"): bstack11lllll1l1l_opy_(test.own_markers)
    }
    if bstack1l11ll1111_opy_ in [bstack1l1l111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫἽ"), bstack1l1l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ἶ")]:
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠬࡳࡥࡵࡣࠪἿ")] = {
            bstack1l1l111_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨὀ"): bstack111lll1l11_opy_.get(bstack1l1l111_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩὁ"), [])
        }
    if bstack1l11ll1111_opy_ == bstack1l1l111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩὂ"):
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩὃ")] = bstack1l1l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫὄ")
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪὅ")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ὆")]
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ὇")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬὈ")]
    if result:
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨὉ")] = result.outcome
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪὊ")] = result.duration * 1000
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨὋ")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩὌ")]
        if result.failed:
            bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫὍ")] = bstack1l11l11lll_opy_.bstack111l111ll1_opy_(call.excinfo.typename)
            bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ὎")] = bstack1l11l11lll_opy_.bstack111ll1l11ll_opy_(call.excinfo, result)
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭὏")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧὐ")]
    if outcome:
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩὑ")] = bstack11ll1l1ll11_opy_(outcome)
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫὒ")] = 0
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩὓ")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪὔ")]
        if bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ὕ")] == bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧὖ"):
            bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧὗ")] = bstack1l1l111_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ὘")  # bstack111l1l1l11l_opy_
            bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫὙ")] = [{bstack1l1l111_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ὚"): [bstack1l1l111_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩὛ")]}]
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ὜")] = bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭Ὕ")]
    return bstack11l11lllll_opy_
def bstack111l1l1llll_opy_(test, bstack111lllllll_opy_, bstack1l11ll1111_opy_, result, call, outcome, bstack111l11l1ll1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ὞")]
    hook_name = bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬὟ")]
    hook_data = {
        bstack1l1l111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨὠ"): bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠫࡺࡻࡩࡥࠩὡ")],
        bstack1l1l111_opy_ (u"ࠬࡺࡹࡱࡧࠪὢ"): bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࠫὣ"),
        bstack1l1l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬὤ"): bstack1l1l111_opy_ (u"ࠨࡽࢀࠫὥ").format(bstack11l11111lll_opy_(hook_name)),
        bstack1l1l111_opy_ (u"ࠩࡥࡳࡩࡿࠧὦ"): {
            bstack1l1l111_opy_ (u"ࠪࡰࡦࡴࡧࠨὧ"): bstack1l1l111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫὨ"),
            bstack1l1l111_opy_ (u"ࠬࡩ࡯ࡥࡧࠪὩ"): None
        },
        bstack1l1l111_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬὪ"): test.name,
        bstack1l1l111_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧὫ"): bstack1l1lll1lll_opy_.bstack11l111111l_opy_(test, hook_name),
        bstack1l1l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫὬ"): file_path,
        bstack1l1l111_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫὭ"): file_path,
        bstack1l1l111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪὮ"): bstack1l1l111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬὯ"),
        bstack1l1l111_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪὰ"): file_path,
        bstack1l1l111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪά"): bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫὲ")],
        bstack1l1l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫέ"): bstack1l1l111_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫὴ") if bstack111l1l1l111_opy_ == bstack1l1l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧή") else bstack1l1l111_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫὶ"),
        bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨί"): hook_type
    }
    bstack111lll1ll11_opy_ = bstack11l111l111_opy_(_111ll11ll1_opy_.get(test.nodeid, None))
    if bstack111lll1ll11_opy_:
        hook_data[bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫὸ")] = bstack111lll1ll11_opy_
    if result:
        hook_data[bstack1l1l111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧό")] = result.outcome
        hook_data[bstack1l1l111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩὺ")] = result.duration * 1000
        hook_data[bstack1l1l111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧύ")] = bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨὼ")]
        if result.failed:
            hook_data[bstack1l1l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪώ")] = bstack1l11l11lll_opy_.bstack111l111ll1_opy_(call.excinfo.typename)
            hook_data[bstack1l1l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭὾")] = bstack1l11l11lll_opy_.bstack111ll1l11ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1l1l111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭὿")] = bstack11ll1l1ll11_opy_(outcome)
        hook_data[bstack1l1l111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᾀ")] = 100
        hook_data[bstack1l1l111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᾁ")] = bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᾂ")]
        if hook_data[bstack1l1l111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᾃ")] == bstack1l1l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᾄ"):
            hook_data[bstack1l1l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᾅ")] = bstack1l1l111_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧᾆ")  # bstack111l1l1l11l_opy_
            hook_data[bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᾇ")] = [{bstack1l1l111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᾈ"): [bstack1l1l111_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭ᾉ")]}]
    if bstack111l11l1ll1_opy_:
        hook_data[bstack1l1l111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᾊ")] = bstack111l11l1ll1_opy_.result
        hook_data[bstack1l1l111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᾋ")] = bstack11llll1ll1l_opy_(bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᾌ")], bstack111lllllll_opy_[bstack1l1l111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᾍ")])
        hook_data[bstack1l1l111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᾎ")] = bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᾏ")]
        if hook_data[bstack1l1l111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᾐ")] == bstack1l1l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᾑ"):
            hook_data[bstack1l1l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᾒ")] = bstack1l11l11lll_opy_.bstack111l111ll1_opy_(bstack111l11l1ll1_opy_.exception_type)
            hook_data[bstack1l1l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᾓ")] = [{bstack1l1l111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᾔ"): bstack11ll1l1l1l1_opy_(bstack111l11l1ll1_opy_.exception)}]
    return hook_data
def bstack111l1l1ll1l_opy_(test, bstack111lll1l11_opy_, bstack1l11ll1111_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack1l1l111_opy_ (u"ࠧࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡦࡸࡨࡲࡹࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡷࡩࡸࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠦ࠭ࠡࡽࢀࠫᾕ").format(bstack1l11ll1111_opy_))
    bstack11l11lllll_opy_ = bstack111l1l1ll11_opy_(test, bstack111lll1l11_opy_, result, call, bstack1l11ll1111_opy_, outcome)
    driver = getattr(test, bstack1l1l111_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᾖ"), None)
    if bstack1l11ll1111_opy_ == bstack1l1l111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᾗ") and driver:
        bstack11l11lllll_opy_[bstack1l1l111_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩᾘ")] = bstack1l11l11lll_opy_.bstack11l111ll1l_opy_(driver)
    if bstack1l11ll1111_opy_ == bstack1l1l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬᾙ"):
        bstack1l11ll1111_opy_ = bstack1l1l111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᾚ")
    bstack111ll1ll1l_opy_ = {
        bstack1l1l111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᾛ"): bstack1l11ll1111_opy_,
        bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩᾜ"): bstack11l11lllll_opy_
    }
    bstack1l11l11lll_opy_.bstack111ll111l_opy_(bstack111ll1ll1l_opy_)
    if bstack1l11ll1111_opy_ == bstack1l1l111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᾝ"):
        threading.current_thread().bstackTestMeta = {bstack1l1l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᾞ"): bstack1l1l111_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᾟ")}
    elif bstack1l11ll1111_opy_ == bstack1l1l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᾠ"):
        threading.current_thread().bstackTestMeta = {bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᾡ"): getattr(result, bstack1l1l111_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧᾢ"), bstack1l1l111_opy_ (u"ࠧࠨᾣ"))}
def bstack111l1l111ll_opy_(test, bstack111lll1l11_opy_, bstack1l11ll1111_opy_, result=None, call=None, outcome=None, bstack111l11l1ll1_opy_=None):
    logger.debug(bstack1l1l111_opy_ (u"ࠨࡵࡨࡲࡩࡥࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡧࡹࡩࡳࡺ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣ࡬ࡴࡵ࡫ࠡࡦࡤࡸࡦ࠲ࠠࡦࡸࡨࡲࡹ࡚ࡹࡱࡧࠣ࠱ࠥࢁࡽࠨᾤ").format(bstack1l11ll1111_opy_))
    hook_data = bstack111l1l1llll_opy_(test, bstack111lll1l11_opy_, bstack1l11ll1111_opy_, result, call, outcome, bstack111l11l1ll1_opy_)
    bstack111ll1ll1l_opy_ = {
        bstack1l1l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᾥ"): bstack1l11ll1111_opy_,
        bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬᾦ"): hook_data
    }
    bstack1l11l11lll_opy_.bstack111ll111l_opy_(bstack111ll1ll1l_opy_)
def bstack11l111l111_opy_(bstack111lll1l11_opy_):
    if not bstack111lll1l11_opy_:
        return None
    if bstack111lll1l11_opy_.get(bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᾧ"), None):
        return getattr(bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᾨ")], bstack1l1l111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᾩ"), None)
    return bstack111lll1l11_opy_.get(bstack1l1l111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᾪ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.LOG, bstack1lllll11111_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack111111l111_opy_.LOG, bstack1lllll11111_opy_.POST, request, caplog)
        return # skip all existing bstack111l1l1l1ll_opy_
    try:
        if not bstack1l11l11lll_opy_.on():
            return
        places = [bstack1l1l111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᾫ"), bstack1l1l111_opy_ (u"ࠩࡦࡥࡱࡲࠧᾬ"), bstack1l1l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᾭ")]
        logs = []
        for bstack111l11l1l1l_opy_ in places:
            records = caplog.get_records(bstack111l11l1l1l_opy_)
            bstack111l1l11l11_opy_ = bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᾮ") if bstack111l11l1l1l_opy_ == bstack1l1l111_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᾯ") else bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᾰ")
            bstack111l11l1lll_opy_ = request.node.nodeid + (bstack1l1l111_opy_ (u"ࠧࠨᾱ") if bstack111l11l1l1l_opy_ == bstack1l1l111_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᾲ") else bstack1l1l111_opy_ (u"ࠩ࠰ࠫᾳ") + bstack111l11l1l1l_opy_)
            test_uuid = bstack11l111l111_opy_(_111ll11ll1_opy_.get(bstack111l11l1lll_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack11lll11l1l1_opy_(record.message):
                    continue
                logs.append({
                    bstack1l1l111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᾴ"): bstack11ll11lllll_opy_(record.created).isoformat() + bstack1l1l111_opy_ (u"ࠫ࡟࠭᾵"),
                    bstack1l1l111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᾶ"): record.levelname,
                    bstack1l1l111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᾷ"): record.message,
                    bstack111l1l11l11_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l11l11lll_opy_.bstack11l11lll1_opy_(logs)
    except Exception as err:
        print(bstack1l1l111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡥࡲࡲࡩࡥࡦࡪࡺࡷࡹࡷ࡫࠺ࠡࡽࢀࠫᾸ"), str(err))
def bstack1llllllll1_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l11ll1l1_opy_
    bstack1l1l111l1_opy_ = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᾹ"), None) and bstack1l11ll111l_opy_(
            threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᾺ"), None)
    bstack1ll11lllll_opy_ = getattr(driver, bstack1l1l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪΆ"), None) != None and getattr(driver, bstack1l1l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫᾼ"), None) == True
    if sequence == bstack1l1l111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ᾽") and driver != None:
      if not bstack1l11ll1l1_opy_ and bstack1ll111111l1_opy_() and bstack1l1l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ι") in CONFIG and CONFIG[bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᾿")] == True and bstack11l1l1ll1l_opy_.bstack1ll11l1ll_opy_(driver_command) and (bstack1ll11lllll_opy_ or bstack1l1l111l1_opy_) and not bstack11llll111l_opy_(args):
        try:
          bstack1l11ll1l1_opy_ = True
          logger.debug(bstack1l1l111_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪ῀").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1l1l111_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧ῁").format(str(err)))
        bstack1l11ll1l1_opy_ = False
    if sequence == bstack1l1l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩῂ"):
        if driver_command == bstack1l1l111_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨῃ"):
            bstack1l11l11lll_opy_.bstack11l11lll_opy_({
                bstack1l1l111_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫῄ"): response[bstack1l1l111_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ῅")],
                bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧῆ"): store[bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬῇ")]
            })
def bstack1ll111l11l_opy_():
    global bstack1111l11l1_opy_
    bstack1111ll11l_opy_.bstack1l1l11l1ll_opy_()
    logging.shutdown()
    bstack1l11l11lll_opy_.bstack11l11111l1_opy_()
    for driver in bstack1111l11l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack111l11lllll_opy_(*args):
    global bstack1111l11l1_opy_
    bstack1l11l11lll_opy_.bstack11l11111l1_opy_()
    for driver in bstack1111l11l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11ll1l1l1l_opy_, stage=STAGE.bstack1l1l1111l_opy_, bstack1ll1l1l11_opy_=bstack11ll111l1l_opy_)
def bstack11111111l_opy_(self, *args, **kwargs):
    bstack1l1l1lll1_opy_ = bstack11lllllll_opy_(self, *args, **kwargs)
    bstack1l1l1ll1l_opy_ = getattr(threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪῈ"), None)
    if bstack1l1l1ll1l_opy_ and bstack1l1l1ll1l_opy_.get(bstack1l1l111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪΈ"), bstack1l1l111_opy_ (u"ࠫࠬῊ")) == bstack1l1l111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭Ή"):
        bstack1l11l11lll_opy_.bstack1ll1ll1lll_opy_(self)
    return bstack1l1l1lll1_opy_
@measure(event_name=EVENTS.bstack1l111ll1_opy_, stage=STAGE.bstack1l111lllll_opy_, bstack1ll1l1l11_opy_=bstack11ll111l1l_opy_)
def bstack1l11l1llll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
    if bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪῌ")):
        return
    bstack111l11l1l_opy_.bstack11lll11111_opy_(bstack1l1l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ῍"), True)
    global bstack111l111l_opy_
    global bstack11l1llllll_opy_
    bstack111l111l_opy_ = framework_name
    logger.info(bstack1l111111l_opy_.format(bstack111l111l_opy_.split(bstack1l1l111_opy_ (u"ࠨ࠯ࠪ῎"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1ll111111l1_opy_():
            Service.start = bstack11ll1l1ll1_opy_
            Service.stop = bstack1l11l11ll_opy_
            webdriver.Remote.get = bstack1l1ll1l1ll_opy_
            webdriver.Remote.__init__ = bstack1lll1lll11_opy_
            if not isinstance(os.getenv(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪ῏")), str):
                return
            WebDriver.close = bstack11l111l1_opy_
            WebDriver.quit = bstack1lllll111_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l11l11lll_opy_.on():
            webdriver.Remote.__init__ = bstack11111111l_opy_
        bstack11l1llllll_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack1l1l111_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨῐ")):
        bstack11l1llllll_opy_ = eval(os.environ.get(bstack1l1l111_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩῑ")))
    if not bstack11l1llllll_opy_:
        bstack1l111111l1_opy_(bstack1l1l111_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢῒ"), bstack1l111lll_opy_)
    if bstack11l1ll111l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._111l1l11_opy_ = bstack11lll1l11_opy_
        except Exception as e:
            logger.error(bstack11111l1ll_opy_.format(str(e)))
    if bstack1l1l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ΐ") in str(framework_name).lower():
        if not bstack1ll111111l1_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1ll1llll11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11llll1l11_opy_
            Config.getoption = bstack1l1l11ll1_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1ll111111_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lllll1l11_opy_, stage=STAGE.bstack1l1l1111l_opy_, bstack1ll1l1l11_opy_=bstack11ll111l1l_opy_)
def bstack1lllll111_opy_(self):
    global bstack111l111l_opy_
    global bstack1lll111l11_opy_
    global bstack11lll1ll1l_opy_
    try:
        if bstack1l1l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ῔") in bstack111l111l_opy_ and self.session_id != None and bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ῕"), bstack1l1l111_opy_ (u"ࠩࠪῖ")) != bstack1l1l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫῗ"):
            bstack111lllll1_opy_ = bstack1l1l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫῘ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬῙ")
            bstack111l111ll_opy_(logger, True)
            if self != None:
                bstack11ll111111_opy_(self, bstack111lllll1_opy_, bstack1l1l111_opy_ (u"࠭ࠬࠡࠩῚ").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1llll11ll1l_opy_(bstack1lll1l11111_opy_):
            item = store.get(bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫΊ"), None)
            if item is not None and bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ῜"), None):
                bstack1l11l111_opy_.bstack111ll1lll_opy_(self, bstack111l1l1l1_opy_, logger, item)
        threading.current_thread().testStatus = bstack1l1l111_opy_ (u"ࠩࠪ῝")
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦ῞") + str(e))
    bstack11lll1ll1l_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1llll1l111_opy_, stage=STAGE.bstack1l1l1111l_opy_, bstack1ll1l1l11_opy_=bstack11ll111l1l_opy_)
def bstack1lll1lll11_opy_(self, command_executor,
             desired_capabilities=None, bstack1ll1lll1l1_opy_=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1lll111l11_opy_
    global bstack11ll111l1l_opy_
    global bstack1ll1l1lll_opy_
    global bstack111l111l_opy_
    global bstack11lllllll_opy_
    global bstack1111l11l1_opy_
    global bstack11l1llll_opy_
    global bstack1111ll1l_opy_
    global bstack111l1l1l1_opy_
    CONFIG[bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭῟")] = str(bstack111l111l_opy_) + str(__version__)
    command_executor = bstack11l1l1llll_opy_(bstack11l1llll_opy_, CONFIG)
    logger.debug(bstack11l1111l1_opy_.format(command_executor))
    proxy = bstack1ll1ll111l_opy_(CONFIG, proxy)
    bstack1l11ll11l_opy_ = 0
    try:
        if bstack1ll1l1lll_opy_ is True:
            bstack1l11ll11l_opy_ = int(os.environ.get(bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬῠ")))
    except:
        bstack1l11ll11l_opy_ = 0
    bstack11llll1lll_opy_ = bstack111l11l1_opy_(CONFIG, bstack1l11ll11l_opy_)
    logger.debug(bstack1ll111l1l_opy_.format(str(bstack11llll1lll_opy_)))
    bstack111l1l1l1_opy_ = CONFIG.get(bstack1l1l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῡ"))[bstack1l11ll11l_opy_]
    if bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫῢ") in CONFIG and CONFIG[bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬΰ")]:
        bstack1l1l1ll11l_opy_(bstack11llll1lll_opy_, bstack1111ll1l_opy_)
    if bstack11l1l1lll_opy_.bstack1111llll1_opy_(CONFIG, bstack1l11ll11l_opy_) and bstack11l1l1lll_opy_.bstack1111lll1l_opy_(bstack11llll1lll_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1llll11ll1l_opy_(bstack1lll1l11111_opy_):
            bstack11l1l1lll_opy_.set_capabilities(bstack11llll1lll_opy_, CONFIG)
    if desired_capabilities:
        bstack1ll1111ll1_opy_ = bstack1llllll1l1_opy_(desired_capabilities)
        bstack1ll1111ll1_opy_[bstack1l1l111_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩῤ")] = bstack1lll1l1l1_opy_(CONFIG)
        bstack11lll111_opy_ = bstack111l11l1_opy_(bstack1ll1111ll1_opy_)
        if bstack11lll111_opy_:
            bstack11llll1lll_opy_ = update(bstack11lll111_opy_, bstack11llll1lll_opy_)
        desired_capabilities = None
    if options:
        bstack11l1l1ll1_opy_(options, bstack11llll1lll_opy_)
    if not options:
        options = bstack1l1l1l11l_opy_(bstack11llll1lll_opy_)
    if proxy and bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪῥ")):
        options.proxy(proxy)
    if options and bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪῦ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11l1lllll_opy_() < version.parse(bstack1l1l111_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫῧ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11llll1lll_opy_)
    logger.info(bstack1l1lll1ll1_opy_)
    bstack1111l1ll1_opy_.end(EVENTS.bstack1l111ll1_opy_.value, EVENTS.bstack1l111ll1_opy_.value + bstack1l1l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨῨ"),
                               EVENTS.bstack1l111ll1_opy_.value + bstack1l1l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧῩ"), True, None)
    if bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨῪ")):
        bstack11lllllll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨΎ")):
        bstack11lllllll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  bstack1ll1lll1l1_opy_=bstack1ll1lll1l1_opy_, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪῬ")):
        bstack11lllllll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  bstack1ll1lll1l1_opy_=bstack1ll1lll1l1_opy_, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11lllllll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  bstack1ll1lll1l1_opy_=bstack1ll1lll1l1_opy_, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l111ll1l_opy_ = bstack1l1l111_opy_ (u"ࠫࠬ῭")
        if bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭΅")):
            bstack1l111ll1l_opy_ = self.caps.get(bstack1l1l111_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨ`"))
        else:
            bstack1l111ll1l_opy_ = self.capabilities.get(bstack1l1l111_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ῰"))
        if bstack1l111ll1l_opy_:
            bstack1ll1l1l1l_opy_(bstack1l111ll1l_opy_)
            if bstack11l1lllll_opy_() <= version.parse(bstack1l1l111_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ῱")):
                self.command_executor._url = bstack1l1l111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥῲ") + bstack11l1llll_opy_ + bstack1l1l111_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢῳ")
            else:
                self.command_executor._url = bstack1l1l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨῴ") + bstack1l111ll1l_opy_ + bstack1l1l111_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨ῵")
            logger.debug(bstack1ll1l1l11l_opy_.format(bstack1l111ll1l_opy_))
        else:
            logger.debug(bstack1l1llllll1_opy_.format(bstack1l1l111_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢῶ")))
    except Exception as e:
        logger.debug(bstack1l1llllll1_opy_.format(e))
    bstack1lll111l11_opy_ = self.session_id
    if bstack1l1l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧῷ") in bstack111l111l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬῸ"), None)
        if item:
            bstack111l1l11ll1_opy_ = getattr(item, bstack1l1l111_opy_ (u"ࠩࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪࡥࡳࡵࡣࡵࡸࡪࡪࠧΌ"), False)
            if not getattr(item, bstack1l1l111_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫῺ"), None) and bstack111l1l11ll1_opy_:
                setattr(store[bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨΏ")], bstack1l1l111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ῼ"), self)
        bstack1l1l1ll1l_opy_ = getattr(threading.current_thread(), bstack1l1l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ´"), None)
        if bstack1l1l1ll1l_opy_ and bstack1l1l1ll1l_opy_.get(bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ῾"), bstack1l1l111_opy_ (u"ࠨࠩ῿")) == bstack1l1l111_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ "):
            bstack1l11l11lll_opy_.bstack1ll1ll1lll_opy_(self)
    bstack1111l11l1_opy_.append(self)
    if bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ ") in CONFIG and bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ ") in CONFIG[bstack1l1l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ ")][bstack1l11ll11l_opy_]:
        bstack11ll111l1l_opy_ = CONFIG[bstack1l1l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ ")][bstack1l11ll11l_opy_][bstack1l1l111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ ")]
    logger.debug(bstack1l1lll11l_opy_.format(bstack1lll111l11_opy_))
@measure(event_name=EVENTS.bstack11l11llll_opy_, stage=STAGE.bstack1l1l1111l_opy_, bstack1ll1l1l11_opy_=bstack11ll111l1l_opy_)
def bstack1l1ll1l1ll_opy_(self, url):
    global bstack1ll1lll1l_opy_
    global CONFIG
    try:
        bstack1ll1ll1ll1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11ll11llll_opy_.format(str(err)))
    try:
        bstack1ll1lll1l_opy_(self, url)
    except Exception as e:
        try:
            bstack11l1lll1ll_opy_ = str(e)
            if any(err_msg in bstack11l1lll1ll_opy_ for err_msg in bstack1l1l1111ll_opy_):
                bstack1ll1ll1ll1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11ll11llll_opy_.format(str(err)))
        raise e
def bstack1l1l11111_opy_(item, when):
    global bstack1lllllll11_opy_
    try:
        bstack1lllllll11_opy_(item, when)
    except Exception as e:
        pass
def bstack1ll111111_opy_(item, call, rep):
    global bstack1ll11lll11_opy_
    global bstack1111l11l1_opy_
    name = bstack1l1l111_opy_ (u"ࠨࠩ ")
    try:
        if rep.when == bstack1l1l111_opy_ (u"ࠩࡦࡥࡱࡲࠧ "):
            bstack1lll111l11_opy_ = threading.current_thread().bstackSessionId
            bstack111l1l11l1l_opy_ = item.config.getoption(bstack1l1l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ "))
            try:
                if (str(bstack111l1l11l1l_opy_).lower() != bstack1l1l111_opy_ (u"ࠫࡹࡸࡵࡦࠩ ")):
                    name = str(rep.nodeid)
                    bstack11l111l11_opy_ = bstack1ll1l1l1l1_opy_(bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ "), name, bstack1l1l111_opy_ (u"࠭ࠧ​"), bstack1l1l111_opy_ (u"ࠧࠨ‌"), bstack1l1l111_opy_ (u"ࠨࠩ‍"), bstack1l1l111_opy_ (u"ࠩࠪ‎"))
                    os.environ[bstack1l1l111_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭‏")] = name
                    for driver in bstack1111l11l1_opy_:
                        if bstack1lll111l11_opy_ == driver.session_id:
                            driver.execute_script(bstack11l111l11_opy_)
            except Exception as e:
                logger.debug(bstack1l1l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ‐").format(str(e)))
            try:
                bstack111llll11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1l1l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭‑"):
                    status = bstack1l1l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭‒") if rep.outcome.lower() == bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ–") else bstack1l1l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ—")
                    reason = bstack1l1l111_opy_ (u"ࠩࠪ―")
                    if status == bstack1l1l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ‖"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1l1l111_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ‗") if status == bstack1l1l111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ‘") else bstack1l1l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ’")
                    data = name + bstack1l1l111_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ‚") if status == bstack1l1l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ‛") else name + bstack1l1l111_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ“") + reason
                    bstack11ll111ll1_opy_ = bstack1ll1l1l1l1_opy_(bstack1l1l111_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ”"), bstack1l1l111_opy_ (u"ࠫࠬ„"), bstack1l1l111_opy_ (u"ࠬ࠭‟"), bstack1l1l111_opy_ (u"࠭ࠧ†"), level, data)
                    for driver in bstack1111l11l1_opy_:
                        if bstack1lll111l11_opy_ == driver.session_id:
                            driver.execute_script(bstack11ll111ll1_opy_)
            except Exception as e:
                logger.debug(bstack1l1l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ‡").format(str(e)))
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ•").format(str(e)))
    bstack1ll11lll11_opy_(item, call, rep)
notset = Notset()
def bstack1l1l11ll1_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1ll11l1l_opy_
    if str(name).lower() == bstack1l1l111_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ‣"):
        return bstack1l1l111_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ․")
    else:
        return bstack1ll11l1l_opy_(self, name, default, skip)
def bstack11lll1l11_opy_(self):
    global CONFIG
    global bstack1lllll1ll1_opy_
    try:
        proxy = bstack11lll11l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1l1l111_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ‥")):
                proxies = bstack1l11ll1l_opy_(proxy, bstack11l1l1llll_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1l1l1lll_opy_ = proxies.popitem()
                    if bstack1l1l111_opy_ (u"ࠧࡀ࠯࠰ࠤ…") in bstack1l1l1l1lll_opy_:
                        return bstack1l1l1l1lll_opy_
                    else:
                        return bstack1l1l111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ‧") + bstack1l1l1l1lll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1l1l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦ ").format(str(e)))
    return bstack1lllll1ll1_opy_(self)
def bstack11l1ll111l_opy_():
    return (bstack1l1l111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ ") in CONFIG or bstack1l1l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭‪") in CONFIG) and bstack1ll111lll1_opy_() and bstack11l1lllll_opy_() >= version.parse(
        bstack1lllll11l1_opy_)
def bstack1lll1ll1ll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack11ll111l1l_opy_
    global bstack1ll1l1lll_opy_
    global bstack111l111l_opy_
    CONFIG[bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ‫")] = str(bstack111l111l_opy_) + str(__version__)
    bstack1l11ll11l_opy_ = 0
    try:
        if bstack1ll1l1lll_opy_ is True:
            bstack1l11ll11l_opy_ = int(os.environ.get(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ‬")))
    except:
        bstack1l11ll11l_opy_ = 0
    CONFIG[bstack1l1l111_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ‭")] = True
    bstack11llll1lll_opy_ = bstack111l11l1_opy_(CONFIG, bstack1l11ll11l_opy_)
    logger.debug(bstack1ll111l1l_opy_.format(str(bstack11llll1lll_opy_)))
    if CONFIG.get(bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ‮")):
        bstack1l1l1ll11l_opy_(bstack11llll1lll_opy_, bstack1111ll1l_opy_)
    if bstack1l1l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ ") in CONFIG and bstack1l1l111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭‰") in CONFIG[bstack1l1l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ‱")][bstack1l11ll11l_opy_]:
        bstack11ll111l1l_opy_ = CONFIG[bstack1l1l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭′")][bstack1l11ll11l_opy_][bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ″")]
    import urllib
    import json
    if bstack1l1l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ‴") in CONFIG and str(CONFIG[bstack1l1l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ‵")]).lower() != bstack1l1l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭‶"):
        bstack11lll11l1l_opy_ = bstack1lll11llll_opy_()
        bstack111l11ll_opy_ = bstack11lll11l1l_opy_ + urllib.parse.quote(json.dumps(bstack11llll1lll_opy_))
    else:
        bstack111l11ll_opy_ = bstack1l1l111_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪ‷") + urllib.parse.quote(json.dumps(bstack11llll1lll_opy_))
    browser = self.connect(bstack111l11ll_opy_)
    return browser
def bstack11111l1l_opy_():
    global bstack11l1llllll_opy_
    global bstack111l111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l1lll111_opy_
        if not bstack1ll111111l1_opy_():
            global bstack1l1ll11ll_opy_
            if not bstack1l1ll11ll_opy_:
                from bstack_utils.helper import bstack1111l11l_opy_, bstack1l1lll111l_opy_
                bstack1l1ll11ll_opy_ = bstack1111l11l_opy_()
                bstack1l1lll111l_opy_(bstack111l111l_opy_)
            BrowserType.connect = bstack1l1lll111_opy_
            return
        BrowserType.launch = bstack1lll1ll1ll_opy_
        bstack11l1llllll_opy_ = True
    except Exception as e:
        pass
def bstack111l1l1l1l1_opy_():
    global CONFIG
    global bstack1l11l1l11l_opy_
    global bstack11l1llll_opy_
    global bstack1111ll1l_opy_
    global bstack1ll1l1lll_opy_
    global bstack111ll1l1_opy_
    CONFIG = json.loads(os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ‸")))
    bstack1l11l1l11l_opy_ = eval(os.environ.get(bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ‹")))
    bstack11l1llll_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ›"))
    bstack11l1111ll_opy_(CONFIG, bstack1l11l1l11l_opy_)
    bstack111ll1l1_opy_ = bstack1111ll11l_opy_.bstack1111l1l1_opy_(CONFIG, bstack111ll1l1_opy_)
    if cli.bstack1lll1ll1l_opy_():
        bstack11lll1l1_opy_.invoke(bstack1llll1lll1_opy_.CONNECT, bstack1l11111111_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ※"), bstack1l1l111_opy_ (u"࠭࠰ࠨ‼")))
        cli.bstack1lll1ll1ll1_opy_(cli_context.platform_index)
        cli.bstack1lll1llll1l_opy_(bstack11l1l1llll_opy_(bstack11l1llll_opy_, CONFIG), cli_context.platform_index, bstack1l1l1l11l_opy_)
        cli.bstack1lllll1l1ll_opy_()
        logger.debug(bstack1l1l111_opy_ (u"ࠢࡄࡎࡌࠤ࡮ࡹࠠࡢࡥࡷ࡭ࡻ࡫ࠠࡧࡱࡵࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࠨ‽") + str(cli_context.platform_index) + bstack1l1l111_opy_ (u"ࠣࠤ‾"))
        return # skip all existing bstack111l1l1l1ll_opy_
    global bstack11lllllll_opy_
    global bstack11lll1ll1l_opy_
    global bstack1ll11l111l_opy_
    global bstack1l1llll1_opy_
    global bstack11ll11ll11_opy_
    global bstack11l1lll1l_opy_
    global bstack1l1l1l1l_opy_
    global bstack1ll1lll1l_opy_
    global bstack1lllll1ll1_opy_
    global bstack1ll11l1l_opy_
    global bstack1lllllll11_opy_
    global bstack1ll11lll11_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11lllllll_opy_ = webdriver.Remote.__init__
        bstack11lll1ll1l_opy_ = WebDriver.quit
        bstack1l1l1l1l_opy_ = WebDriver.close
        bstack1ll1lll1l_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1l1l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ‿") in CONFIG or bstack1l1l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ⁀") in CONFIG) and bstack1ll111lll1_opy_():
        if bstack11l1lllll_opy_() < version.parse(bstack1lllll11l1_opy_):
            logger.error(bstack1l1111l1_opy_.format(bstack11l1lllll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1lllll1ll1_opy_ = RemoteConnection._111l1l11_opy_
            except Exception as e:
                logger.error(bstack11111l1ll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1ll11l1l_opy_ = Config.getoption
        from _pytest import runner
        bstack1lllllll11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11ll1111l1_opy_)
    try:
        from pytest_bdd import reporting
        bstack1ll11lll11_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬ⁁"))
    bstack1111ll1l_opy_ = CONFIG.get(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⁂"), {}).get(bstack1l1l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ⁃"))
    bstack1ll1l1lll_opy_ = True
    bstack1l11l1llll_opy_(bstack1l1l11ll11_opy_)
if (bstack11lllll111l_opy_()):
    bstack111l1l1l1l1_opy_()
@bstack111lllll1l_opy_(class_method=False)
def bstack111l11l111l_opy_(hook_name, event, bstack1l11ll1l11l_opy_=None):
    if hook_name not in [bstack1l1l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ⁄"), bstack1l1l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬ⁅"), bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨ⁆"), bstack1l1l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬ⁇"), bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩ⁈"), bstack1l1l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭⁉"), bstack1l1l111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬ⁊"), bstack1l1l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ⁋")]:
        return
    node = store[bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ⁌")]
    if hook_name in [bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨ⁍"), bstack1l1l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬ⁎")]:
        node = store[bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪ⁏")]
    elif hook_name in [bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪ⁐"), bstack1l1l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧ⁑")]:
        node = store[bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡥ࡯ࡥࡸࡹ࡟ࡪࡶࡨࡱࠬ⁒")]
    hook_type = bstack11l11111l11_opy_(hook_name)
    if event == bstack1l1l111_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ⁓"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_[hook_type], bstack1lllll11111_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack111lllllll_opy_ = {
            bstack1l1l111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⁔"): uuid,
            bstack1l1l111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⁕"): bstack1ll11l1ll1_opy_(),
            bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩ⁖"): bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⁗"),
            bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⁘"): hook_type,
            bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪ⁙"): hook_name
        }
        store[bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⁚")].append(uuid)
        bstack111l11ll1ll_opy_ = node.nodeid
        if hook_type == bstack1l1l111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ⁛"):
            if not _111ll11ll1_opy_.get(bstack111l11ll1ll_opy_, None):
                _111ll11ll1_opy_[bstack111l11ll1ll_opy_] = {bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⁜"): []}
            _111ll11ll1_opy_[bstack111l11ll1ll_opy_][bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⁝")].append(bstack111lllllll_opy_[bstack1l1l111_opy_ (u"ࠬࡻࡵࡪࡦࠪ⁞")])
        _111ll11ll1_opy_[bstack111l11ll1ll_opy_ + bstack1l1l111_opy_ (u"࠭࠭ࠨ ") + hook_name] = bstack111lllllll_opy_
        bstack111l1l111ll_opy_(node, bstack111lllllll_opy_, bstack1l1l111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⁠"))
    elif event == bstack1l1l111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧ⁡"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack111111l111_opy_[hook_type], bstack1lllll11111_opy_.POST, node, None, bstack1l11ll1l11l_opy_)
            return
        bstack11l1l1111l_opy_ = node.nodeid + bstack1l1l111_opy_ (u"ࠩ࠰ࠫ⁢") + hook_name
        _111ll11ll1_opy_[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⁣")] = bstack1ll11l1ll1_opy_()
        bstack111l11l11ll_opy_(_111ll11ll1_opy_[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⁤")])
        bstack111l1l111ll_opy_(node, _111ll11ll1_opy_[bstack11l1l1111l_opy_], bstack1l1l111_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⁥"), bstack111l11l1ll1_opy_=bstack1l11ll1l11l_opy_)
def bstack111l1l1111l_opy_():
    global bstack111l1l1l111_opy_
    if bstack11l1l1111_opy_():
        bstack111l1l1l111_opy_ = bstack1l1l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ⁦")
    else:
        bstack111l1l1l111_opy_ = bstack1l1l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ⁧")
@bstack1l11l11lll_opy_.bstack111ll1ll1l1_opy_
def bstack111l11ll111_opy_():
    bstack111l1l1111l_opy_()
    if cli.is_running():
        try:
            bstack11ll11l111l_opy_(bstack111l11l111l_opy_)
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡸࠦࡰࡢࡶࡦ࡬࠿ࠦࡻࡾࠤ⁨").format(e))
        return
    if bstack1ll111lll1_opy_():
        bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
        bstack1l1l111_opy_ (u"ࠩࠪࠫࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡊࡴࡸࠠࡱࡲࡳࠤࡂࠦ࠱࠭ࠢࡰࡳࡩࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡨࡧࡷࡷࠥࡻࡳࡦࡦࠣࡪࡴࡸࠠࡢ࠳࠴ࡽࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࠭ࡸࡴࡤࡴࡵ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡵࡶࡰࠡࡀࠣ࠵࠱ࠦ࡭ࡰࡦࡢࡩࡽ࡫ࡣࡶࡶࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡲࡶࡰࠣࡦࡪࡩࡡࡶࡵࡨࠤ࡮ࡺࠠࡪࡵࠣࡴࡦࡺࡣࡩࡧࡧࠤ࡮ࡴࠠࡢࠢࡧ࡭࡫࡬ࡥࡳࡧࡱࡸࠥࡶࡲࡰࡥࡨࡷࡸࠦࡩࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡸࡷࠥࡽࡥࠡࡰࡨࡩࡩࠦࡴࡰࠢࡸࡷࡪࠦࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࡑࡣࡷࡧ࡭࠮ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡪࡤࡲࡩࡲࡥࡳࠫࠣࡪࡴࡸࠠࡱࡲࡳࠤࡃࠦ࠱ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪࠫࠬ⁩")
        if bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ⁪")):
            if CONFIG.get(bstack1l1l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ⁫")) is not None and int(CONFIG[bstack1l1l111_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ⁬")]) > 1:
                bstack1l1l11111l_opy_(bstack1llllllll1_opy_)
            return
        bstack1l1l11111l_opy_(bstack1llllllll1_opy_)
    try:
        bstack11ll11l111l_opy_(bstack111l11l111l_opy_)
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢ⁭").format(e))
bstack111l11ll111_opy_()