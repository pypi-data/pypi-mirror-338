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
import json
class bstack1l111l1ll11_opy_(object):
  bstack1l111l111l_opy_ = os.path.join(os.path.expanduser(bstack1l1l111_opy_ (u"ࠧࡿࠩᔿ")), bstack1l1l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᕀ"))
  bstack1l111l1ll1l_opy_ = os.path.join(bstack1l111l111l_opy_, bstack1l1l111_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩᕁ"))
  commands_to_wrap = None
  perform_scan = None
  bstack11llllll_opy_ = None
  bstack1l11111l11_opy_ = None
  bstack1l111l1lll1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l1l111_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬᕂ")):
      cls.instance = super(bstack1l111l1ll11_opy_, cls).__new__(cls)
      cls.instance.bstack1l111l1l1l1_opy_()
    return cls.instance
  def bstack1l111l1l1l1_opy_(self):
    try:
      with open(self.bstack1l111l1ll1l_opy_, bstack1l1l111_opy_ (u"ࠫࡷ࠭ᕃ")) as bstack1ll11l1l1l_opy_:
        bstack1l111l1l1ll_opy_ = bstack1ll11l1l1l_opy_.read()
        data = json.loads(bstack1l111l1l1ll_opy_)
        if bstack1l1l111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᕄ") in data:
          self.bstack1l111lll11l_opy_(data[bstack1l1l111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨᕅ")])
        if bstack1l1l111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᕆ") in data:
          self.bstack1l111lll111_opy_(data[bstack1l1l111_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩᕇ")])
    except:
      pass
  def bstack1l111lll111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack1l1l111_opy_ (u"ࠩࡶࡧࡦࡴࠧᕈ")]
      self.bstack11llllll_opy_ = scripts[bstack1l1l111_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧᕉ")]
      self.bstack1l11111l11_opy_ = scripts[bstack1l1l111_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨᕊ")]
      self.bstack1l111l1lll1_opy_ = scripts[bstack1l1l111_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᕋ")]
  def bstack1l111lll11l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1l111l1ll1l_opy_, bstack1l1l111_opy_ (u"࠭ࡷࠨᕌ")) as file:
        json.dump({
          bstack1l1l111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤᕍ"): self.commands_to_wrap,
          bstack1l1l111_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤᕎ"): {
            bstack1l1l111_opy_ (u"ࠤࡶࡧࡦࡴࠢᕏ"): self.perform_scan,
            bstack1l1l111_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢᕐ"): self.bstack11llllll_opy_,
            bstack1l1l111_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣᕑ"): self.bstack1l11111l11_opy_,
            bstack1l1l111_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥᕒ"): self.bstack1l111l1lll1_opy_
          }
        }, file)
    except:
      pass
  def bstack1ll11l1ll_opy_(self, bstack1lll11111ll_opy_):
    try:
      return any(command.get(bstack1l1l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᕓ")) == bstack1lll11111ll_opy_ for command in self.commands_to_wrap)
    except:
      return False
bstack11l1l1ll1l_opy_ = bstack1l111l1ll11_opy_()