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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack11l11lllll_opy_ import bstack11l11lll11_opy_, bstack11l1l11l1l_opy_
from bstack_utils.bstack11l11ll1ll_opy_ import bstack1l1lll1lll_opy_
from bstack_utils.helper import bstack1l11ll111l_opy_, bstack1ll11l1ll1_opy_, Result
from bstack_utils.bstack11l11l1l1l_opy_ import bstack1l11l11lll_opy_
from bstack_utils.capture import bstack11l11lll1l_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack1llll1l11l_opy_:
    def __init__(self):
        self.bstack11l11l1111_opy_ = bstack11l11lll1l_opy_(self.bstack11l1l111l1_opy_)
        self.tests = {}
    @staticmethod
    def bstack11l1l111l1_opy_(log):
        if not (log[bstack1l1l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬຉ")] and log[bstack1l1l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ຊ")].strip()):
            return
        active = bstack1l1lll1lll_opy_.bstack11l11l1ll1_opy_()
        log = {
            bstack1l1l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ຋"): log[bstack1l1l111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ຌ")],
            bstack1l1l111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫຍ"): bstack1ll11l1ll1_opy_(),
            bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪຎ"): log[bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫຏ")],
        }
        if active:
            if active[bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩຐ")] == bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪຑ"):
                log[bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ຒ")] = active[bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧຓ")]
            elif active[bstack1l1l111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ດ")] == bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺࠧຕ"):
                log[bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪຖ")] = active[bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫທ")]
        bstack1l11l11lll_opy_.bstack11l11lll1_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack11l11l1111_opy_.start()
        driver = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫຘ"), None)
        bstack11l11lllll_opy_ = bstack11l1l11l1l_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1ll11l1ll1_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1l1l111_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢນ"),
            framework=bstack1l1l111_opy_ (u"ࠧࡃࡧ࡫ࡥࡻ࡫ࠧບ"),
            scope=[attrs.feature.name],
            bstack11l111llll_opy_=bstack1l11l11lll_opy_.bstack11l111ll1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫປ")] = bstack11l11lllll_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪຜ"), bstack11l11lllll_opy_)
    def end_test(self, attrs):
        bstack11l11l111l_opy_ = {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣຝ"): attrs.feature.name,
            bstack1l1l111_opy_ (u"ࠦࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤພ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack11l11lllll_opy_ = self.tests[current_test_uuid][bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨຟ")]
        meta = {
            bstack1l1l111_opy_ (u"ࠨࡦࡦࡣࡷࡹࡷ࡫ࠢຠ"): bstack11l11l111l_opy_,
            bstack1l1l111_opy_ (u"ࠢࡴࡶࡨࡴࡸࠨມ"): bstack11l11lllll_opy_.meta.get(bstack1l1l111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧຢ"), []),
            bstack1l1l111_opy_ (u"ࠤࡶࡧࡪࡴࡡࡳ࡫ࡲࠦຣ"): {
                bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣ຤"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack11l11lllll_opy_.bstack11l11llll1_opy_(meta)
        bstack11l11lllll_opy_.bstack11l11l1l11_opy_(bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩລ"), []))
        bstack11l1l11ll1_opy_, exception = self._11l1l11l11_opy_(attrs)
        bstack11l1l11111_opy_ = Result(result=attrs.status.name, exception=exception, bstack11l11l11ll_opy_=[bstack11l1l11ll1_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ຦")].stop(time=bstack1ll11l1ll1_opy_(), duration=int(attrs.duration)*1000, result=bstack11l1l11111_opy_)
        bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨວ"), self.tests[threading.current_thread().current_test_uuid][bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪຨ")])
    def bstack1ll1l1ll1_opy_(self, attrs):
        bstack11l11ll111_opy_ = {
            bstack1l1l111_opy_ (u"ࠨ࡫ࡧࠫຩ"): uuid4().__str__(),
            bstack1l1l111_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪສ"): attrs.keyword,
            bstack1l1l111_opy_ (u"ࠪࡷࡹ࡫ࡰࡠࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠪຫ"): [],
            bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡸࡵࠩຬ"): attrs.name,
            bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩອ"): bstack1ll11l1ll1_opy_(),
            bstack1l1l111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ຮ"): bstack1l1l111_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨຯ"),
            bstack1l1l111_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ະ"): bstack1l1l111_opy_ (u"ࠩࠪັ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭າ")].add_step(bstack11l11ll111_opy_)
        threading.current_thread().current_step_uuid = bstack11l11ll111_opy_[bstack1l1l111_opy_ (u"ࠫ࡮ࡪࠧຳ")]
    def bstack1ll11l111_opy_(self, attrs):
        current_test_id = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩິ"), None)
        current_step_uuid = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡶࡨࡴࡤࡻࡵࡪࡦࠪີ"), None)
        bstack11l1l11ll1_opy_, exception = self._11l1l11l11_opy_(attrs)
        bstack11l1l11111_opy_ = Result(result=attrs.status.name, exception=exception, bstack11l11l11ll_opy_=[bstack11l1l11ll1_opy_])
        self.tests[current_test_id][bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪຶ")].bstack11l11l1lll_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack11l1l11111_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack1l1ll111l_opy_(self, name, attrs):
        try:
            bstack11l1l111ll_opy_ = uuid4().__str__()
            self.tests[bstack11l1l111ll_opy_] = {}
            self.bstack11l11l1111_opy_.start()
            scopes = []
            driver = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧື"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1l1l111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹຸࠧ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l1l111ll_opy_)
            if name in [bstack1l1l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲູࠢ"), bstack1l1l111_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲ຺ࠢ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1l1l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨົ"), bstack1l1l111_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪࠨຼ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1l1l111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨຽ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack11l11lll11_opy_(
                name=name,
                uuid=bstack11l1l111ll_opy_,
                started_at=bstack1ll11l1ll1_opy_(),
                file_path=file_path,
                framework=bstack1l1l111_opy_ (u"ࠣࡄࡨ࡬ࡦࡼࡥࠣ຾"),
                bstack11l111llll_opy_=bstack1l11l11lll_opy_.bstack11l111ll1l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1l1l111_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥ຿"),
                hook_type=name
            )
            self.tests[bstack11l1l111ll_opy_][bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡤࡸࡦࠨເ")] = hook_data
            current_test_id = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠦࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣແ"), None)
            if current_test_id:
                hook_data.bstack11l11l11l1_opy_(current_test_id)
            if name == bstack1l1l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤໂ"):
                threading.current_thread().before_all_hook_uuid = bstack11l1l111ll_opy_
            threading.current_thread().current_hook_uuid = bstack11l1l111ll_opy_
            bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠨࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠢໃ"), hook_data)
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡬ࡴࡵ࡫ࠡࡧࡹࡩࡳࡺࡳ࠭ࠢ࡫ࡳࡴࡱࠠ࡯ࡣࡰࡩ࠿ࠦࠥࡴ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠩࡸࠨໄ"), name, e)
    def bstack11ll1111ll_opy_(self, attrs):
        bstack11l1l1111l_opy_ = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ໅"), None)
        hook_data = self.tests[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬໆ")]
        status = bstack1l1l111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ໇")
        exception = None
        bstack11l1l11ll1_opy_ = None
        if hook_data.name == bstack1l1l111_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡢࡥࡱࡲ່ࠢ"):
            self.bstack11l11l1111_opy_.reset()
            bstack11l11ll1l1_opy_ = self.tests[bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨ້ࠬ"), None)][bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢ໊ࠩ")].result.result
            if bstack11l11ll1l1_opy_ == bstack1l1l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ໋ࠢ"):
                if attrs.hook_failures == 1:
                    status = bstack1l1l111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ໌")
                elif attrs.hook_failures == 2:
                    status = bstack1l1l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤໍ")
            elif attrs.bstack11l111lll1_opy_:
                status = bstack1l1l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ໎")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1l1l111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨ໏") and attrs.hook_failures == 1:
                status = bstack1l1l111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ໐")
            elif hasattr(attrs, bstack1l1l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࡤࡳࡥࡴࡵࡤ࡫ࡪ࠭໑")) and attrs.error_message:
                status = bstack1l1l111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ໒")
            bstack11l1l11ll1_opy_, exception = self._11l1l11l11_opy_(attrs)
        bstack11l1l11111_opy_ = Result(result=status, exception=exception, bstack11l11l11ll_opy_=[bstack11l1l11ll1_opy_])
        hook_data.stop(time=bstack1ll11l1ll1_opy_(), duration=0, result=bstack11l1l11111_opy_)
        bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ໓"), self.tests[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ໔")])
        threading.current_thread().current_hook_uuid = None
    def _11l1l11l11_opy_(self, attrs):
        try:
            import traceback
            bstack1lllll1lll_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l1l11ll1_opy_ = bstack1lllll1lll_opy_[-1] if bstack1lllll1lll_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡳࡵࡱࡰࠤࡹࡸࡡࡤࡧࡥࡥࡨࡱࠢ໕"))
            bstack11l1l11ll1_opy_ = None
            exception = None
        return bstack11l1l11ll1_opy_, exception