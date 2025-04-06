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
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack1ll1l11l11_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack1l11111111_opy_:
    pass
class bstack1llll1lll1_opy_:
    bstack1ll111ll11_opy_ = bstack1l1l111_opy_ (u"ࠣࡤࡲࡳࡹࡹࡴࡳࡣࡳࠦႡ")
    CONNECT = bstack1l1l111_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥႢ")
    bstack11ll11l1_opy_ = bstack1l1l111_opy_ (u"ࠥࡷ࡭ࡻࡴࡥࡱࡺࡲࠧႣ")
    CONFIG = bstack1l1l111_opy_ (u"ࠦࡨࡵ࡮ࡧ࡫ࡪࠦႤ")
    bstack1lll111l11l_opy_ = bstack1l1l111_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡴࠤႥ")
    bstack1l1l1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠨࡥࡹ࡫ࡷࠦႦ")
class bstack1lll111ll1l_opy_:
    bstack1lll111l111_opy_ = bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡳࡵࡣࡵࡸࡪࡪࠢႧ")
    FINISHED = bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤႨ")
class bstack1lll111ll11_opy_:
    bstack1lll111l111_opy_ = bstack1l1l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡸࡺࡡࡳࡶࡨࡨࠧႩ")
    FINISHED = bstack1l1l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢႪ")
class bstack1lll111l1ll_opy_:
    bstack1lll111l111_opy_ = bstack1l1l111_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡳࡵࡣࡵࡸࡪࡪࠢႫ")
    FINISHED = bstack1l1l111_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤႬ")
class bstack1lll111llll_opy_:
    bstack1lll111l1l1_opy_ = bstack1l1l111_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧႭ")
class bstack1lll111lll1_opy_:
    _1lll1ll11ll_opy_ = None
    def __new__(cls):
        if not cls._1lll1ll11ll_opy_:
            cls._1lll1ll11ll_opy_ = super(bstack1lll111lll1_opy_, cls).__new__(cls)
        return cls._1lll1ll11ll_opy_
    def __init__(self):
        self._hooks = defaultdict(lambda: defaultdict(list))
        self._lock = Lock()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def clear(self):
        with self._lock:
            self._hooks = defaultdict(list)
    def register(self, event_name, callback):
        with self._lock:
            if not callable(callback):
                raise ValueError(bstack1l1l111_opy_ (u"ࠢࡄࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡰࡹࡸࡺࠠࡣࡧࠣࡧࡦࡲ࡬ࡢࡤ࡯ࡩࠥ࡬࡯ࡳࠢࠥႮ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡔࡨ࡫࡮ࡹࡴࡦࡴ࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣႯ") + str(pid) + bstack1l1l111_opy_ (u"ࠤࠥႰ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack1l1l111_opy_ (u"ࠥࡒࡴࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࡴࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࠥ࠭ࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠬࠦࡷࡪࡶ࡫ࠤࡵ࡯ࡤࠡࠤႱ") + str(pid) + bstack1l1l111_opy_ (u"ࠦࠧႲ"))
                return
            self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡏ࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡼ࡮ࡨࡲ࠭ࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠪࡿࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨႳ") + str(pid) + bstack1l1l111_opy_ (u"ࠨࠢႴ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡊࡰࡹࡳࡰ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࠦࠧࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂ࠭ࠠࡸ࡫ࡷ࡬ࠥࡶࡩࡥࠢࠥႵ") + str(pid) + bstack1l1l111_opy_ (u"ࠣࠤႶ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack1l1l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࢀࡶࡩࡥࡿ࠽ࠤࠧႷ") + str(e) + bstack1l1l111_opy_ (u"ࠥࠦႸ"))
                    traceback.print_exc()
bstack11lll1l1_opy_ = bstack1lll111lll1_opy_()