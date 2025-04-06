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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack111ll1llll_opy_ import RobotHandler
from bstack_utils.capture import bstack11l11lll1l_opy_
from bstack_utils.bstack11l11lllll_opy_ import bstack111lll11ll_opy_, bstack11l11lll11_opy_, bstack11l1l11l1l_opy_
from bstack_utils.bstack11l11ll1ll_opy_ import bstack1l1lll1lll_opy_
from bstack_utils.bstack11l11l1l1l_opy_ import bstack1l11l11lll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l11ll111l_opy_, bstack1ll11l1ll1_opy_, Result, \
    bstack111lllll1l_opy_, bstack111ll1111l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ໖"): [],
        bstack1l1l111_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫ໗"): [],
        bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪ໘"): []
    }
    bstack111lllll11_opy_ = []
    bstack111lll1lll_opy_ = []
    @staticmethod
    def bstack11l1l111l1_opy_(log):
        if not ((isinstance(log[bstack1l1l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ໙")], list) or (isinstance(log[bstack1l1l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ໚")], dict)) and len(log[bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ໛")])>0) or (isinstance(log[bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫໜ")], str) and log[bstack1l1l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬໝ")].strip())):
            return
        active = bstack1l1lll1lll_opy_.bstack11l11l1ll1_opy_()
        log = {
            bstack1l1l111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫໞ"): log[bstack1l1l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬໟ")],
            bstack1l1l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ໠"): bstack111ll1111l_opy_().isoformat() + bstack1l1l111_opy_ (u"ࠨ࡜ࠪ໡"),
            bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ໢"): log[bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ໣")],
        }
        if active:
            if active[bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩ໤")] == bstack1l1l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ໥"):
                log[bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭໦")] = active[bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ໧")]
            elif active[bstack1l1l111_opy_ (u"ࠨࡶࡼࡴࡪ࠭໨")] == bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺࠧ໩"):
                log[bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ໪")] = active[bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ໫")]
        bstack1l11l11lll_opy_.bstack11l11lll1_opy_([log])
    def __init__(self):
        self.messages = bstack111lll11l1_opy_()
        self._11l111l1l1_opy_ = None
        self._11l111l11l_opy_ = None
        self._111ll11ll1_opy_ = OrderedDict()
        self.bstack11l11l1111_opy_ = bstack11l11lll1l_opy_(self.bstack11l1l111l1_opy_)
    @bstack111lllll1l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack111ll111ll_opy_()
        if not self._111ll11ll1_opy_.get(attrs.get(bstack1l1l111_opy_ (u"ࠬ࡯ࡤࠨ໬")), None):
            self._111ll11ll1_opy_[attrs.get(bstack1l1l111_opy_ (u"࠭ࡩࡥࠩ໭"))] = {}
        bstack111l1lll1l_opy_ = bstack11l1l11l1l_opy_(
                bstack111ll1l111_opy_=attrs.get(bstack1l1l111_opy_ (u"ࠧࡪࡦࠪ໮")),
                name=name,
                started_at=bstack1ll11l1ll1_opy_(),
                file_path=os.path.relpath(attrs[bstack1l1l111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ໯")], start=os.getcwd()) if attrs.get(bstack1l1l111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ໰")) != bstack1l1l111_opy_ (u"ࠪࠫ໱") else bstack1l1l111_opy_ (u"ࠫࠬ໲"),
                framework=bstack1l1l111_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ໳")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack1l1l111_opy_ (u"࠭ࡩࡥࠩ໴"), None)
        self._111ll11ll1_opy_[attrs.get(bstack1l1l111_opy_ (u"ࠧࡪࡦࠪ໵"))][bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ໶")] = bstack111l1lll1l_opy_
    @bstack111lllll1l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack111ll1l11l_opy_()
        self._111llll1l1_opy_(messages)
        for bstack111ll1ll11_opy_ in self.bstack111lllll11_opy_:
            bstack111ll1ll11_opy_[bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ໷")][bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ໸")].extend(self.store[bstack1l1l111_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪ໹")])
            bstack1l11l11lll_opy_.bstack111ll111l_opy_(bstack111ll1ll11_opy_)
        self.bstack111lllll11_opy_ = []
        self.store[bstack1l1l111_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫ໺")] = []
    @bstack111lllll1l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11l11l1111_opy_.start()
        if not self._111ll11ll1_opy_.get(attrs.get(bstack1l1l111_opy_ (u"࠭ࡩࡥࠩ໻")), None):
            self._111ll11ll1_opy_[attrs.get(bstack1l1l111_opy_ (u"ࠧࡪࡦࠪ໼"))] = {}
        driver = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ໽"), None)
        bstack11l11lllll_opy_ = bstack11l1l11l1l_opy_(
            bstack111ll1l111_opy_=attrs.get(bstack1l1l111_opy_ (u"ࠩ࡬ࡨࠬ໾")),
            name=name,
            started_at=bstack1ll11l1ll1_opy_(),
            file_path=os.path.relpath(attrs[bstack1l1l111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໿")], start=os.getcwd()),
            scope=RobotHandler.bstack11l111111l_opy_(attrs.get(bstack1l1l111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫༀ"), None)),
            framework=bstack1l1l111_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ༁"),
            tags=attrs[bstack1l1l111_opy_ (u"࠭ࡴࡢࡩࡶࠫ༂")],
            hooks=self.store[bstack1l1l111_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭༃")],
            bstack11l111llll_opy_=bstack1l11l11lll_opy_.bstack11l111ll1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack1l1l111_opy_ (u"ࠣࡽࢀࠤࡡࡴࠠࡼࡿࠥ༄").format(bstack1l1l111_opy_ (u"ࠤࠣࠦ༅").join(attrs[bstack1l1l111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ༆")]), name) if attrs[bstack1l1l111_opy_ (u"ࠫࡹࡧࡧࡴࠩ༇")] else name
        )
        self._111ll11ll1_opy_[attrs.get(bstack1l1l111_opy_ (u"ࠬ࡯ࡤࠨ༈"))][bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ༉")] = bstack11l11lllll_opy_
        threading.current_thread().current_test_uuid = bstack11l11lllll_opy_.bstack111llll111_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack1l1l111_opy_ (u"ࠧࡪࡦࠪ༊"), None)
        self.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ་"), bstack11l11lllll_opy_)
    @bstack111lllll1l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11l11l1111_opy_.reset()
        bstack111lll1111_opy_ = bstack111lll1l1l_opy_.get(attrs.get(bstack1l1l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ༌")), bstack1l1l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ།"))
        self._111ll11ll1_opy_[attrs.get(bstack1l1l111_opy_ (u"ࠫ࡮ࡪࠧ༎"))][bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ༏")].stop(time=bstack1ll11l1ll1_opy_(), duration=int(attrs.get(bstack1l1l111_opy_ (u"࠭ࡥ࡭ࡣࡳࡷࡪࡪࡴࡪ࡯ࡨࠫ༐"), bstack1l1l111_opy_ (u"ࠧ࠱ࠩ༑"))), result=Result(result=bstack111lll1111_opy_, exception=attrs.get(bstack1l1l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ༒")), bstack11l11l11ll_opy_=[attrs.get(bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ༓"))]))
        self.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ༔"), self._111ll11ll1_opy_[attrs.get(bstack1l1l111_opy_ (u"ࠫ࡮ࡪࠧ༕"))][bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ༖")], True)
        self.store[bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪ༗")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack111lllll1l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack111ll111ll_opy_()
        current_test_id = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥ༘ࠩ"), None)
        bstack11l1111lll_opy_ = current_test_id if bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡦ༙ࠪ"), None) else bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡺ࡯ࡴࡦࡡ࡬ࡨࠬ༚"), None)
        if attrs.get(bstack1l1l111_opy_ (u"ࠪࡸࡾࡶࡥࠨ༛"), bstack1l1l111_opy_ (u"ࠫࠬ༜")).lower() in [bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ༝"), bstack1l1l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ༞")]:
            hook_type = bstack111lll111l_opy_(attrs.get(bstack1l1l111_opy_ (u"ࠧࡵࡻࡳࡩࠬ༟")), bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ༠"), None))
            hook_name = bstack1l1l111_opy_ (u"ࠩࡾࢁࠬ༡").format(attrs.get(bstack1l1l111_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪ༢"), bstack1l1l111_opy_ (u"ࠫࠬ༣")))
            if hook_type in [bstack1l1l111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩ༤"), bstack1l1l111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩ༥")]:
                hook_name = bstack1l1l111_opy_ (u"ࠧ࡜ࡽࢀࡡࠥࢁࡽࠨ༦").format(bstack111llll1ll_opy_.get(hook_type), attrs.get(bstack1l1l111_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨ༧"), bstack1l1l111_opy_ (u"ࠩࠪ༨")))
            bstack111lllllll_opy_ = bstack11l11lll11_opy_(
                bstack111ll1l111_opy_=bstack11l1111lll_opy_ + bstack1l1l111_opy_ (u"ࠪ࠱ࠬ༩") + attrs.get(bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩ༪"), bstack1l1l111_opy_ (u"ࠬ࠭༫")).lower(),
                name=hook_name,
                started_at=bstack1ll11l1ll1_opy_(),
                file_path=os.path.relpath(attrs.get(bstack1l1l111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭༬")), start=os.getcwd()),
                framework=bstack1l1l111_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭༭"),
                tags=attrs[bstack1l1l111_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭༮")],
                scope=RobotHandler.bstack11l111111l_opy_(attrs.get(bstack1l1l111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ༯"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack111lllllll_opy_.bstack111llll111_opy_()
            threading.current_thread().current_hook_id = bstack11l1111lll_opy_ + bstack1l1l111_opy_ (u"ࠪ࠱ࠬ༰") + attrs.get(bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩ༱"), bstack1l1l111_opy_ (u"ࠬ࠭༲")).lower()
            self.store[bstack1l1l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ༳")] = [bstack111lllllll_opy_.bstack111llll111_opy_()]
            if bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ༴"), None):
                self.store[bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷ༵ࠬ")].append(bstack111lllllll_opy_.bstack111llll111_opy_())
            else:
                self.store[bstack1l1l111_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨ༶")].append(bstack111lllllll_opy_.bstack111llll111_opy_())
            if bstack11l1111lll_opy_:
                self._111ll11ll1_opy_[bstack11l1111lll_opy_ + bstack1l1l111_opy_ (u"ࠪ࠱༷ࠬ") + attrs.get(bstack1l1l111_opy_ (u"ࠫࡹࡿࡰࡦࠩ༸"), bstack1l1l111_opy_ (u"༹ࠬ࠭")).lower()] = { bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ༺"): bstack111lllllll_opy_ }
            bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ༻"), bstack111lllllll_opy_)
        else:
            bstack11l11ll111_opy_ = {
                bstack1l1l111_opy_ (u"ࠨ࡫ࡧࠫ༼"): uuid4().__str__(),
                bstack1l1l111_opy_ (u"ࠩࡷࡩࡽࡺࠧ༽"): bstack1l1l111_opy_ (u"ࠪࡿࢂࠦࡻࡾࠩ༾").format(attrs.get(bstack1l1l111_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫ༿")), attrs.get(bstack1l1l111_opy_ (u"ࠬࡧࡲࡨࡵࠪཀ"), bstack1l1l111_opy_ (u"࠭ࠧཁ"))) if attrs.get(bstack1l1l111_opy_ (u"ࠧࡢࡴࡪࡷࠬག"), []) else attrs.get(bstack1l1l111_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨགྷ")),
                bstack1l1l111_opy_ (u"ࠩࡶࡸࡪࡶ࡟ࡢࡴࡪࡹࡲ࡫࡮ࡵࠩང"): attrs.get(bstack1l1l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨཅ"), []),
                bstack1l1l111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨཆ"): bstack1ll11l1ll1_opy_(),
                bstack1l1l111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬཇ"): bstack1l1l111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ཈"),
                bstack1l1l111_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬཉ"): attrs.get(bstack1l1l111_opy_ (u"ࠨࡦࡲࡧࠬཊ"), bstack1l1l111_opy_ (u"ࠩࠪཋ"))
            }
            if attrs.get(bstack1l1l111_opy_ (u"ࠪࡰ࡮ࡨ࡮ࡢ࡯ࡨࠫཌ"), bstack1l1l111_opy_ (u"ࠫࠬཌྷ")) != bstack1l1l111_opy_ (u"ࠬ࠭ཎ"):
                bstack11l11ll111_opy_[bstack1l1l111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧཏ")] = attrs.get(bstack1l1l111_opy_ (u"ࠧ࡭࡫ࡥࡲࡦࡳࡥࠨཐ"))
            if not self.bstack111lll1lll_opy_:
                self._111ll11ll1_opy_[self._111l1llll1_opy_()][bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫད")].add_step(bstack11l11ll111_opy_)
                threading.current_thread().current_step_uuid = bstack11l11ll111_opy_[bstack1l1l111_opy_ (u"ࠩ࡬ࡨࠬདྷ")]
            self.bstack111lll1lll_opy_.append(bstack11l11ll111_opy_)
    @bstack111lllll1l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack111ll1l11l_opy_()
        self._111llll1l1_opy_(messages)
        current_test_id = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬན"), None)
        bstack11l1111lll_opy_ = current_test_id if current_test_id else bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧཔ"), None)
        bstack111ll1lll1_opy_ = bstack111lll1l1l_opy_.get(attrs.get(bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬཕ")), bstack1l1l111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧབ"))
        bstack11l111l1ll_opy_ = attrs.get(bstack1l1l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨབྷ"))
        if bstack111ll1lll1_opy_ != bstack1l1l111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩམ") and not attrs.get(bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪཙ")) and self._11l111l1l1_opy_:
            bstack11l111l1ll_opy_ = self._11l111l1l1_opy_
        bstack11l1l11111_opy_ = Result(result=bstack111ll1lll1_opy_, exception=bstack11l111l1ll_opy_, bstack11l11l11ll_opy_=[bstack11l111l1ll_opy_])
        if attrs.get(bstack1l1l111_opy_ (u"ࠪࡸࡾࡶࡥࠨཚ"), bstack1l1l111_opy_ (u"ࠫࠬཛ")).lower() in [bstack1l1l111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫཛྷ"), bstack1l1l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨཝ")]:
            bstack11l1111lll_opy_ = current_test_id if current_test_id else bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡸ࡭ࡹ࡫࡟ࡪࡦࠪཞ"), None)
            if bstack11l1111lll_opy_:
                bstack11l1l1111l_opy_ = bstack11l1111lll_opy_ + bstack1l1l111_opy_ (u"ࠣ࠯ࠥཟ") + attrs.get(bstack1l1l111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧའ"), bstack1l1l111_opy_ (u"ࠪࠫཡ")).lower()
                self._111ll11ll1_opy_[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧར")].stop(time=bstack1ll11l1ll1_opy_(), duration=int(attrs.get(bstack1l1l111_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪལ"), bstack1l1l111_opy_ (u"࠭࠰ࠨཤ"))), result=bstack11l1l11111_opy_)
                bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(bstack1l1l111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩཥ"), self._111ll11ll1_opy_[bstack11l1l1111l_opy_][bstack1l1l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫས")])
        else:
            bstack11l1111lll_opy_ = current_test_id if current_test_id else bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠ࡫ࡧࠫཧ"), None)
            if bstack11l1111lll_opy_ and len(self.bstack111lll1lll_opy_) == 1:
                current_step_uuid = bstack1l11ll111l_opy_(threading.current_thread(), bstack1l1l111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧཨ"), None)
                self._111ll11ll1_opy_[bstack11l1111lll_opy_][bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧཀྵ")].bstack11l11l1lll_opy_(current_step_uuid, duration=int(attrs.get(bstack1l1l111_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪཪ"), bstack1l1l111_opy_ (u"࠭࠰ࠨཫ"))), result=bstack11l1l11111_opy_)
            else:
                self.bstack11l111ll11_opy_(attrs)
            self.bstack111lll1lll_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack1l1l111_opy_ (u"ࠧࡩࡶࡰࡰࠬཬ"), bstack1l1l111_opy_ (u"ࠨࡰࡲࠫ཭")) == bstack1l1l111_opy_ (u"ࠩࡼࡩࡸ࠭཮"):
                return
            self.messages.push(message)
            logs = []
            if bstack1l1lll1lll_opy_.bstack11l11l1ll1_opy_():
                logs.append({
                    bstack1l1l111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭཯"): bstack1ll11l1ll1_opy_(),
                    bstack1l1l111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ཰"): message.get(bstack1l1l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪཱ࠭")),
                    bstack1l1l111_opy_ (u"࠭࡬ࡦࡸࡨࡰིࠬ"): message.get(bstack1l1l111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱཱི࠭")),
                    **bstack1l1lll1lll_opy_.bstack11l11l1ll1_opy_()
                })
                if len(logs) > 0:
                    bstack1l11l11lll_opy_.bstack11l11lll1_opy_(logs)
        except Exception as err:
            pass
    def close(self):
        bstack1l11l11lll_opy_.bstack11l11111l1_opy_()
    def bstack11l111ll11_opy_(self, bstack111ll11l11_opy_):
        if not bstack1l1lll1lll_opy_.bstack11l11l1ll1_opy_():
            return
        kwname = bstack1l1l111_opy_ (u"ࠨࡽࢀࠤࢀࢃུࠧ").format(bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦཱུࠩ")), bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨྲྀ"), bstack1l1l111_opy_ (u"ࠫࠬཷ"))) if bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠬࡧࡲࡨࡵࠪླྀ"), []) else bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭ཹ"))
        error_message = bstack1l1l111_opy_ (u"ࠢ࡬ࡹࡱࡥࡲ࡫࠺ࠡ࡞ࠥࡿ࠵ࢃ࡜ࠣࠢࡿࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࡢࠢࡼ࠳ࢀࡠࠧࠦࡼࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࡢࠢࡼ࠴ࢀࡠࠧࠨེ").format(kwname, bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨཻ")), str(bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧོࠪ"))))
        bstack111l1lllll_opy_ = bstack1l1l111_opy_ (u"ࠥ࡯ࡼࡴࡡ࡮ࡧ࠽ࠤࡡࠨࡻ࠱ࡿ࡟ࠦࠥࢂࠠࡴࡶࡤࡸࡺࡹ࠺ࠡ࡞ࠥࡿ࠶ࢃ࡜ࠣࠤཽ").format(kwname, bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫཾ")))
        bstack111ll11111_opy_ = error_message if bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ཿ")) else bstack111l1lllll_opy_
        bstack111llll11l_opy_ = {
            bstack1l1l111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱྀࠩ"): self.bstack111lll1lll_opy_[-1].get(bstack1l1l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷཱྀࠫ"), bstack1ll11l1ll1_opy_()),
            bstack1l1l111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩྂ"): bstack111ll11111_opy_,
            bstack1l1l111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨྃ"): bstack1l1l111_opy_ (u"ࠪࡉࡗࡘࡏࡓ྄ࠩ") if bstack111ll11l11_opy_.get(bstack1l1l111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ྅")) == bstack1l1l111_opy_ (u"ࠬࡌࡁࡊࡎࠪ྆") else bstack1l1l111_opy_ (u"࠭ࡉࡏࡈࡒࠫ྇"),
            **bstack1l1lll1lll_opy_.bstack11l11l1ll1_opy_()
        }
        bstack1l11l11lll_opy_.bstack11l11lll1_opy_([bstack111llll11l_opy_])
    def _111l1llll1_opy_(self):
        for bstack111ll1l111_opy_ in reversed(self._111ll11ll1_opy_):
            bstack111llllll1_opy_ = bstack111ll1l111_opy_
            data = self._111ll11ll1_opy_[bstack111ll1l111_opy_][bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪྈ")]
            if isinstance(data, bstack11l11lll11_opy_):
                if not bstack1l1l111_opy_ (u"ࠨࡇࡄࡇࡍ࠭ྉ") in data.bstack111lll1ll1_opy_():
                    return bstack111llllll1_opy_
            else:
                return bstack111llllll1_opy_
    def _111llll1l1_opy_(self, messages):
        try:
            bstack11l1111l11_opy_ = BuiltIn().get_variable_value(bstack1l1l111_opy_ (u"ࠤࠧࡿࡑࡕࡇࠡࡎࡈ࡚ࡊࡒࡽࠣྊ")) in (bstack11l1111l1l_opy_.DEBUG, bstack11l1111l1l_opy_.TRACE)
            for message, bstack111ll11lll_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack1l1l111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫྋ"))
                level = message.get(bstack1l1l111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪྌ"))
                if level == bstack11l1111l1l_opy_.FAIL:
                    self._11l111l1l1_opy_ = name or self._11l111l1l1_opy_
                    self._11l111l11l_opy_ = bstack111ll11lll_opy_.get(bstack1l1l111_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨྍ")) if bstack11l1111l11_opy_ and bstack111ll11lll_opy_ else self._11l111l11l_opy_
        except:
            pass
    @classmethod
    def bstack11l11ll11l_opy_(self, event: str, bstack111ll1l1ll_opy_: bstack111lll11ll_opy_, bstack11l11111ll_opy_=False):
        if event == bstack1l1l111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨྎ"):
            bstack111ll1l1ll_opy_.set(hooks=self.store[bstack1l1l111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫྏ")])
        if event == bstack1l1l111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩྐ"):
            event = bstack1l1l111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫྑ")
        if bstack11l11111ll_opy_:
            bstack111ll1ll1l_opy_ = {
                bstack1l1l111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧྒ"): event,
                bstack111ll1l1ll_opy_.bstack11l1111111_opy_(): bstack111ll1l1ll_opy_.bstack11l1111ll1_opy_(event)
            }
            self.bstack111lllll11_opy_.append(bstack111ll1ll1l_opy_)
        else:
            bstack1l11l11lll_opy_.bstack11l11ll11l_opy_(event, bstack111ll1l1ll_opy_)
class bstack111lll11l1_opy_:
    def __init__(self):
        self._111ll111l1_opy_ = []
    def bstack111ll111ll_opy_(self):
        self._111ll111l1_opy_.append([])
    def bstack111ll1l11l_opy_(self):
        return self._111ll111l1_opy_.pop() if self._111ll111l1_opy_ else list()
    def push(self, message):
        self._111ll111l1_opy_[-1].append(message) if self._111ll111l1_opy_ else self._111ll111l1_opy_.append([message])
class bstack11l1111l1l_opy_:
    FAIL = bstack1l1l111_opy_ (u"ࠫࡋࡇࡉࡍࠩྒྷ")
    ERROR = bstack1l1l111_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫྔ")
    WARNING = bstack1l1l111_opy_ (u"࠭ࡗࡂࡔࡑࠫྕ")
    bstack111ll11l1l_opy_ = bstack1l1l111_opy_ (u"ࠧࡊࡐࡉࡓࠬྖ")
    DEBUG = bstack1l1l111_opy_ (u"ࠨࡆࡈࡆ࡚ࡍࠧྗ")
    TRACE = bstack1l1l111_opy_ (u"ࠩࡗࡖࡆࡉࡅࠨ྘")
    bstack111ll1l1l1_opy_ = [FAIL, ERROR]
def bstack11l111l111_opy_(bstack111lll1l11_opy_):
    if not bstack111lll1l11_opy_:
        return None
    if bstack111lll1l11_opy_.get(bstack1l1l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ྙ"), None):
        return getattr(bstack111lll1l11_opy_[bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧྚ")], bstack1l1l111_opy_ (u"ࠬࡻࡵࡪࡦࠪྛ"), None)
    return bstack111lll1l11_opy_.get(bstack1l1l111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫྜ"), None)
def bstack111lll111l_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack1l1l111_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ྜྷ"), bstack1l1l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪྞ")]:
        return
    if hook_type.lower() == bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨྟ"):
        if current_test_uuid is None:
            return bstack1l1l111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧྠ")
        else:
            return bstack1l1l111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩྡ")
    elif hook_type.lower() == bstack1l1l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧྡྷ"):
        if current_test_uuid is None:
            return bstack1l1l111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩྣ")
        else:
            return bstack1l1l111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫྤ")