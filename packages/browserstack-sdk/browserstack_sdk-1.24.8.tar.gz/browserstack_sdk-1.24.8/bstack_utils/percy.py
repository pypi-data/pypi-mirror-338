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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11ll1111_opy_, bstack1l1l1lll_opy_
from bstack_utils.measure import measure
class bstack1lll1l1l1l_opy_:
  working_dir = os.getcwd()
  bstack1llll111l1_opy_ = False
  config = {}
  bstack11lll1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠪࠫ᭢")
  binary_path = bstack1l1l111_opy_ (u"ࠫࠬ᭣")
  bstack11l11ll1l1l_opy_ = bstack1l1l111_opy_ (u"ࠬ࠭᭤")
  bstack111lll11_opy_ = False
  bstack11l11llll11_opy_ = None
  bstack11l11lll11l_opy_ = {}
  bstack11l1ll11111_opy_ = 300
  bstack11l1ll1l11l_opy_ = False
  logger = None
  bstack11l1l1l111l_opy_ = False
  bstack1ll1111l1l_opy_ = False
  percy_build_id = None
  bstack11l1ll11l11_opy_ = bstack1l1l111_opy_ (u"࠭ࠧ᭥")
  bstack11l1l1lll1l_opy_ = {
    bstack1l1l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ᭦") : 1,
    bstack1l1l111_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩ᭧") : 2,
    bstack1l1l111_opy_ (u"ࠩࡨࡨ࡬࡫ࠧ᭨") : 3,
    bstack1l1l111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪ᭩") : 4
  }
  def __init__(self) -> None: pass
  def bstack11l1l11111l_opy_(self):
    bstack11l11l1llll_opy_ = bstack1l1l111_opy_ (u"ࠫࠬ᭪")
    bstack11l11lll111_opy_ = sys.platform
    bstack11l1l1ll11l_opy_ = bstack1l1l111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ᭫")
    if re.match(bstack1l1l111_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨ᭬"), bstack11l11lll111_opy_) != None:
      bstack11l11l1llll_opy_ = bstack1l11111l1ll_opy_ + bstack1l1l111_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣ᭭")
      self.bstack11l1ll11l11_opy_ = bstack1l1l111_opy_ (u"ࠨ࡯ࡤࡧࠬ᭮")
    elif re.match(bstack1l1l111_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢ᭯"), bstack11l11lll111_opy_) != None:
      bstack11l11l1llll_opy_ = bstack1l11111l1ll_opy_ + bstack1l1l111_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦ᭰")
      bstack11l1l1ll11l_opy_ = bstack1l1l111_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢ᭱")
      self.bstack11l1ll11l11_opy_ = bstack1l1l111_opy_ (u"ࠬࡽࡩ࡯ࠩ᭲")
    else:
      bstack11l11l1llll_opy_ = bstack1l11111l1ll_opy_ + bstack1l1l111_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤ᭳")
      self.bstack11l1ll11l11_opy_ = bstack1l1l111_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭᭴")
    return bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_
  def bstack11l1l1l1l11_opy_(self):
    try:
      bstack11l1l111l11_opy_ = [os.path.join(expanduser(bstack1l1l111_opy_ (u"ࠣࢀࠥ᭵")), bstack1l1l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ᭶")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11l1l111l11_opy_:
        if(self.bstack11l1l1l1l1l_opy_(path)):
          return path
      raise bstack1l1l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢ᭷")
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨ᭸").format(e))
  def bstack11l1l1l1l1l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack11l1l111111_opy_(self, bstack11l1ll1l1ll_opy_):
    return os.path.join(bstack11l1ll1l1ll_opy_, self.bstack11lll1ll1ll_opy_ + bstack1l1l111_opy_ (u"ࠧ࠴ࡥࡵࡣࡪࠦ᭹"))
  def bstack11l11ll1l11_opy_(self, bstack11l1ll1l1ll_opy_, bstack11l1l11llll_opy_):
    if not bstack11l1l11llll_opy_: return
    try:
      bstack11l1l1lll11_opy_ = self.bstack11l1l111111_opy_(bstack11l1ll1l1ll_opy_)
      with open(bstack11l1l1lll11_opy_, bstack1l1l111_opy_ (u"ࠨࡷࠣ᭺")) as f:
        f.write(bstack11l1l11llll_opy_)
        self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡔࡣࡹࡩࡩࠦ࡮ࡦࡹࠣࡉ࡙ࡧࡧࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠦ᭻"))
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡷ࡬ࡪࠦࡥࡵࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ᭼").format(e))
  def bstack11l1l11ll11_opy_(self, bstack11l1ll1l1ll_opy_):
    try:
      bstack11l1l1lll11_opy_ = self.bstack11l1l111111_opy_(bstack11l1ll1l1ll_opy_)
      if os.path.exists(bstack11l1l1lll11_opy_):
        with open(bstack11l1l1lll11_opy_, bstack1l1l111_opy_ (u"ࠤࡵࠦ᭽")) as f:
          bstack11l1l11llll_opy_ = f.read().strip()
          return bstack11l1l11llll_opy_ if bstack11l1l11llll_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡰࡴࡧࡤࡪࡰࡪࠤࡊ࡚ࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨ᭾").format(e))
  def bstack11l11ll11ll_opy_(self, bstack11l1ll1l1ll_opy_, bstack11l11l1llll_opy_):
    bstack11l1l1llll1_opy_ = self.bstack11l1l11ll11_opy_(bstack11l1ll1l1ll_opy_)
    if bstack11l1l1llll1_opy_:
      try:
        bstack11l1ll111ll_opy_ = self.bstack11l11ll1ll1_opy_(bstack11l1l1llll1_opy_, bstack11l11l1llll_opy_)
        if not bstack11l1ll111ll_opy_:
          self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡸࠦࡵࡱࠢࡷࡳࠥࡪࡡࡵࡧࠣࠬࡊ࡚ࡡࡨࠢࡸࡲࡨ࡮ࡡ࡯ࡩࡨࡨ࠮ࠨ᭿"))
          return True
        self.logger.debug(bstack1l1l111_opy_ (u"ࠧࡔࡥࡸࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡺࡶࡤࡢࡶࡨࠦᮀ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l1l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡲࡶࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧᮁ").format(e))
    return False
  def bstack11l11ll1ll1_opy_(self, bstack11l1l1llll1_opy_, bstack11l11l1llll_opy_):
    try:
      headers = {
        bstack1l1l111_opy_ (u"ࠢࡊࡨ࠰ࡒࡴࡴࡥ࠮ࡏࡤࡸࡨ࡮ࠢᮂ"): bstack11l1l1llll1_opy_
      }
      response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠨࡉࡈࡘࠬᮃ"), bstack11l11l1llll_opy_, {}, {bstack1l1l111_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥᮄ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠻ࠢࡾࢁࠧᮅ").format(e))
  @measure(event_name=EVENTS.bstack1l111111lll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
  def bstack11l1ll11ll1_opy_(self, bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_):
    try:
      bstack11l1l1111ll_opy_ = self.bstack11l1l1l1l11_opy_()
      bstack11l11lllll1_opy_ = os.path.join(bstack11l1l1111ll_opy_, bstack1l1l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧᮆ"))
      bstack11l1ll111l1_opy_ = os.path.join(bstack11l1l1111ll_opy_, bstack11l1l1ll11l_opy_)
      if self.bstack11l11ll11ll_opy_(bstack11l1l1111ll_opy_, bstack11l11l1llll_opy_):
        if os.path.exists(bstack11l1ll111l1_opy_):
          self.logger.info(bstack1l1l111_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᮇ").format(bstack11l1ll111l1_opy_))
          return bstack11l1ll111l1_opy_
        if os.path.exists(bstack11l11lllll1_opy_):
          self.logger.info(bstack1l1l111_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦᮈ").format(bstack11l11lllll1_opy_))
          return self.bstack11l1l1l11l1_opy_(bstack11l11lllll1_opy_, bstack11l1l1ll11l_opy_)
      self.logger.info(bstack1l1l111_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧᮉ").format(bstack11l11l1llll_opy_))
      response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠨࡉࡈࡘࠬᮊ"), bstack11l11l1llll_opy_, {}, {})
      if response.status_code == 200:
        bstack11l11llllll_opy_ = response.headers.get(bstack1l1l111_opy_ (u"ࠤࡈࡘࡦ࡭ࠢᮋ"), bstack1l1l111_opy_ (u"ࠥࠦᮌ"))
        if bstack11l11llllll_opy_:
          self.bstack11l11ll1l11_opy_(bstack11l1l1111ll_opy_, bstack11l11llllll_opy_)
        with open(bstack11l11lllll1_opy_, bstack1l1l111_opy_ (u"ࠫࡼࡨࠧᮍ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l1l111_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡿࠥᮎ").format(bstack11l11lllll1_opy_))
        return self.bstack11l1l1l11l1_opy_(bstack11l11lllll1_opy_, bstack11l1l1ll11l_opy_)
      else:
        raise(bstack1l1l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡾࠤᮏ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣᮐ").format(e))
  def bstack11l1l111l1l_opy_(self, bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_):
    try:
      retry = 2
      bstack11l1ll111l1_opy_ = None
      bstack11l1l11l11l_opy_ = False
      while retry > 0:
        bstack11l1ll111l1_opy_ = self.bstack11l1ll11ll1_opy_(bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_)
        bstack11l1l11l11l_opy_ = self.bstack11l1l1111l1_opy_(bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_, bstack11l1ll111l1_opy_)
        if bstack11l1l11l11l_opy_:
          break
        retry -= 1
      return bstack11l1ll111l1_opy_, bstack11l1l11l11l_opy_
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧᮑ").format(e))
    return bstack11l1ll111l1_opy_, False
  def bstack11l1l1111l1_opy_(self, bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_, bstack11l1ll111l1_opy_, bstack11l1ll11lll_opy_ = 0):
    if bstack11l1ll11lll_opy_ > 1:
      return False
    if bstack11l1ll111l1_opy_ == None or os.path.exists(bstack11l1ll111l1_opy_) == False:
      self.logger.warn(bstack1l1l111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᮒ"))
      return False
    bstack11l1ll1l111_opy_ = bstack1l1l111_opy_ (u"ࠥࡢ࠳࠰ࡀࡱࡧࡵࡧࡾࡢ࠯ࡤ࡮࡬ࠤࡡࡪ࠮࡝ࡦ࠮࠲ࡡࡪࠫࠣᮓ")
    command = bstack1l1l111_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪᮔ").format(bstack11l1ll111l1_opy_)
    bstack11l11lll1l1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11l1ll1l111_opy_, bstack11l11lll1l1_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l1l111_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦᮕ"))
      return False
  def bstack11l1l1l11l1_opy_(self, bstack11l11lllll1_opy_, bstack11l1l1ll11l_opy_):
    try:
      working_dir = os.path.dirname(bstack11l11lllll1_opy_)
      shutil.unpack_archive(bstack11l11lllll1_opy_, working_dir)
      bstack11l1ll111l1_opy_ = os.path.join(working_dir, bstack11l1l1ll11l_opy_)
      os.chmod(bstack11l1ll111l1_opy_, 0o755)
      return bstack11l1ll111l1_opy_
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᮖ"))
  def bstack11l11lll1ll_opy_(self):
    try:
      bstack11l1ll1111l_opy_ = self.config.get(bstack1l1l111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᮗ"))
      bstack11l11lll1ll_opy_ = bstack11l1ll1111l_opy_ or (bstack11l1ll1111l_opy_ is None and self.bstack1llll111l1_opy_)
      if not bstack11l11lll1ll_opy_ or self.config.get(bstack1l1l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᮘ"), None) not in bstack1l1111lll1l_opy_:
        return False
      self.bstack111lll11_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᮙ").format(e))
  def bstack11l11ll1111_opy_(self):
    try:
      bstack11l11ll1111_opy_ = self.percy_capture_mode
      return bstack11l11ll1111_opy_
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᮚ").format(e))
  def init(self, bstack1llll111l1_opy_, config, logger):
    self.bstack1llll111l1_opy_ = bstack1llll111l1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11l11lll1ll_opy_():
      return
    self.bstack11l11lll11l_opy_ = config.get(bstack1l1l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᮛ"), {})
    self.percy_capture_mode = config.get(bstack1l1l111_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᮜ"))
    try:
      bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_ = self.bstack11l1l11111l_opy_()
      self.bstack11lll1ll1ll_opy_ = bstack11l1l1ll11l_opy_
      bstack11l1ll111l1_opy_, bstack11l1l11l11l_opy_ = self.bstack11l1l111l1l_opy_(bstack11l11l1llll_opy_, bstack11l1l1ll11l_opy_)
      if bstack11l1l11l11l_opy_:
        self.binary_path = bstack11l1ll111l1_opy_
        thread = Thread(target=self.bstack11l1l1l11ll_opy_)
        thread.start()
      else:
        self.bstack11l1l1l111l_opy_ = True
        self.logger.error(bstack1l1l111_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥᮝ").format(bstack11l1ll111l1_opy_))
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᮞ").format(e))
  def bstack11l11llll1l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l1l111_opy_ (u"ࠨ࡮ࡲ࡫ࠬᮟ"), bstack1l1l111_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬᮠ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l1l111_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢᮡ").format(logfile))
      self.bstack11l11ll1l1l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᮢ").format(e))
  @measure(event_name=EVENTS.bstack1l1111111l1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
  def bstack11l1l1l11ll_opy_(self):
    bstack11l1l1l1lll_opy_ = self.bstack11l1l11lll1_opy_()
    if bstack11l1l1l1lll_opy_ == None:
      self.bstack11l1l1l111l_opy_ = True
      self.logger.error(bstack1l1l111_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣᮣ"))
      return False
    command_args = [bstack1l1l111_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢᮤ") if self.bstack1llll111l1_opy_ else bstack1l1l111_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫᮥ")]
    bstack11ll1111l1l_opy_ = self.bstack11l1ll11l1l_opy_()
    if bstack11ll1111l1l_opy_ != None:
      command_args.append(bstack1l1l111_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢᮦ").format(bstack11ll1111l1l_opy_))
    env = os.environ.copy()
    env[bstack1l1l111_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢᮧ")] = bstack11l1l1l1lll_opy_
    env[bstack1l1l111_opy_ (u"ࠥࡘࡍࡥࡂࡖࡋࡏࡈࡤ࡛ࡕࡊࡆࠥᮨ")] = os.environ.get(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᮩ"), bstack1l1l111_opy_ (u"᮪ࠬ࠭"))
    bstack11l1l11ll1l_opy_ = [self.binary_path]
    self.bstack11l11llll1l_opy_()
    self.bstack11l11llll11_opy_ = self.bstack11l1l1lllll_opy_(bstack11l1l11ll1l_opy_ + command_args, env)
    self.logger.debug(bstack1l1l111_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱ᮫ࠢ"))
    bstack11l1ll11lll_opy_ = 0
    while self.bstack11l11llll11_opy_.poll() == None:
      bstack11l11l1ll1l_opy_ = self.bstack11l11ll11l1_opy_()
      if bstack11l11l1ll1l_opy_:
        self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᮬ"))
        self.bstack11l1ll1l11l_opy_ = True
        return True
      bstack11l1ll11lll_opy_ += 1
      self.logger.debug(bstack1l1l111_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᮭ").format(bstack11l1ll11lll_opy_))
      time.sleep(2)
    self.logger.error(bstack1l1l111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᮮ").format(bstack11l1ll11lll_opy_))
    self.bstack11l1l1l111l_opy_ = True
    return False
  def bstack11l11ll11l1_opy_(self, bstack11l1ll11lll_opy_ = 0):
    if bstack11l1ll11lll_opy_ > 10:
      return False
    try:
      bstack11l1l1l1ll1_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᮯ"), bstack1l1l111_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬ᮰"))
      bstack11l1l1ll111_opy_ = bstack11l1l1l1ll1_opy_ + bstack1l111111l1l_opy_
      response = requests.get(bstack11l1l1ll111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l1l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫ᮱"), {}).get(bstack1l1l111_opy_ (u"࠭ࡩࡥࠩ᮲"), None)
      return True
    except:
      self.logger.debug(bstack1l1l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡭࡫ࡡ࡭ࡶ࡫ࠤࡨ࡮ࡥࡤ࡭ࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧ᮳"))
      return False
  def bstack11l1l11lll1_opy_(self):
    bstack11l1l1l1111_opy_ = bstack1l1l111_opy_ (u"ࠨࡣࡳࡴࠬ᮴") if self.bstack1llll111l1_opy_ else bstack1l1l111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ᮵")
    bstack11l11ll1lll_opy_ = bstack1l1l111_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨ᮶") if self.config.get(bstack1l1l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ᮷")) is None else True
    bstack11lll1lll1l_opy_ = bstack1l1l111_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠪࡵ࡫ࡲࡤࡻࡀࡿࢂࠨ᮸").format(self.config[bstack1l1l111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ᮹")], bstack11l1l1l1111_opy_, bstack11l11ll1lll_opy_)
    if self.percy_capture_mode:
      bstack11lll1lll1l_opy_ += bstack1l1l111_opy_ (u"ࠢࠧࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪࡃࡻࡾࠤᮺ").format(self.percy_capture_mode)
    uri = bstack11ll1111_opy_(bstack11lll1lll1l_opy_)
    try:
      response = bstack1l1l1lll_opy_(bstack1l1l111_opy_ (u"ࠨࡉࡈࡘࠬᮻ"), uri, {}, {bstack1l1l111_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᮼ"): (self.config[bstack1l1l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᮽ")], self.config[bstack1l1l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᮾ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack111lll11_opy_ = data.get(bstack1l1l111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ᮿ"))
        self.percy_capture_mode = data.get(bstack1l1l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࠫᯀ"))
        os.environ[bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᯁ")] = str(self.bstack111lll11_opy_)
        os.environ[bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᯂ")] = str(self.percy_capture_mode)
        if bstack11l11ll1lll_opy_ == bstack1l1l111_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᯃ") and str(self.bstack111lll11_opy_).lower() == bstack1l1l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᯄ"):
          self.bstack1ll1111l1l_opy_ = True
        if bstack1l1l111_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᯅ") in data:
          return data[bstack1l1l111_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᯆ")]
        else:
          raise bstack1l1l111_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᯇ").format(data)
      else:
        raise bstack1l1l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᯈ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᯉ").format(e))
  def bstack11l1ll11l1l_opy_(self):
    bstack11l1l11l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᯊ"))
    try:
      if bstack1l1l111_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᯋ") not in self.bstack11l11lll11l_opy_:
        self.bstack11l11lll11l_opy_[bstack1l1l111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᯌ")] = 2
      with open(bstack11l1l11l1l1_opy_, bstack1l1l111_opy_ (u"ࠬࡽࠧᯍ")) as fp:
        json.dump(self.bstack11l11lll11l_opy_, fp)
      return bstack11l1l11l1l1_opy_
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᯎ").format(e))
  def bstack11l1l1lllll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11l1ll11l11_opy_ == bstack1l1l111_opy_ (u"ࠧࡸ࡫ࡱࠫᯏ"):
        bstack11l1ll1ll11_opy_ = [bstack1l1l111_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᯐ"), bstack1l1l111_opy_ (u"ࠩ࠲ࡧࠬᯑ")]
        cmd = bstack11l1ll1ll11_opy_ + cmd
      cmd = bstack1l1l111_opy_ (u"ࠪࠤࠬᯒ").join(cmd)
      self.logger.debug(bstack1l1l111_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣᯓ").format(cmd))
      with open(self.bstack11l11ll1l1l_opy_, bstack1l1l111_opy_ (u"ࠧࡧࠢᯔ")) as bstack11l11ll111l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11l11ll111l_opy_, text=True, stderr=bstack11l11ll111l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11l1l1l111l_opy_ = True
      self.logger.error(bstack1l1l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᯕ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11l1ll1l11l_opy_:
        self.logger.info(bstack1l1l111_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣᯖ"))
        cmd = [self.binary_path, bstack1l1l111_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦᯗ")]
        self.bstack11l1l1lllll_opy_(cmd)
        self.bstack11l1ll1l11l_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᯘ").format(cmd, e))
  def bstack11111l11_opy_(self):
    if not self.bstack111lll11_opy_:
      return
    try:
      bstack11l1l111lll_opy_ = 0
      while not self.bstack11l1ll1l11l_opy_ and bstack11l1l111lll_opy_ < self.bstack11l1ll11111_opy_:
        if self.bstack11l1l1l111l_opy_:
          self.logger.info(bstack1l1l111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣᯙ"))
          return
        time.sleep(1)
        bstack11l1l111lll_opy_ += 1
      os.environ[bstack1l1l111_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪᯚ")] = str(self.bstack11l1l1ll1ll_opy_())
      self.logger.info(bstack1l1l111_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨᯛ"))
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᯜ").format(e))
  def bstack11l1l1ll1ll_opy_(self):
    if self.bstack1llll111l1_opy_:
      return
    try:
      bstack11l1l11l111_opy_ = [platform[bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᯝ")].lower() for platform in self.config.get(bstack1l1l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᯞ"), [])]
      bstack11l1l11l1ll_opy_ = sys.maxsize
      bstack11l1l111ll1_opy_ = bstack1l1l111_opy_ (u"ࠩࠪᯟ")
      for browser in bstack11l1l11l111_opy_:
        if browser in self.bstack11l1l1lll1l_opy_:
          bstack11l1l1ll1l1_opy_ = self.bstack11l1l1lll1l_opy_[browser]
        if bstack11l1l1ll1l1_opy_ < bstack11l1l11l1ll_opy_:
          bstack11l1l11l1ll_opy_ = bstack11l1l1ll1l1_opy_
          bstack11l1l111ll1_opy_ = browser
      return bstack11l1l111ll1_opy_
    except Exception as e:
      self.logger.error(bstack1l1l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᯠ").format(e))
  @classmethod
  def bstack1llll11lll_opy_(self):
    return os.getenv(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᯡ"), bstack1l1l111_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫᯢ")).lower()
  @classmethod
  def bstack11llllll1_opy_(self):
    return os.getenv(bstack1l1l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᯣ"), bstack1l1l111_opy_ (u"ࠧࠨᯤ"))
  @classmethod
  def bstack1l1llllll11_opy_(cls, value):
    cls.bstack1ll1111l1l_opy_ = value
  @classmethod
  def bstack11l1ll1l1l1_opy_(cls):
    return cls.bstack1ll1111l1l_opy_
  @classmethod
  def bstack1l1llll1ll1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack11l11l1lll1_opy_(cls):
    return cls.percy_build_id