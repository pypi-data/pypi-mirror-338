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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack1l111l11111_opy_, bstack1l11111l11l_opy_
import tempfile
import json
bstack11l1lllll1l_opy_ = os.getenv(bstack1l1l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡋࡤࡌࡉࡍࡇࠥ᫕"), None) or os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠧ᫖"))
bstack11l1lllll11_opy_ = os.path.join(bstack1l1l111_opy_ (u"ࠦࡱࡵࡧࠣ᫗"), bstack1l1l111_opy_ (u"ࠬࡹࡤ࡬࠯ࡦࡰ࡮࠳ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠩ᫘"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l1l111_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩ᫙"),
      datefmt=bstack1l1l111_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬ᫚"),
      stream=sys.stdout
    )
  return logger
def bstack11111111l1_opy_():
  bstack11l1llll1ll_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡅࡇࡅ࡙ࡌࠨ᫛"), bstack1l1l111_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣ᫜"))
  return logging.DEBUG if bstack11l1llll1ll_opy_.lower() == bstack1l1l111_opy_ (u"ࠥࡸࡷࡻࡥࠣ᫝") else logging.INFO
def bstack1ll111ll1l1_opy_():
  global bstack11l1lllll1l_opy_
  if os.path.exists(bstack11l1lllll1l_opy_):
    os.remove(bstack11l1lllll1l_opy_)
  if os.path.exists(bstack11l1lllll11_opy_):
    os.remove(bstack11l1lllll11_opy_)
def bstack1l1l11l1ll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1111l1l1_opy_(config, log_level):
  bstack11l1lll1l1l_opy_ = log_level
  if bstack1l1l111_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭᫞") in config and config[bstack1l1l111_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧ᫟")] in bstack1l111l11111_opy_:
    bstack11l1lll1l1l_opy_ = bstack1l111l11111_opy_[config[bstack1l1l111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ᫠")]]
  if config.get(bstack1l1l111_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩ᫡"), False):
    logging.getLogger().setLevel(bstack11l1lll1l1l_opy_)
    return bstack11l1lll1l1l_opy_
  global bstack11l1lllll1l_opy_
  bstack1l1l11l1ll_opy_()
  bstack11l1llll111_opy_ = logging.Formatter(
    fmt=bstack1l1l111_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫ᫢"),
    datefmt=bstack1l1l111_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧ᫣"),
  )
  bstack11ll1111111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11l1lllll1l_opy_)
  file_handler.setFormatter(bstack11l1llll111_opy_)
  bstack11ll1111111_opy_.setFormatter(bstack11l1llll111_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11ll1111111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l1l111_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬ᫤"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11ll1111111_opy_.setLevel(bstack11l1lll1l1l_opy_)
  logging.getLogger().addHandler(bstack11ll1111111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11l1lll1l1l_opy_
def bstack11ll1111l11_opy_(config):
  try:
    bstack11l1lll1ll1_opy_ = set(bstack1l11111l11l_opy_)
    bstack11l1lll11ll_opy_ = bstack1l1l111_opy_ (u"ࠫࠬ᫥")
    with open(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨ᫦")) as bstack11ll111l111_opy_:
      bstack11l1llll1l1_opy_ = bstack11ll111l111_opy_.read()
      bstack11l1lll11ll_opy_ = re.sub(bstack1l1l111_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠤ࠰࠭ࠨࡡࡴࠧ᫧"), bstack1l1l111_opy_ (u"ࠧࠨ᫨"), bstack11l1llll1l1_opy_, flags=re.M)
      bstack11l1lll11ll_opy_ = re.sub(
        bstack1l1l111_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠫࠫ᫩") + bstack1l1l111_opy_ (u"ࠩࡿࠫ᫪").join(bstack11l1lll1ll1_opy_) + bstack1l1l111_opy_ (u"ࠪ࠭࠳࠰ࠤࠨ᫫"),
        bstack1l1l111_opy_ (u"ࡶࠬࡢ࠲࠻ࠢ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭᫬"),
        bstack11l1lll11ll_opy_, flags=re.M | re.I
      )
    def bstack11l1llllll1_opy_(dic):
      bstack11ll1111lll_opy_ = {}
      for key, value in dic.items():
        if key in bstack11l1lll1ll1_opy_:
          bstack11ll1111lll_opy_[key] = bstack1l1l111_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩ᫭")
        else:
          if isinstance(value, dict):
            bstack11ll1111lll_opy_[key] = bstack11l1llllll1_opy_(value)
          else:
            bstack11ll1111lll_opy_[key] = value
      return bstack11ll1111lll_opy_
    bstack11ll1111lll_opy_ = bstack11l1llllll1_opy_(config)
    return {
      bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ᫮"): bstack11l1lll11ll_opy_,
      bstack1l1l111_opy_ (u"ࠧࡧ࡫ࡱࡥࡱࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪ᫯"): json.dumps(bstack11ll1111lll_opy_)
    }
  except Exception as e:
    return {}
def bstack11ll11111l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1l1l111_opy_ (u"ࠨ࡮ࡲ࡫ࠬ᫰"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11ll1111l1l_opy_ = os.path.join(log_dir, bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵࠪ᫱"))
  if not os.path.exists(bstack11ll1111l1l_opy_):
    bstack11l1llll11l_opy_ = {
      bstack1l1l111_opy_ (u"ࠥ࡭ࡳ࡯ࡰࡢࡶ࡫ࠦ᫲"): str(inipath),
      bstack1l1l111_opy_ (u"ࠦࡷࡵ࡯ࡵࡲࡤࡸ࡭ࠨ᫳"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1l1l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫ᫴")), bstack1l1l111_opy_ (u"࠭ࡷࠨ᫵")) as bstack11ll111111l_opy_:
      bstack11ll111111l_opy_.write(json.dumps(bstack11l1llll11l_opy_))
def bstack11l1lllllll_opy_():
  try:
    bstack11ll1111l1l_opy_ = os.path.join(os.getcwd(), bstack1l1l111_opy_ (u"ࠧ࡭ࡱࡪࠫ᫶"), bstack1l1l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧ᫷"))
    if os.path.exists(bstack11ll1111l1l_opy_):
      with open(bstack11ll1111l1l_opy_, bstack1l1l111_opy_ (u"ࠩࡵࠫ᫸")) as bstack11ll111111l_opy_:
        bstack11l1lll11l1_opy_ = json.load(bstack11ll111111l_opy_)
      return bstack11l1lll11l1_opy_.get(bstack1l1l111_opy_ (u"ࠪ࡭ࡳ࡯ࡰࡢࡶ࡫ࠫ᫹"), bstack1l1l111_opy_ (u"ࠫࠬ᫺")), bstack11l1lll11l1_opy_.get(bstack1l1l111_opy_ (u"ࠬࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠧ᫻"), bstack1l1l111_opy_ (u"࠭ࠧ᫼"))
  except:
    pass
  return None, None
def bstack11ll11111ll_opy_():
  try:
    bstack11ll1111l1l_opy_ = os.path.join(os.getcwd(), bstack1l1l111_opy_ (u"ࠧ࡭ࡱࡪࠫ᫽"), bstack1l1l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧ᫾"))
    if os.path.exists(bstack11ll1111l1l_opy_):
      os.remove(bstack11ll1111l1l_opy_)
  except:
    pass
def bstack11l11lll1_opy_(config):
  from bstack_utils.helper import bstack111l11l1l_opy_
  global bstack11l1lllll1l_opy_
  try:
    if config.get(bstack1l1l111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫ᫿"), False):
      return
    uuid = os.getenv(bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᬀ")) if os.getenv(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᬁ")) else bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢᬂ"))
    if not uuid or uuid == bstack1l1l111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᬃ"):
      return
    bstack11l1lll1lll_opy_ = [bstack1l1l111_opy_ (u"ࠧࡳࡧࡴࡹ࡮ࡸࡥ࡮ࡧࡱࡸࡸ࠴ࡴࡹࡶࠪᬄ"), bstack1l1l111_opy_ (u"ࠨࡒ࡬ࡴ࡫࡯࡬ࡦࠩᬅ"), bstack1l1l111_opy_ (u"ࠩࡳࡽࡵࡸ࡯࡫ࡧࡦࡸ࠳ࡺ࡯࡮࡮ࠪᬆ"), bstack11l1lllll1l_opy_, bstack11l1lllll11_opy_]
    bstack11ll1111ll1_opy_, root_path = bstack11l1lllllll_opy_()
    if bstack11ll1111ll1_opy_ != None:
      bstack11l1lll1lll_opy_.append(bstack11ll1111ll1_opy_)
    if root_path != None:
      bstack11l1lll1lll_opy_.append(os.path.join(root_path, bstack1l1l111_opy_ (u"ࠪࡧࡴࡴࡦࡵࡧࡶࡸ࠳ࡶࡹࠨᬇ")))
    bstack1l1l11l1ll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡱࡵࡧࡴ࠯ࠪᬈ") + uuid + bstack1l1l111_opy_ (u"ࠬ࠴ࡴࡢࡴ࠱࡫ࡿ࠭ᬉ"))
    with tarfile.open(output_file, bstack1l1l111_opy_ (u"ࠨࡷ࠻ࡩࡽࠦᬊ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11l1lll1lll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11ll1111l11_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11l1lll1l11_opy_ = data.encode()
        tarinfo.size = len(bstack11l1lll1l11_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11l1lll1l11_opy_))
    bstack11lll1111l_opy_ = MultipartEncoder(
      fields= {
        bstack1l1l111_opy_ (u"ࠧࡥࡣࡷࡥࠬᬋ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l1l111_opy_ (u"ࠨࡴࡥࠫᬌ")), bstack1l1l111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࠯ࡪࡾ࡮ࡶࠧᬍ")),
        bstack1l1l111_opy_ (u"ࠪࡧࡱ࡯ࡥ࡯ࡶࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᬎ"): uuid
      }
    )
    response = requests.post(
      bstack1l1l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡻࡰ࡭ࡱࡤࡨ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡥ࡯࡭ࡪࡴࡴ࠮࡮ࡲ࡫ࡸ࠵ࡵࡱ࡮ࡲࡥࡩࠨᬏ"),
      data=bstack11lll1111l_opy_,
      headers={bstack1l1l111_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᬐ"): bstack11lll1111l_opy_.content_type},
      auth=(config[bstack1l1l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᬑ")], config[bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᬒ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l1l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧᬓ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l1l111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨᬔ") + str(e))
  finally:
    try:
      bstack1ll111ll1l1_opy_()
      bstack11ll11111ll_opy_()
    except:
      pass