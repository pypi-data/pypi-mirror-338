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
import os
from typing import Dict, Any
from dataclasses import dataclass
from collections import defaultdict
from datetime import timedelta
@dataclass
class bstack11111l11ll_opy_:
    id: str
    hash: str
    thread_id: int
    process_id: int
    type: str
class bstack11111llll1_opy_:
    bstack1l11l11l11l_opy_ = bstack1l1l111_opy_ (u"ࠧࡨࡥ࡯ࡥ࡫ࡱࡦࡸ࡫ࠣᒇ")
    context: bstack11111l11ll_opy_
    data: Dict[str, Any]
    platform_index: int
    def __init__(self, context: bstack11111l11ll_opy_):
        self.context = context
        self.data = dict({bstack11111llll1_opy_.bstack1l11l11l11l_opy_: defaultdict(lambda: timedelta(microseconds=0))})
        self.platform_index = int(os.environ.get(bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᒈ"), bstack1l1l111_opy_ (u"ࠧ࠱ࠩᒉ")))
    def ref(self) -> str:
        return str(self.context.id)
    def bstack1111l11lll_opy_(self, target: object):
        return bstack11111llll1_opy_.create_context(target) == self.context
    def bstack1ll11lllll1_opy_(self, context: bstack11111l11ll_opy_):
        return context and context.thread_id == self.context.thread_id and context.process_id == self.context.process_id
    def bstack11ll1llll_opy_(self, key: str, value: timedelta):
        self.data[bstack11111llll1_opy_.bstack1l11l11l11l_opy_][key] += value
    def bstack1llll1l111l_opy_(self) -> dict:
        return self.data[bstack11111llll1_opy_.bstack1l11l11l11l_opy_]
    @staticmethod
    def create_context(
        target: object,
        thread_id=threading.get_ident(),
        process_id=os.getpid(),
    ):
        return bstack11111l11ll_opy_(
            id=hash(target),
            hash=hash(target),
            thread_id=thread_id,
            process_id=process_id,
            type=target,
        )