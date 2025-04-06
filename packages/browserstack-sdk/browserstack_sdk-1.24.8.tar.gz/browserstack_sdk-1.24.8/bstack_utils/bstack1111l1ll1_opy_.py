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
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1111ll11l_opy_ import get_logger
logger = get_logger(__name__)
bstack11l111lll11_opy_: Dict[str, float] = {}
bstack11l111ll11l_opy_: List = []
bstack11l111ll1ll_opy_ = 5
bstack1l1111ll11_opy_ = os.path.join(os.getcwd(), bstack1l1l111_opy_ (u"ࠩ࡯ࡳ࡬᯦࠭"), bstack1l1l111_opy_ (u"ࠪ࡯ࡪࡿ࠭࡮ࡧࡷࡶ࡮ࡩࡳ࠯࡬ࡶࡳࡳ࠭ᯧ"))
logging.getLogger(bstack1l1l111_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰ࠭ᯨ")).setLevel(logging.WARNING)
lock = FileLock(bstack1l1111ll11_opy_+bstack1l1l111_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᯩ"))
class bstack11l111ll1l1_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    cli: Optional[bool]
    def __init__(self, duration: float, name: str, start_time: float, bstack11l111llll1_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11l111llll1_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1l1l111_opy_ (u"ࠨ࡭ࡦࡣࡶࡹࡷ࡫ࠢᯪ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll11ll11_opy_:
    global bstack11l111lll11_opy_
    @staticmethod
    def bstack1ll1lll1111_opy_(key: str):
        bstack1ll1ll11lll_opy_ = bstack1llll11ll11_opy_.bstack1l111ll1ll1_opy_(key)
        bstack1llll11ll11_opy_.mark(bstack1ll1ll11lll_opy_+bstack1l1l111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᯫ"))
        return bstack1ll1ll11lll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11l111lll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᯬ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll11ll11_opy_.mark(end)
            bstack1llll11ll11_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᯭ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11l111lll11_opy_ or end not in bstack11l111lll11_opy_:
                logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡴࡢࡴࡷࠤࡰ࡫ࡹࠡࡹ࡬ࡸ࡭ࠦࡶࡢ࡮ࡸࡩࠥࢁࡽࠡࡱࡵࠤࡪࡴࡤࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠧᯮ").format(start,end))
                return
            duration: float = bstack11l111lll11_opy_[end] - bstack11l111lll11_opy_[start]
            bstack11l111l1lll_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢᯯ"), bstack1l1l111_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᯰ")).lower() == bstack1l1l111_opy_ (u"ࠨࡴࡳࡷࡨࠦᯱ")
            bstack11l111ll111_opy_: bstack11l111ll1l1_opy_ = bstack11l111ll1l1_opy_(duration, label, bstack11l111lll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1l1l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞᯲ࠢ"), 0), command, test_name, hook_type, bstack11l111l1lll_opy_)
            del bstack11l111lll11_opy_[start]
            del bstack11l111lll11_opy_[end]
            bstack1llll11ll11_opy_.bstack11l111l1ll1_opy_(bstack11l111ll111_opy_)
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡦࡣࡶࡹࡷ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹ࠺ࠡࡽࢀ᯳ࠦ").format(e))
    @staticmethod
    def bstack11l111l1ll1_opy_(bstack11l111ll111_opy_):
        os.makedirs(os.path.dirname(bstack1l1111ll11_opy_)) if not os.path.exists(os.path.dirname(bstack1l1111ll11_opy_)) else None
        bstack1llll11ll11_opy_.bstack11l111lll1l_opy_()
        try:
            with lock:
                with open(bstack1l1111ll11_opy_, bstack1l1l111_opy_ (u"ࠤࡵ࠯ࠧ᯴"), encoding=bstack1l1l111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤ᯵")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11l111ll111_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11l111lllll_opy_:
            logger.debug(bstack1l1l111_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠥࢁࡽࠣ᯶").format(bstack11l111lllll_opy_))
            with lock:
                with open(bstack1l1111ll11_opy_, bstack1l1l111_opy_ (u"ࠧࡽࠢ᯷"), encoding=bstack1l1l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧ᯸")) as file:
                    data = [bstack11l111ll111_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡢࡲࡳࡩࡳࡪࠠࡼࡿࠥ᯹").format(str(e)))
        finally:
            if os.path.exists(bstack1l1111ll11_opy_+bstack1l1l111_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢ᯺")):
                os.remove(bstack1l1111ll11_opy_+bstack1l1l111_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣ᯻"))
    @staticmethod
    def bstack11l111lll1l_opy_():
        attempt = 0
        while (attempt < bstack11l111ll1ll_opy_):
            attempt += 1
            if os.path.exists(bstack1l1111ll11_opy_+bstack1l1l111_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤ᯼")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack1l111ll1ll1_opy_(label: str) -> str:
        try:
            return bstack1l1l111_opy_ (u"ࠦࢀࢃ࠺ࡼࡿࠥ᯽").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ᯾").format(e))