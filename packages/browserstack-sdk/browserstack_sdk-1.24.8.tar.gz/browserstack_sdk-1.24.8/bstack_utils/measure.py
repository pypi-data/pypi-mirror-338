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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1111ll11l_opy_ import get_logger
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll11ll11_opy_
bstack1111l1ll1_opy_ = bstack1llll11ll11_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1ll1l1l11_opy_: Optional[str] = None):
    bstack1l1l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡈࡪࡩ࡯ࡳࡣࡷࡳࡷࠦࡴࡰࠢ࡯ࡳ࡬ࠦࡴࡩࡧࠣࡷࡹࡧࡲࡵࠢࡷ࡭ࡲ࡫ࠠࡰࡨࠣࡥࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠍࠤࠥࠦࠠࡢ࡮ࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࠣࡲࡦࡳࡥࠡࡣࡱࡨࠥࡹࡴࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᬕ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1ll11lll_opy_: str = bstack1111l1ll1_opy_.bstack1l111ll1ll1_opy_(label)
            start_mark: str = label + bstack1l1l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᬖ")
            end_mark: str = label + bstack1l1l111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᬗ")
            result = None
            try:
                if stage.value == STAGE.bstack1l111lllll_opy_.value:
                    bstack1111l1ll1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1111l1ll1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1ll1l1l11_opy_)
                elif stage.value == STAGE.bstack1l1l1111l_opy_.value:
                    start_mark: str = bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᬘ")
                    end_mark: str = bstack1ll1ll11lll_opy_ + bstack1l1l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᬙ")
                    bstack1111l1ll1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1111l1ll1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1ll1l1l11_opy_)
            except Exception as e:
                bstack1111l1ll1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1ll1l1l11_opy_)
            return result
        return wrapper
    return decorator