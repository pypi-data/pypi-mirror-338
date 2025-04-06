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
from uuid import uuid4
from bstack_utils.helper import bstack1ll11l1ll1_opy_, bstack11llll1ll1l_opy_
from bstack_utils.bstack1l1l1lll11_opy_ import bstack11l1111l1l1_opy_
class bstack111lll11ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111ll1lllll_opy_=None, bstack111lll1l11l_opy_=True, bstack1l1l11lll11_opy_=None, bstack1l11ll1111_opy_=None, result=None, duration=None, bstack111ll1l111_opy_=None, meta={}):
        self.bstack111ll1l111_opy_ = bstack111ll1l111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111lll1l11l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111ll1lllll_opy_ = bstack111ll1lllll_opy_
        self.bstack1l1l11lll11_opy_ = bstack1l1l11lll11_opy_
        self.bstack1l11ll1111_opy_ = bstack1l11ll1111_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack111llll111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11llll1_opy_(self, meta):
        self.meta = meta
    def bstack11l11l1l11_opy_(self, hooks):
        self.hooks = hooks
    def bstack111lll111ll_opy_(self):
        bstack111lll1l1ll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l1l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᲓ"): bstack111lll1l1ll_opy_,
            bstack1l1l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᲔ"): bstack111lll1l1ll_opy_,
            bstack1l1l111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᲕ"): bstack111lll1l1ll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l1l111_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᲖ") + key)
            setattr(self, key, val)
    def bstack111lll1l1l1_opy_(self):
        return {
            bstack1l1l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᲗ"): self.name,
            bstack1l1l111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᲘ"): {
                bstack1l1l111_opy_ (u"࠭࡬ࡢࡰࡪࠫᲙ"): bstack1l1l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᲚ"),
                bstack1l1l111_opy_ (u"ࠨࡥࡲࡨࡪ࠭Მ"): self.code
            },
            bstack1l1l111_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᲜ"): self.scope,
            bstack1l1l111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᲝ"): self.tags,
            bstack1l1l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᲞ"): self.framework,
            bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᲟ"): self.started_at
        }
    def bstack111lll1l111_opy_(self):
        return {
         bstack1l1l111_opy_ (u"࠭࡭ࡦࡶࡤࠫᲠ"): self.meta
        }
    def bstack111lll11l11_opy_(self):
        return {
            bstack1l1l111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᲡ"): {
                bstack1l1l111_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᲢ"): self.bstack111ll1lllll_opy_
            }
        }
    def bstack111lll11lll_opy_(self, bstack111lll11ll1_opy_, details):
        step = next(filter(lambda st: st[bstack1l1l111_opy_ (u"ࠩ࡬ࡨࠬᲣ")] == bstack111lll11ll1_opy_, self.meta[bstack1l1l111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᲤ")]), None)
        step.update(details)
    def bstack1ll1l1ll1_opy_(self, bstack111lll11ll1_opy_):
        step = next(filter(lambda st: st[bstack1l1l111_opy_ (u"ࠫ࡮ࡪࠧᲥ")] == bstack111lll11ll1_opy_, self.meta[bstack1l1l111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᲦ")]), None)
        step.update({
            bstack1l1l111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᲧ"): bstack1ll11l1ll1_opy_()
        })
    def bstack11l11l1lll_opy_(self, bstack111lll11ll1_opy_, result, duration=None):
        bstack1l1l11lll11_opy_ = bstack1ll11l1ll1_opy_()
        if bstack111lll11ll1_opy_ is not None and self.meta.get(bstack1l1l111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Შ")):
            step = next(filter(lambda st: st[bstack1l1l111_opy_ (u"ࠨ࡫ࡧࠫᲩ")] == bstack111lll11ll1_opy_, self.meta[bstack1l1l111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᲪ")]), None)
            step.update({
                bstack1l1l111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᲫ"): bstack1l1l11lll11_opy_,
                bstack1l1l111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭Წ"): duration if duration else bstack11llll1ll1l_opy_(step[bstack1l1l111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᲭ")], bstack1l1l11lll11_opy_),
                bstack1l1l111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭Ხ"): result.result,
                bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᲯ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111ll1lll11_opy_):
        if self.meta.get(bstack1l1l111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᲰ")):
            self.meta[bstack1l1l111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᲱ")].append(bstack111ll1lll11_opy_)
        else:
            self.meta[bstack1l1l111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᲲ")] = [ bstack111ll1lll11_opy_ ]
    def bstack111ll1lll1l_opy_(self):
        return {
            bstack1l1l111_opy_ (u"ࠫࡺࡻࡩࡥࠩᲳ"): self.bstack111llll111_opy_(),
            **self.bstack111lll1l1l1_opy_(),
            **self.bstack111lll111ll_opy_(),
            **self.bstack111lll1l111_opy_()
        }
    def bstack111ll1llll1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l1l111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᲴ"): self.bstack1l1l11lll11_opy_,
            bstack1l1l111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᲵ"): self.duration,
            bstack1l1l111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᲶ"): self.result.result
        }
        if data[bstack1l1l111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᲷ")] == bstack1l1l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᲸ"):
            data[bstack1l1l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᲹ")] = self.result.bstack111l111ll1_opy_()
            data[bstack1l1l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᲺ")] = [{bstack1l1l111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ᲻"): self.result.bstack11ll1l11l11_opy_()}]
        return data
    def bstack111lll1ll1l_opy_(self):
        return {
            bstack1l1l111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ᲼"): self.bstack111llll111_opy_(),
            **self.bstack111lll1l1l1_opy_(),
            **self.bstack111lll111ll_opy_(),
            **self.bstack111ll1llll1_opy_(),
            **self.bstack111lll1l111_opy_()
        }
    def bstack11l1111ll1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l1l111_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨᲽ") in event:
            return self.bstack111ll1lll1l_opy_()
        elif bstack1l1l111_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᲾ") in event:
            return self.bstack111lll1ll1l_opy_()
    def bstack11l1111111_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l1l11lll11_opy_ = time if time else bstack1ll11l1ll1_opy_()
        self.duration = duration if duration else bstack11llll1ll1l_opy_(self.started_at, self.bstack1l1l11lll11_opy_)
        if result:
            self.result = result
class bstack11l1l11l1l_opy_(bstack111lll11ll_opy_):
    def __init__(self, hooks=[], bstack11l111llll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11l111llll_opy_ = bstack11l111llll_opy_
        super().__init__(*args, **kwargs, bstack1l11ll1111_opy_=bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺࠧᲿ"))
    @classmethod
    def bstack111lll11l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1l111_opy_ (u"ࠪ࡭ࡩ࠭᳀"): id(step),
                bstack1l1l111_opy_ (u"ࠫࡹ࡫ࡸࡵࠩ᳁"): step.name,
                bstack1l1l111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭᳂"): step.keyword,
            })
        return bstack11l1l11l1l_opy_(
            **kwargs,
            meta={
                bstack1l1l111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧ᳃"): {
                    bstack1l1l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ᳄"): feature.name,
                    bstack1l1l111_opy_ (u"ࠨࡲࡤࡸ࡭࠭᳅"): feature.filename,
                    bstack1l1l111_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ᳆"): feature.description
                },
                bstack1l1l111_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ᳇"): {
                    bstack1l1l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᳈"): scenario.name
                },
                bstack1l1l111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫ᳉"): steps,
                bstack1l1l111_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨ᳊"): bstack11l1111l1l1_opy_(test)
            }
        )
    def bstack111lll1111l_opy_(self):
        return {
            bstack1l1l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭᳋"): self.hooks
        }
    def bstack111lll11111_opy_(self):
        if self.bstack11l111llll_opy_:
            return {
                bstack1l1l111_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧ᳌"): self.bstack11l111llll_opy_
            }
        return {}
    def bstack111lll1ll1l_opy_(self):
        return {
            **super().bstack111lll1ll1l_opy_(),
            **self.bstack111lll1111l_opy_()
        }
    def bstack111ll1lll1l_opy_(self):
        return {
            **super().bstack111ll1lll1l_opy_(),
            **self.bstack111lll11111_opy_()
        }
    def bstack11l1111111_opy_(self):
        return bstack1l1l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ᳍")
class bstack11l11lll11_opy_(bstack111lll11ll_opy_):
    def __init__(self, hook_type, *args,bstack11l111llll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack111lll1ll11_opy_ = None
        self.bstack11l111llll_opy_ = bstack11l111llll_opy_
        super().__init__(*args, **kwargs, bstack1l11ll1111_opy_=bstack1l1l111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ᳎"))
    def bstack111lll1ll1_opy_(self):
        return self.hook_type
    def bstack111lll111l1_opy_(self):
        return {
            bstack1l1l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ᳏"): self.hook_type
        }
    def bstack111lll1ll1l_opy_(self):
        return {
            **super().bstack111lll1ll1l_opy_(),
            **self.bstack111lll111l1_opy_()
        }
    def bstack111ll1lll1l_opy_(self):
        return {
            **super().bstack111ll1lll1l_opy_(),
            bstack1l1l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪ᳐"): self.bstack111lll1ll11_opy_,
            **self.bstack111lll111l1_opy_()
        }
    def bstack11l1111111_opy_(self):
        return bstack1l1l111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ᳑")
    def bstack11l11l11l1_opy_(self, bstack111lll1ll11_opy_):
        self.bstack111lll1ll11_opy_ = bstack111lll1ll11_opy_