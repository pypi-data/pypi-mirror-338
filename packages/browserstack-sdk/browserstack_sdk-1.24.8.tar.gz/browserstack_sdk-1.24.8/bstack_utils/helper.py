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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l11111l1l1_opy_, bstack1l11l11l11_opy_, bstack1lll11l1_opy_, bstack11lll11ll_opy_,
                                    bstack1l1111l11l1_opy_, bstack11llllllll1_opy_, bstack1l11111l11l_opy_, bstack1l1111l1ll1_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111ll1111_opy_, bstack11111l1ll_opy_
from bstack_utils.proxy import bstack11ll1llll1_opy_, bstack11lll11l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1111ll11l_opy_
from browserstack_sdk._version import __version__
bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
logger = bstack1111ll11l_opy_.get_logger(__name__, bstack1111ll11l_opy_.bstack11111111l1_opy_())
def bstack1l11l1111ll_opy_(config):
    return config[bstack1l1l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᢛ")]
def bstack1l11l111111_opy_(config):
    return config[bstack1l1l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᢜ")]
def bstack11ll1l11ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11llll1111l_opy_(obj):
    values = []
    bstack11lll11111l_opy_ = re.compile(bstack1l1l111_opy_ (u"ࡳࠤࡡࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࡝ࡦ࠮ࠨࠧᢝ"), re.I)
    for key in obj.keys():
        if bstack11lll11111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11ll1ll1lll_opy_(config):
    tags = []
    tags.extend(bstack11llll1111l_opy_(os.environ))
    tags.extend(bstack11llll1111l_opy_(config))
    return tags
def bstack11lllll1l1l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11ll1l1111l_opy_(bstack11lll111l11_opy_):
    if not bstack11lll111l11_opy_:
        return bstack1l1l111_opy_ (u"ࠩࠪᢞ")
    return bstack1l1l111_opy_ (u"ࠥࡿࢂࠦࠨࡼࡿࠬࠦᢟ").format(bstack11lll111l11_opy_.name, bstack11lll111l11_opy_.email)
def bstack1l111llllll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11llll1l111_opy_ = repo.common_dir
        info = {
            bstack1l1l111_opy_ (u"ࠦࡸ࡮ࡡࠣᢠ"): repo.head.commit.hexsha,
            bstack1l1l111_opy_ (u"ࠧࡹࡨࡰࡴࡷࡣࡸ࡮ࡡࠣᢡ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l1l111_opy_ (u"ࠨࡢࡳࡣࡱࡧ࡭ࠨᢢ"): repo.active_branch.name,
            bstack1l1l111_opy_ (u"ࠢࡵࡣࡪࠦᢣ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l1l111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࠦᢤ"): bstack11ll1l1111l_opy_(repo.head.commit.committer),
            bstack1l1l111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࡤࡪࡡࡵࡧࠥᢥ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l1l111_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࠥᢦ"): bstack11ll1l1111l_opy_(repo.head.commit.author),
            bstack1l1l111_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡣࡩࡧࡴࡦࠤᢧ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l1l111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᢨ"): repo.head.commit.message,
            bstack1l1l111_opy_ (u"ࠨࡲࡰࡱࡷᢩࠦ"): repo.git.rev_parse(bstack1l1l111_opy_ (u"ࠢ࠮࠯ࡶ࡬ࡴࡽ࠭ࡵࡱࡳࡰࡪࡼࡥ࡭ࠤᢪ")),
            bstack1l1l111_opy_ (u"ࠣࡥࡲࡱࡲࡵ࡮ࡠࡩ࡬ࡸࡤࡪࡩࡳࠤ᢫"): bstack11llll1l111_opy_,
            bstack1l1l111_opy_ (u"ࠤࡺࡳࡷࡱࡴࡳࡧࡨࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧ᢬"): subprocess.check_output([bstack1l1l111_opy_ (u"ࠥ࡫࡮ࡺࠢ᢭"), bstack1l1l111_opy_ (u"ࠦࡷ࡫ࡶ࠮ࡲࡤࡶࡸ࡫ࠢ᢮"), bstack1l1l111_opy_ (u"ࠧ࠳࠭ࡨ࡫ࡷ࠱ࡨࡵ࡭࡮ࡱࡱ࠱ࡩ࡯ࡲࠣ᢯")]).strip().decode(
                bstack1l1l111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᢰ")),
            bstack1l1l111_opy_ (u"ࠢ࡭ࡣࡶࡸࡤࡺࡡࡨࠤᢱ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l1l111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡴࡡࡶ࡭ࡳࡩࡥࡠ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᢲ"): repo.git.rev_list(
                bstack1l1l111_opy_ (u"ࠤࡾࢁ࠳࠴ࡻࡾࠤᢳ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11lll1111ll_opy_ = []
        for remote in remotes:
            bstack11lll1l1ll1_opy_ = {
                bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᢴ"): remote.name,
                bstack1l1l111_opy_ (u"ࠦࡺࡸ࡬ࠣᢵ"): remote.url,
            }
            bstack11lll1111ll_opy_.append(bstack11lll1l1ll1_opy_)
        bstack11lll11llll_opy_ = {
            bstack1l1l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᢶ"): bstack1l1l111_opy_ (u"ࠨࡧࡪࡶࠥᢷ"),
            **info,
            bstack1l1l111_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫ࡳࠣᢸ"): bstack11lll1111ll_opy_
        }
        bstack11lll11llll_opy_ = bstack11llll1l1l1_opy_(bstack11lll11llll_opy_)
        return bstack11lll11llll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᢹ").format(err))
        return {}
def bstack11llll1l1l1_opy_(bstack11lll11llll_opy_):
    bstack11ll1lll1ll_opy_ = bstack11lll1l11ll_opy_(bstack11lll11llll_opy_)
    if bstack11ll1lll1ll_opy_ and bstack11ll1lll1ll_opy_ > bstack1l1111l11l1_opy_:
        bstack11ll1ll111l_opy_ = bstack11ll1lll1ll_opy_ - bstack1l1111l11l1_opy_
        bstack11ll11llll1_opy_ = bstack11llllll11l_opy_(bstack11lll11llll_opy_[bstack1l1l111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᢺ")], bstack11ll1ll111l_opy_)
        bstack11lll11llll_opy_[bstack1l1l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᢻ")] = bstack11ll11llll1_opy_
        logger.info(bstack1l1l111_opy_ (u"࡙ࠦ࡮ࡥࠡࡥࡲࡱࡲ࡯ࡴࠡࡪࡤࡷࠥࡨࡥࡦࡰࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩ࠴ࠠࡔ࡫ࡽࡩࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࠡࡣࡩࡸࡪࡸࠠࡵࡴࡸࡲࡨࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡼࡿࠣࡏࡇࠨᢼ")
                    .format(bstack11lll1l11ll_opy_(bstack11lll11llll_opy_) / 1024))
    return bstack11lll11llll_opy_
def bstack11lll1l11ll_opy_(bstack1lll1l1ll1_opy_):
    try:
        if bstack1lll1l1ll1_opy_:
            bstack11lllll1lll_opy_ = json.dumps(bstack1lll1l1ll1_opy_)
            bstack11llll1llll_opy_ = sys.getsizeof(bstack11lllll1lll_opy_)
            return bstack11llll1llll_opy_
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"࡙ࠧ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤࡨࡧ࡬ࡤࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡶ࡭ࡿ࡫ࠠࡰࡨࠣࡎࡘࡕࡎࠡࡱࡥ࡮ࡪࡩࡴ࠻ࠢࡾࢁࠧᢽ").format(e))
    return -1
def bstack11llllll11l_opy_(field, bstack11lll1ll1l1_opy_):
    try:
        bstack11llll111l1_opy_ = len(bytes(bstack11llllllll1_opy_, bstack1l1l111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᢾ")))
        bstack11ll1lll1l1_opy_ = bytes(field, bstack1l1l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᢿ"))
        bstack11llll1lll1_opy_ = len(bstack11ll1lll1l1_opy_)
        bstack11llll1l11l_opy_ = ceil(bstack11llll1lll1_opy_ - bstack11lll1ll1l1_opy_ - bstack11llll111l1_opy_)
        if bstack11llll1l11l_opy_ > 0:
            bstack11lll1llll1_opy_ = bstack11ll1lll1l1_opy_[:bstack11llll1l11l_opy_].decode(bstack1l1l111_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᣀ"), errors=bstack1l1l111_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࠩᣁ")) + bstack11llllllll1_opy_
            return bstack11lll1llll1_opy_
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩࡦ࡮ࡧ࠰ࠥࡴ࡯ࡵࡪ࡬ࡲ࡬ࠦࡷࡢࡵࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩࠦࡨࡦࡴࡨ࠾ࠥࢁࡽࠣᣂ").format(e))
    return field
def bstack1l1lll1ll_opy_():
    env = os.environ
    if (bstack1l1l111_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤᣃ") in env and len(env[bstack1l1l111_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᣄ")]) > 0) or (
            bstack1l1l111_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧᣅ") in env and len(env[bstack1l1l111_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᣆ")]) > 0):
        return {
            bstack1l1l111_opy_ (u"ࠣࡰࡤࡱࡪࠨᣇ"): bstack1l1l111_opy_ (u"ࠤࡍࡩࡳࡱࡩ࡯ࡵࠥᣈ"),
            bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᣉ"): env.get(bstack1l1l111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᣊ")),
            bstack1l1l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᣋ"): env.get(bstack1l1l111_opy_ (u"ࠨࡊࡐࡄࡢࡒࡆࡓࡅࠣᣌ")),
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᣍ"): env.get(bstack1l1l111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᣎ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠤࡆࡍࠧᣏ")) == bstack1l1l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᣐ") and bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡇࡎࠨᣑ"))):
        return {
            bstack1l1l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᣒ"): bstack1l1l111_opy_ (u"ࠨࡃࡪࡴࡦࡰࡪࡉࡉࠣᣓ"),
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᣔ"): env.get(bstack1l1l111_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᣕ")),
            bstack1l1l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᣖ"): env.get(bstack1l1l111_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡎࡔࡈࠢᣗ")),
            bstack1l1l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᣘ"): env.get(bstack1l1l111_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࠣᣙ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠨࡃࡊࠤᣚ")) == bstack1l1l111_opy_ (u"ࠢࡵࡴࡸࡩࠧᣛ") and bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࠣᣜ"))):
        return {
            bstack1l1l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᣝ"): bstack1l1l111_opy_ (u"ࠥࡘࡷࡧࡶࡪࡵࠣࡇࡎࠨᣞ"),
            bstack1l1l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᣟ"): env.get(bstack1l1l111_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣ࡜ࡋࡂࡠࡗࡕࡐࠧᣠ")),
            bstack1l1l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᣡ"): env.get(bstack1l1l111_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᣢ")),
            bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᣣ"): env.get(bstack1l1l111_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᣤ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠥࡇࡎࠨᣥ")) == bstack1l1l111_opy_ (u"ࠦࡹࡸࡵࡦࠤᣦ") and env.get(bstack1l1l111_opy_ (u"ࠧࡉࡉࡠࡐࡄࡑࡊࠨᣧ")) == bstack1l1l111_opy_ (u"ࠨࡣࡰࡦࡨࡷ࡭࡯ࡰࠣᣨ"):
        return {
            bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᣩ"): bstack1l1l111_opy_ (u"ࠣࡅࡲࡨࡪࡹࡨࡪࡲࠥᣪ"),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᣫ"): None,
            bstack1l1l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᣬ"): None,
            bstack1l1l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᣭ"): None
        }
    if env.get(bstack1l1l111_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡕࡅࡓࡉࡈࠣᣮ")) and env.get(bstack1l1l111_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡆࡓࡒࡓࡉࡕࠤᣯ")):
        return {
            bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᣰ"): bstack1l1l111_opy_ (u"ࠣࡄ࡬ࡸࡧࡻࡣ࡬ࡧࡷࠦᣱ"),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᣲ"): env.get(bstack1l1l111_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡇࡊࡖࡢࡌ࡙࡚ࡐࡠࡑࡕࡍࡌࡏࡎࠣᣳ")),
            bstack1l1l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᣴ"): None,
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᣵ"): env.get(bstack1l1l111_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᣶"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠢࡄࡋࠥ᣷")) == bstack1l1l111_opy_ (u"ࠣࡶࡵࡹࡪࠨ᣸") and bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠤࡇࡖࡔࡔࡅࠣ᣹"))):
        return {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣ᣺"): bstack1l1l111_opy_ (u"ࠦࡉࡸ࡯࡯ࡧࠥ᣻"),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᣼"): env.get(bstack1l1l111_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡑࡏࡎࡌࠤ᣽")),
            bstack1l1l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᣾"): None,
            bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᣿"): env.get(bstack1l1l111_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᤀ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠥࡇࡎࠨᤁ")) == bstack1l1l111_opy_ (u"ࠦࡹࡸࡵࡦࠤᤂ") and bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࠣᤃ"))):
        return {
            bstack1l1l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᤄ"): bstack1l1l111_opy_ (u"ࠢࡔࡧࡰࡥࡵ࡮࡯ࡳࡧࠥᤅ"),
            bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᤆ"): env.get(bstack1l1l111_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡕࡒࡈࡃࡑࡍ࡟ࡇࡔࡊࡑࡑࡣ࡚ࡘࡌࠣᤇ")),
            bstack1l1l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᤈ"): env.get(bstack1l1l111_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᤉ")),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᤊ"): env.get(bstack1l1l111_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡉࡅࠤᤋ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠢࡄࡋࠥᤌ")) == bstack1l1l111_opy_ (u"ࠣࡶࡵࡹࡪࠨᤍ") and bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠤࡊࡍ࡙ࡒࡁࡃࡡࡆࡍࠧᤎ"))):
        return {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᤏ"): bstack1l1l111_opy_ (u"ࠦࡌ࡯ࡴࡍࡣࡥࠦᤐ"),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᤑ"): env.get(bstack1l1l111_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡕࡓࡎࠥᤒ")),
            bstack1l1l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᤓ"): env.get(bstack1l1l111_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᤔ")),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᤕ"): env.get(bstack1l1l111_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡍࡉࠨᤖ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠦࡈࡏࠢᤗ")) == bstack1l1l111_opy_ (u"ࠧࡺࡲࡶࡧࠥᤘ") and bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࠤᤙ"))):
        return {
            bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᤚ"): bstack1l1l111_opy_ (u"ࠣࡄࡸ࡭ࡱࡪ࡫ࡪࡶࡨࠦᤛ"),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᤜ"): env.get(bstack1l1l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᤝ")),
            bstack1l1l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᤞ"): env.get(bstack1l1l111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡎࡄࡆࡊࡒࠢ᤟")) or env.get(bstack1l1l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᤠ")),
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᤡ"): env.get(bstack1l1l111_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᤢ"))
        }
    if bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦᤣ"))):
        return {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᤤ"): bstack1l1l111_opy_ (u"࡛ࠦ࡯ࡳࡶࡣ࡯ࠤࡘࡺࡵࡥ࡫ࡲࠤ࡙࡫ࡡ࡮ࠢࡖࡩࡷࡼࡩࡤࡧࡶࠦᤥ"),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᤦ"): bstack1l1l111_opy_ (u"ࠨࡻࡾࡽࢀࠦᤧ").format(env.get(bstack1l1l111_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪᤨ")), env.get(bstack1l1l111_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙ࡏࡄࠨᤩ"))),
            bstack1l1l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᤪ"): env.get(bstack1l1l111_opy_ (u"ࠥࡗ࡞࡙ࡔࡆࡏࡢࡈࡊࡌࡉࡏࡋࡗࡍࡔࡔࡉࡅࠤᤫ")),
            bstack1l1l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᤬"): env.get(bstack1l1l111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ᤭"))
        }
    if bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࠣ᤮"))):
        return {
            bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᤯"): bstack1l1l111_opy_ (u"ࠣࡃࡳࡴࡻ࡫ࡹࡰࡴࠥᤰ"),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᤱ"): bstack1l1l111_opy_ (u"ࠥࡿࢂ࠵ࡰࡳࡱ࡭ࡩࡨࡺ࠯ࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠤᤲ").format(env.get(bstack1l1l111_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡕࡓࡎࠪᤳ")), env.get(bstack1l1l111_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡂࡅࡆࡓ࡚ࡔࡔࡠࡐࡄࡑࡊ࠭ᤴ")), env.get(bstack1l1l111_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡒࡕࡓࡏࡋࡃࡕࡡࡖࡐ࡚ࡍࠧᤵ")), env.get(bstack1l1l111_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫᤶ"))),
            bstack1l1l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᤷ"): env.get(bstack1l1l111_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᤸ")),
            bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᤹"): env.get(bstack1l1l111_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᤺"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠧࡇ࡚ࡖࡔࡈࡣࡍ࡚ࡔࡑࡡࡘࡗࡊࡘ࡟ࡂࡉࡈࡒ࡙ࠨ᤻")) and env.get(bstack1l1l111_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣ᤼")):
        return {
            bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᤽"): bstack1l1l111_opy_ (u"ࠣࡃࡽࡹࡷ࡫ࠠࡄࡋࠥ᤾"),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᤿"): bstack1l1l111_opy_ (u"ࠥࡿࢂࢁࡽ࠰ࡡࡥࡹ࡮ࡲࡤ࠰ࡴࡨࡷࡺࡲࡴࡴࡁࡥࡹ࡮ࡲࡤࡊࡦࡀࡿࢂࠨ᥀").format(env.get(bstack1l1l111_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧ᥁")), env.get(bstack1l1l111_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࠪ᥂")), env.get(bstack1l1l111_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭᥃"))),
            bstack1l1l111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᥄"): env.get(bstack1l1l111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣ᥅")),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᥆"): env.get(bstack1l1l111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥ᥇"))
        }
    if any([env.get(bstack1l1l111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ᥈")), env.get(bstack1l1l111_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡔࡈࡗࡔࡒࡖࡆࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦ᥉")), env.get(bstack1l1l111_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥ᥊"))]):
        return {
            bstack1l1l111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᥋"): bstack1l1l111_opy_ (u"ࠣࡃ࡚ࡗࠥࡉ࡯ࡥࡧࡅࡹ࡮ࡲࡤࠣ᥌"),
            bstack1l1l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᥍"): env.get(bstack1l1l111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡐࡖࡄࡏࡍࡈࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᥎")),
            bstack1l1l111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᥏"): env.get(bstack1l1l111_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᥐ")),
            bstack1l1l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᥑ"): env.get(bstack1l1l111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᥒ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨᥓ")):
        return {
            bstack1l1l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᥔ"): bstack1l1l111_opy_ (u"ࠥࡆࡦࡳࡢࡰࡱࠥᥕ"),
            bstack1l1l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᥖ"): env.get(bstack1l1l111_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡖࡪࡹࡵ࡭ࡶࡶ࡙ࡷࡲࠢᥗ")),
            bstack1l1l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᥘ"): env.get(bstack1l1l111_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡴࡪࡲࡶࡹࡐ࡯ࡣࡐࡤࡱࡪࠨᥙ")),
            bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᥚ"): env.get(bstack1l1l111_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢᥛ"))
        }
    if env.get(bstack1l1l111_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࠦᥜ")) or env.get(bstack1l1l111_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨᥝ")):
        return {
            bstack1l1l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᥞ"): bstack1l1l111_opy_ (u"ࠨࡗࡦࡴࡦ࡯ࡪࡸࠢᥟ"),
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᥠ"): env.get(bstack1l1l111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᥡ")),
            bstack1l1l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᥢ"): bstack1l1l111_opy_ (u"ࠥࡑࡦ࡯࡮ࠡࡒ࡬ࡴࡪࡲࡩ࡯ࡧࠥᥣ") if env.get(bstack1l1l111_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨᥤ")) else None,
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᥥ"): env.get(bstack1l1l111_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡈࡋࡗࡣࡈࡕࡍࡎࡋࡗࠦᥦ"))
        }
    if any([env.get(bstack1l1l111_opy_ (u"ࠢࡈࡅࡓࡣࡕࡘࡏࡋࡇࡆࡘࠧᥧ")), env.get(bstack1l1l111_opy_ (u"ࠣࡉࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤᥨ")), env.get(bstack1l1l111_opy_ (u"ࠤࡊࡓࡔࡍࡌࡆࡡࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤᥩ"))]):
        return {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᥪ"): bstack1l1l111_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡈࡲ࡯ࡶࡦࠥᥫ"),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᥬ"): None,
            bstack1l1l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᥭ"): env.get(bstack1l1l111_opy_ (u"ࠢࡑࡔࡒࡎࡊࡉࡔࡠࡋࡇࠦ᥮")),
            bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᥯"): env.get(bstack1l1l111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᥰ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࠨᥱ")):
        return {
            bstack1l1l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᥲ"): bstack1l1l111_opy_ (u"࡙ࠧࡨࡪࡲࡳࡥࡧࡲࡥࠣᥳ"),
            bstack1l1l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᥴ"): env.get(bstack1l1l111_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᥵")),
            bstack1l1l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᥶"): bstack1l1l111_opy_ (u"ࠤࡍࡳࡧࠦࠣࡼࡿࠥ᥷").format(env.get(bstack1l1l111_opy_ (u"ࠪࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉ࠭᥸"))) if env.get(bstack1l1l111_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠢ᥹")) else None,
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᥺"): env.get(bstack1l1l111_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᥻"))
        }
    if bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠢࡏࡇࡗࡐࡎࡌ࡙ࠣ᥼"))):
        return {
            bstack1l1l111_opy_ (u"ࠣࡰࡤࡱࡪࠨ᥽"): bstack1l1l111_opy_ (u"ࠤࡑࡩࡹࡲࡩࡧࡻࠥ᥾"),
            bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᥿"): env.get(bstack1l1l111_opy_ (u"ࠦࡉࡋࡐࡍࡑ࡜ࡣ࡚ࡘࡌࠣᦀ")),
            bstack1l1l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᦁ"): env.get(bstack1l1l111_opy_ (u"ࠨࡓࡊࡖࡈࡣࡓࡇࡍࡆࠤᦂ")),
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᦃ"): env.get(bstack1l1l111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᦄ"))
        }
    if bstack11l1l1l1l1_opy_(env.get(bstack1l1l111_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡄࡇ࡙ࡏࡏࡏࡕࠥᦅ"))):
        return {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᦆ"): bstack1l1l111_opy_ (u"ࠦࡌ࡯ࡴࡉࡷࡥࠤࡆࡩࡴࡪࡱࡱࡷࠧᦇ"),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᦈ"): bstack1l1l111_opy_ (u"ࠨࡻࡾ࠱ࡾࢁ࠴ࡧࡣࡵ࡫ࡲࡲࡸ࠵ࡲࡶࡰࡶ࠳ࢀࢃࠢᦉ").format(env.get(bstack1l1l111_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡖࡔࡏࠫᦊ")), env.get(bstack1l1l111_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡈࡔࡔ࡙ࡉࡕࡑࡕ࡝ࠬᦋ")), env.get(bstack1l1l111_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠩᦌ"))),
            bstack1l1l111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᦍ"): env.get(bstack1l1l111_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣ࡜ࡕࡒࡌࡈࡏࡓ࡜ࠨᦎ")),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᦏ"): env.get(bstack1l1l111_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉࠨᦐ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠢࡄࡋࠥᦑ")) == bstack1l1l111_opy_ (u"ࠣࡶࡵࡹࡪࠨᦒ") and env.get(bstack1l1l111_opy_ (u"ࠤ࡙ࡉࡗࡉࡅࡍࠤᦓ")) == bstack1l1l111_opy_ (u"ࠥ࠵ࠧᦔ"):
        return {
            bstack1l1l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᦕ"): bstack1l1l111_opy_ (u"ࠧ࡜ࡥࡳࡥࡨࡰࠧᦖ"),
            bstack1l1l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᦗ"): bstack1l1l111_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࡼࡿࠥᦘ").format(env.get(bstack1l1l111_opy_ (u"ࠨࡘࡈࡖࡈࡋࡌࡠࡗࡕࡐࠬᦙ"))),
            bstack1l1l111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᦚ"): None,
            bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᦛ"): None,
        }
    if env.get(bstack1l1l111_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡖࡆࡔࡖࡍࡔࡔࠢᦜ")):
        return {
            bstack1l1l111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᦝ"): bstack1l1l111_opy_ (u"ࠨࡔࡦࡣࡰࡧ࡮ࡺࡹࠣᦞ"),
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᦟ"): None,
            bstack1l1l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᦠ"): env.get(bstack1l1l111_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣࡕࡘࡏࡋࡇࡆࡘࡤࡔࡁࡎࡇࠥᦡ")),
            bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᦢ"): env.get(bstack1l1l111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᦣ"))
        }
    if any([env.get(bstack1l1l111_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࠣᦤ")), env.get(bstack1l1l111_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡖࡑࠨᦥ")), env.get(bstack1l1l111_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠧᦦ")), env.get(bstack1l1l111_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡙ࡋࡁࡎࠤᦧ"))]):
        return {
            bstack1l1l111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᦨ"): bstack1l1l111_opy_ (u"ࠥࡇࡴࡴࡣࡰࡷࡵࡷࡪࠨᦩ"),
            bstack1l1l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᦪ"): None,
            bstack1l1l111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᦫ"): env.get(bstack1l1l111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᦬")) or None,
            bstack1l1l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᦭"): env.get(bstack1l1l111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ᦮"), 0)
        }
    if env.get(bstack1l1l111_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᦯")):
        return {
            bstack1l1l111_opy_ (u"ࠥࡲࡦࡳࡥࠣᦰ"): bstack1l1l111_opy_ (u"ࠦࡌࡵࡃࡅࠤᦱ"),
            bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᦲ"): None,
            bstack1l1l111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᦳ"): env.get(bstack1l1l111_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᦴ")),
            bstack1l1l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᦵ"): env.get(bstack1l1l111_opy_ (u"ࠤࡊࡓࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡄࡑࡘࡒ࡙ࡋࡒࠣᦶ"))
        }
    if env.get(bstack1l1l111_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᦷ")):
        return {
            bstack1l1l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᦸ"): bstack1l1l111_opy_ (u"ࠧࡉ࡯ࡥࡧࡉࡶࡪࡹࡨࠣᦹ"),
            bstack1l1l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᦺ"): env.get(bstack1l1l111_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᦻ")),
            bstack1l1l111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᦼ"): env.get(bstack1l1l111_opy_ (u"ࠤࡆࡊࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᦽ")),
            bstack1l1l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᦾ"): env.get(bstack1l1l111_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᦿ"))
        }
    return {bstack1l1l111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᧀ"): None}
def get_host_info():
    return {
        bstack1l1l111_opy_ (u"ࠨࡨࡰࡵࡷࡲࡦࡳࡥࠣᧁ"): platform.node(),
        bstack1l1l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤᧂ"): platform.system(),
        bstack1l1l111_opy_ (u"ࠣࡶࡼࡴࡪࠨᧃ"): platform.machine(),
        bstack1l1l111_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥᧄ"): platform.version(),
        bstack1l1l111_opy_ (u"ࠥࡥࡷࡩࡨࠣᧅ"): platform.architecture()[0]
    }
def bstack1ll111lll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11ll1lll111_opy_():
    if bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬᧆ")):
        return bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᧇ")
    return bstack1l1l111_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠬᧈ")
def bstack11llll11ll1_opy_(driver):
    info = {
        bstack1l1l111_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᧉ"): driver.capabilities,
        bstack1l1l111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬ᧊"): driver.session_id,
        bstack1l1l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ᧋"): driver.capabilities.get(bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ᧌"), None),
        bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭᧍"): driver.capabilities.get(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᧎"), None),
        bstack1l1l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨ᧏"): driver.capabilities.get(bstack1l1l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭᧐"), None),
    }
    if bstack11ll1lll111_opy_() == bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ᧑"):
        if bstack1llll111l1_opy_():
            info[bstack1l1l111_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪ᧒")] = bstack1l1l111_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩ᧓")
        elif driver.capabilities.get(bstack1l1l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᧔"), {}).get(bstack1l1l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ᧕"), False):
            info[bstack1l1l111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧ᧖")] = bstack1l1l111_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ᧗")
        else:
            info[bstack1l1l111_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩ᧘")] = bstack1l1l111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ᧙")
    return info
def bstack1llll111l1_opy_():
    if bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ᧚")):
        return True
    if bstack11l1l1l1l1_opy_(os.environ.get(bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ᧛"), None)):
        return True
    return False
def bstack1l1l1lll_opy_(bstack11ll1l1l1ll_opy_, url, data, config):
    headers = config.get(bstack1l1l111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭᧜"), None)
    proxies = bstack11ll1llll1_opy_(config, url)
    auth = config.get(bstack1l1l111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ᧝"), None)
    response = requests.request(
            bstack11ll1l1l1ll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1llll1l_opy_(bstack1l11l1l11_opy_, size):
    bstack1l1llll11l_opy_ = []
    while len(bstack1l11l1l11_opy_) > size:
        bstack1l1lllll1_opy_ = bstack1l11l1l11_opy_[:size]
        bstack1l1llll11l_opy_.append(bstack1l1lllll1_opy_)
        bstack1l11l1l11_opy_ = bstack1l11l1l11_opy_[size:]
    bstack1l1llll11l_opy_.append(bstack1l11l1l11_opy_)
    return bstack1l1llll11l_opy_
def bstack11lll11l11l_opy_(message, bstack11ll1l1l111_opy_=False):
    os.write(1, bytes(message, bstack1l1l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭᧞")))
    os.write(1, bytes(bstack1l1l111_opy_ (u"ࠨ࡞ࡱࠫ᧟"), bstack1l1l111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ᧠")))
    if bstack11ll1l1l111_opy_:
        with open(bstack1l1l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩ᧡") + os.environ[bstack1l1l111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪ᧢")] + bstack1l1l111_opy_ (u"ࠬ࠴࡬ࡰࡩࠪ᧣"), bstack1l1l111_opy_ (u"࠭ࡡࠨ᧤")) as f:
            f.write(message + bstack1l1l111_opy_ (u"ࠧ࡝ࡰࠪ᧥"))
def bstack1ll111111l1_opy_():
    return os.environ[bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ᧦")].lower() == bstack1l1l111_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ᧧")
def bstack11ll1111_opy_(bstack11lll1lll1l_opy_):
    return bstack1l1l111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ᧨").format(bstack1l11111l1l1_opy_, bstack11lll1lll1l_opy_)
def bstack1ll11l1ll1_opy_():
    return bstack111ll1111l_opy_().replace(tzinfo=None).isoformat() + bstack1l1l111_opy_ (u"ࠫ࡟࠭᧩")
def bstack11llll1ll1l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l1l111_opy_ (u"ࠬࡠࠧ᧪"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l1l111_opy_ (u"࡚࠭ࠨ᧫")))).total_seconds() * 1000
def bstack11lll11ll1l_opy_(timestamp):
    return bstack11ll11lllll_opy_(timestamp).isoformat() + bstack1l1l111_opy_ (u"࡛ࠧࠩ᧬")
def bstack11ll11lll11_opy_(bstack11ll1l1llll_opy_):
    date_format = bstack1l1l111_opy_ (u"ࠨࠧ࡜ࠩࡲࠫࡤࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫࠭᧭")
    bstack11ll1lllll1_opy_ = datetime.datetime.strptime(bstack11ll1l1llll_opy_, date_format)
    return bstack11ll1lllll1_opy_.isoformat() + bstack1l1l111_opy_ (u"ࠩ࡝ࠫ᧮")
def bstack11ll1l1ll11_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l1l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᧯")
    else:
        return bstack1l1l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ᧰")
def bstack11l1l1l1l1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l1l111_opy_ (u"ࠬࡺࡲࡶࡧࠪ᧱")
def bstack11lll1l111l_opy_(val):
    return val.__str__().lower() == bstack1l1l111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ᧲")
def bstack111lllll1l_opy_(bstack11llll11l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11llll11l11_opy_ as e:
                print(bstack1l1l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢ᧳").format(func.__name__, bstack11llll11l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11lll11ll11_opy_(bstack11lllll11l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11lllll11l1_opy_(cls, *args, **kwargs)
            except bstack11llll11l11_opy_ as e:
                print(bstack1l1l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣ᧴").format(bstack11lllll11l1_opy_.__name__, bstack11llll11l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11lll11ll11_opy_
    else:
        return decorator
def bstack111l111l1_opy_(bstack111l1l1ll1_opy_):
    if os.getenv(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ᧵")) is not None:
        return bstack11l1l1l1l1_opy_(os.getenv(bstack1l1l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭᧶")))
    if bstack1l1l111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᧷") in bstack111l1l1ll1_opy_ and bstack11lll1l111l_opy_(bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ᧸")]):
        return False
    if bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᧹") in bstack111l1l1ll1_opy_ and bstack11lll1l111l_opy_(bstack111l1l1ll1_opy_[bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ᧺")]):
        return False
    return True
def bstack11l1l1111_opy_():
    try:
        from pytest_bdd import reporting
        bstack11ll1l1l11l_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠣ᧻"), None)
        return bstack11ll1l1l11l_opy_ is None or bstack11ll1l1l11l_opy_ == bstack1l1l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨ᧼")
    except Exception as e:
        return False
def bstack11l1l1llll_opy_(hub_url, CONFIG):
    if bstack11l1lllll_opy_() <= version.parse(bstack1l1l111_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ᧽")):
        if hub_url:
            return bstack1l1l111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ᧾") + hub_url + bstack1l1l111_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ᧿")
        return bstack1lll11l1_opy_
    if hub_url:
        return bstack1l1l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᨀ") + hub_url + bstack1l1l111_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣᨁ")
    return bstack11lll11ll_opy_
def bstack11lllll111l_opy_():
    return isinstance(os.getenv(bstack1l1l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧᨂ")), str)
def bstack1l111ll1l1_opy_(url):
    return urlparse(url).hostname
def bstack1lll11ll1l_opy_(hostname):
    for bstack1111l1lll_opy_ in bstack1l11l11l11_opy_:
        regex = re.compile(bstack1111l1lll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11lll1l1l1l_opy_(bstack11lll11lll1_opy_, file_name, logger):
    bstack1l111l111l_opy_ = os.path.join(os.path.expanduser(bstack1l1l111_opy_ (u"ࠩࢁࠫᨃ")), bstack11lll11lll1_opy_)
    try:
        if not os.path.exists(bstack1l111l111l_opy_):
            os.makedirs(bstack1l111l111l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l1l111_opy_ (u"ࠪࢂࠬᨄ")), bstack11lll11lll1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l1l111_opy_ (u"ࠫࡼ࠭ᨅ")):
                pass
            with open(file_path, bstack1l1l111_opy_ (u"ࠧࡽࠫࠣᨆ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111ll1111_opy_.format(str(e)))
def bstack11ll11ll1ll_opy_(file_name, key, value, logger):
    file_path = bstack11lll1l1l1l_opy_(bstack1l1l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᨇ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l1ll111l1_opy_ = json.load(open(file_path, bstack1l1l111_opy_ (u"ࠧࡳࡤࠪᨈ")))
        else:
            bstack1l1ll111l1_opy_ = {}
        bstack1l1ll111l1_opy_[key] = value
        with open(file_path, bstack1l1l111_opy_ (u"ࠣࡹ࠮ࠦᨉ")) as outfile:
            json.dump(bstack1l1ll111l1_opy_, outfile)
def bstack11lll1l1l_opy_(file_name, logger):
    file_path = bstack11lll1l1l1l_opy_(bstack1l1l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᨊ"), file_name, logger)
    bstack1l1ll111l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l1l111_opy_ (u"ࠪࡶࠬᨋ")) as bstack1ll11l1l1l_opy_:
            bstack1l1ll111l1_opy_ = json.load(bstack1ll11l1l1l_opy_)
    return bstack1l1ll111l1_opy_
def bstack1l111ll111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࡀࠠࠨᨌ") + file_path + bstack1l1l111_opy_ (u"ࠬࠦࠧᨍ") + str(e))
def bstack11l1lllll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l1l111_opy_ (u"ࠨ࠼ࡏࡑࡗࡗࡊ࡚࠾ࠣᨎ")
def bstack1lll1l1l1_opy_(config):
    if bstack1l1l111_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᨏ") in config:
        del (config[bstack1l1l111_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᨐ")])
        return False
    if bstack11l1lllll_opy_() < version.parse(bstack1l1l111_opy_ (u"ࠩ࠶࠲࠹࠴࠰ࠨᨑ")):
        return False
    if bstack11l1lllll_opy_() >= version.parse(bstack1l1l111_opy_ (u"ࠪ࠸࠳࠷࠮࠶ࠩᨒ")):
        return True
    if bstack1l1l111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᨓ") in config and config[bstack1l1l111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᨔ")] is False:
        return False
    else:
        return True
def bstack1ll1lllll_opy_(args_list, bstack11ll1ll1ll1_opy_):
    index = -1
    for value in bstack11ll1ll1ll1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11l11l11ll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11l11l11ll_opy_ = bstack11l11l11ll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l1l111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᨕ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l1l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᨖ"), exception=exception)
    def bstack111l111ll1_opy_(self):
        if self.result != bstack1l1l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᨗ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l1l111_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲᨘࠧ") in self.exception_type:
            return bstack1l1l111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᨙ")
        return bstack1l1l111_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᨚ")
    def bstack11ll1l11l11_opy_(self):
        if self.result != bstack1l1l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᨛ"):
            return None
        if self.bstack11l11l11ll_opy_:
            return self.bstack11l11l11ll_opy_
        return bstack11ll1l1l1l1_opy_(self.exception)
def bstack11ll1l1l1l1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11lll11l1l1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11ll111l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1llll111_opy_(config, logger):
    try:
        import playwright
        bstack11llll11l1l_opy_ = playwright.__file__
        bstack11lll1ll111_opy_ = os.path.split(bstack11llll11l1l_opy_)
        bstack11ll11lll1l_opy_ = bstack11lll1ll111_opy_[0] + bstack1l1l111_opy_ (u"࠭࠯ࡥࡴ࡬ࡺࡪࡸ࠯ࡱࡣࡦ࡯ࡦ࡭ࡥ࠰࡮࡬ࡦ࠴ࡩ࡬ࡪ࠱ࡦࡰ࡮࠴ࡪࡴࠩ᨜")
        os.environ[bstack1l1l111_opy_ (u"ࠧࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠪ᨝")] = bstack11lll11l_opy_(config)
        with open(bstack11ll11lll1l_opy_, bstack1l1l111_opy_ (u"ࠨࡴࠪ᨞")) as f:
            bstack11l1l111l_opy_ = f.read()
            bstack11lll1l1111_opy_ = bstack1l1l111_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨ᨟")
            bstack11ll1l11ll1_opy_ = bstack11l1l111l_opy_.find(bstack11lll1l1111_opy_)
            if bstack11ll1l11ll1_opy_ == -1:
              process = subprocess.Popen(bstack1l1l111_opy_ (u"ࠥࡲࡵࡳࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠢᨠ"), shell=True, cwd=bstack11lll1ll111_opy_[0])
              process.wait()
              bstack11llll1ll11_opy_ = bstack1l1l111_opy_ (u"ࠫࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵࠤ࠾ࠫᨡ")
              bstack11lll111lll_opy_ = bstack1l1l111_opy_ (u"ࠧࠨࠢࠡ࡞ࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺ࡜ࠣ࠽ࠣࡧࡴࡴࡳࡵࠢࡾࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠠࡾࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬ࠯࠻ࠡ࡫ࡩࠤ࠭ࡶࡲࡰࡥࡨࡷࡸ࠴ࡥ࡯ࡸ࠱ࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠯ࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠫ࠭ࡀࠦࠢࠣࠤᨢ")
              bstack11lll1l1l11_opy_ = bstack11l1l111l_opy_.replace(bstack11llll1ll11_opy_, bstack11lll111lll_opy_)
              with open(bstack11ll11lll1l_opy_, bstack1l1l111_opy_ (u"࠭ࡷࠨᨣ")) as f:
                f.write(bstack11lll1l1l11_opy_)
    except Exception as e:
        logger.error(bstack11111l1ll_opy_.format(str(e)))
def bstack1ll1ll11_opy_():
  try:
    bstack11ll1l1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᨤ"))
    bstack11llll1l1ll_opy_ = []
    if os.path.exists(bstack11ll1l1ll1l_opy_):
      with open(bstack11ll1l1ll1l_opy_) as f:
        bstack11llll1l1ll_opy_ = json.load(f)
      os.remove(bstack11ll1l1ll1l_opy_)
    return bstack11llll1l1ll_opy_
  except:
    pass
  return []
def bstack1ll1l1l1l_opy_(bstack1l111ll1l_opy_):
  try:
    bstack11llll1l1ll_opy_ = []
    bstack11ll1l1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᨥ"))
    if os.path.exists(bstack11ll1l1ll1l_opy_):
      with open(bstack11ll1l1ll1l_opy_) as f:
        bstack11llll1l1ll_opy_ = json.load(f)
    bstack11llll1l1ll_opy_.append(bstack1l111ll1l_opy_)
    with open(bstack11ll1l1ll1l_opy_, bstack1l1l111_opy_ (u"ࠩࡺࠫᨦ")) as f:
        json.dump(bstack11llll1l1ll_opy_, f)
  except:
    pass
def bstack111l111ll_opy_(logger, bstack11lllll11ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l1l111_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭ᨧ"), bstack1l1l111_opy_ (u"ࠫࠬᨨ"))
    if test_name == bstack1l1l111_opy_ (u"ࠬ࠭ᨩ"):
        test_name = threading.current_thread().__dict__.get(bstack1l1l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡈࡤࡥࡡࡷࡩࡸࡺ࡟࡯ࡣࡰࡩࠬᨪ"), bstack1l1l111_opy_ (u"ࠧࠨᨫ"))
    bstack11llll11lll_opy_ = bstack1l1l111_opy_ (u"ࠨ࠮ࠣࠫᨬ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11lllll11ll_opy_:
        bstack1l11ll11l_opy_ = os.environ.get(bstack1l1l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᨭ"), bstack1l1l111_opy_ (u"ࠪ࠴ࠬᨮ"))
        bstack11ll11ll1_opy_ = {bstack1l1l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᨯ"): test_name, bstack1l1l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᨰ"): bstack11llll11lll_opy_, bstack1l1l111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᨱ"): bstack1l11ll11l_opy_}
        bstack11lllllll11_opy_ = []
        bstack11ll1lll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᨲ"))
        if os.path.exists(bstack11ll1lll11l_opy_):
            with open(bstack11ll1lll11l_opy_) as f:
                bstack11lllllll11_opy_ = json.load(f)
        bstack11lllllll11_opy_.append(bstack11ll11ll1_opy_)
        with open(bstack11ll1lll11l_opy_, bstack1l1l111_opy_ (u"ࠨࡹࠪᨳ")) as f:
            json.dump(bstack11lllllll11_opy_, f)
    else:
        bstack11ll11ll1_opy_ = {bstack1l1l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᨴ"): test_name, bstack1l1l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᨵ"): bstack11llll11lll_opy_, bstack1l1l111_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᨶ"): str(multiprocessing.current_process().name)}
        if bstack1l1l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩᨷ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11ll11ll1_opy_)
  except Exception as e:
      logger.warn(bstack1l1l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡲࡼࡸࡪࡹࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᨸ").format(e))
def bstack1ll1lll1_opy_(error_message, test_name, index, logger):
  try:
    bstack11lll1ll11l_opy_ = []
    bstack11ll11ll1_opy_ = {bstack1l1l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᨹ"): test_name, bstack1l1l111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᨺ"): error_message, bstack1l1l111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᨻ"): index}
    bstack11lll1111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᨼ"))
    if os.path.exists(bstack11lll1111l1_opy_):
        with open(bstack11lll1111l1_opy_) as f:
            bstack11lll1ll11l_opy_ = json.load(f)
    bstack11lll1ll11l_opy_.append(bstack11ll11ll1_opy_)
    with open(bstack11lll1111l1_opy_, bstack1l1l111_opy_ (u"ࠫࡼ࠭ᨽ")) as f:
        json.dump(bstack11lll1ll11l_opy_, f)
  except Exception as e:
    logger.warn(bstack1l1l111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᨾ").format(e))
def bstack11l111lll_opy_(bstack1l1l11lll1_opy_, name, logger):
  try:
    bstack11ll11ll1_opy_ = {bstack1l1l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᨿ"): name, bstack1l1l111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᩀ"): bstack1l1l11lll1_opy_, bstack1l1l111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᩁ"): str(threading.current_thread()._name)}
    return bstack11ll11ll1_opy_
  except Exception as e:
    logger.warn(bstack1l1l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᩂ").format(e))
  return
def bstack11lllll1ll1_opy_():
    return platform.system() == bstack1l1l111_opy_ (u"࡛ࠪ࡮ࡴࡤࡰࡹࡶࠫᩃ")
def bstack1l1l1l1111_opy_(bstack11lll11l1ll_opy_, config, logger):
    bstack11ll1l111l1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11lll11l1ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫࡯ࡸࡪࡸࠠࡤࡱࡱࡪ࡮࡭ࠠ࡬ࡧࡼࡷࠥࡨࡹࠡࡴࡨ࡫ࡪࡾࠠ࡮ࡣࡷࡧ࡭ࡀࠠࡼࡿࠥᩄ").format(e))
    return bstack11ll1l111l1_opy_
def bstack11lll1lllll_opy_(bstack11lll1l11l1_opy_, bstack11lll111ll1_opy_):
    bstack11lll111l1l_opy_ = version.parse(bstack11lll1l11l1_opy_)
    bstack11ll1ll1111_opy_ = version.parse(bstack11lll111ll1_opy_)
    if bstack11lll111l1l_opy_ > bstack11ll1ll1111_opy_:
        return 1
    elif bstack11lll111l1l_opy_ < bstack11ll1ll1111_opy_:
        return -1
    else:
        return 0
def bstack111ll1111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11ll11lllll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack11lll11l111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll1ll111_opy_(options, framework, bstack1lll1l1l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l1l111_opy_ (u"ࠬ࡭ࡥࡵࠩᩅ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11ll1lll_opy_ = caps.get(bstack1l1l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᩆ"))
    bstack11ll1l11111_opy_ = True
    bstack1lll11ll_opy_ = os.environ[bstack1l1l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᩇ")]
    if bstack11lll1l111l_opy_(caps.get(bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨ࡛࠸ࡉࠧᩈ"))) or bstack11lll1l111l_opy_(caps.get(bstack1l1l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩᩉ"))):
        bstack11ll1l11111_opy_ = False
    if bstack1lll1l1l1_opy_({bstack1l1l111_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥᩊ"): bstack11ll1l11111_opy_}):
        bstack11ll1lll_opy_ = bstack11ll1lll_opy_ or {}
        bstack11ll1lll_opy_[bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᩋ")] = bstack11lll11l111_opy_(framework)
        bstack11ll1lll_opy_[bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᩌ")] = bstack1ll111111l1_opy_()
        bstack11ll1lll_opy_[bstack1l1l111_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᩍ")] = bstack1lll11ll_opy_
        bstack11ll1lll_opy_[bstack1l1l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᩎ")] = bstack1lll1l1l_opy_
        if getattr(options, bstack1l1l111_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᩏ"), None):
            options.set_capability(bstack1l1l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᩐ"), bstack11ll1lll_opy_)
        else:
            options[bstack1l1l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᩑ")] = bstack11ll1lll_opy_
    else:
        if getattr(options, bstack1l1l111_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬᩒ"), None):
            options.set_capability(bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᩓ"), bstack11lll11l111_opy_(framework))
            options.set_capability(bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᩔ"), bstack1ll111111l1_opy_())
            options.set_capability(bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᩕ"), bstack1lll11ll_opy_)
            options.set_capability(bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᩖ"), bstack1lll1l1l_opy_)
        else:
            options[bstack1l1l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᩗ")] = bstack11lll11l111_opy_(framework)
            options[bstack1l1l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᩘ")] = bstack1ll111111l1_opy_()
            options[bstack1l1l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᩙ")] = bstack1lll11ll_opy_
            options[bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᩚ")] = bstack1lll1l1l_opy_
    return options
def bstack11ll11ll1l1_opy_(bstack11ll1ll11l1_opy_, framework):
    bstack1lll1l1l_opy_ = bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣᩛ"))
    if bstack11ll1ll11l1_opy_ and len(bstack11ll1ll11l1_opy_.split(bstack1l1l111_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᩜ"))) > 1:
        ws_url = bstack11ll1ll11l1_opy_.split(bstack1l1l111_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᩝ"))[0]
        if bstack1l1l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᩞ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack11ll1ll1l1l_opy_ = json.loads(urllib.parse.unquote(bstack11ll1ll11l1_opy_.split(bstack1l1l111_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩ᩟"))[1]))
            bstack11ll1ll1l1l_opy_ = bstack11ll1ll1l1l_opy_ or {}
            bstack1lll11ll_opy_ = os.environ[bstack1l1l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅ᩠ࠩ")]
            bstack11ll1ll1l1l_opy_[bstack1l1l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᩡ")] = str(framework) + str(__version__)
            bstack11ll1ll1l1l_opy_[bstack1l1l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᩢ")] = bstack1ll111111l1_opy_()
            bstack11ll1ll1l1l_opy_[bstack1l1l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᩣ")] = bstack1lll11ll_opy_
            bstack11ll1ll1l1l_opy_[bstack1l1l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᩤ")] = bstack1lll1l1l_opy_
            bstack11ll1ll11l1_opy_ = bstack11ll1ll11l1_opy_.split(bstack1l1l111_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᩥ"))[0] + bstack1l1l111_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᩦ") + urllib.parse.quote(json.dumps(bstack11ll1ll1l1l_opy_))
    return bstack11ll1ll11l1_opy_
def bstack1111l11l_opy_():
    global bstack1l1ll11ll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l1ll11ll_opy_ = BrowserType.connect
    return bstack1l1ll11ll_opy_
def bstack1l1lll111l_opy_(framework_name):
    global bstack111l111l_opy_
    bstack111l111l_opy_ = framework_name
    return framework_name
def bstack1l1lll111_opy_(self, *args, **kwargs):
    global bstack1l1ll11ll_opy_
    try:
        global bstack111l111l_opy_
        if bstack1l1l111_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᩧ") in kwargs:
            kwargs[bstack1l1l111_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩᩨ")] = bstack11ll11ll1l1_opy_(
                kwargs.get(bstack1l1l111_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪᩩ"), None),
                bstack111l111l_opy_
            )
    except Exception as e:
        logger.error(bstack1l1l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡕࡇࡏࠥࡩࡡࡱࡵ࠽ࠤࢀࢃࠢᩪ").format(str(e)))
    return bstack1l1ll11ll_opy_(self, *args, **kwargs)
def bstack11llllll1ll_opy_(bstack11ll1llll11_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11ll1llll1_opy_(bstack11ll1llll11_opy_, bstack1l1l111_opy_ (u"ࠣࠤᩫ"))
        if proxies and proxies.get(bstack1l1l111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣᩬ")):
            parsed_url = urlparse(proxies.get(bstack1l1l111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤᩭ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l1l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧᩮ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l1l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨᩯ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l1l111_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩᩰ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l1l111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪᩱ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1lllll1111_opy_(bstack11ll1llll11_opy_):
    bstack11llllll111_opy_ = {
        bstack1l1111l1ll1_opy_[bstack11ll1l1lll1_opy_]: bstack11ll1llll11_opy_[bstack11ll1l1lll1_opy_]
        for bstack11ll1l1lll1_opy_ in bstack11ll1llll11_opy_
        if bstack11ll1l1lll1_opy_ in bstack1l1111l1ll1_opy_
    }
    bstack11llllll111_opy_[bstack1l1l111_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣᩲ")] = bstack11llllll1ll_opy_(bstack11ll1llll11_opy_, bstack111l11l1l_opy_.get_property(bstack1l1l111_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤᩳ")))
    bstack11lll1l1lll_opy_ = [element.lower() for element in bstack1l11111l11l_opy_]
    bstack11ll1ll1l11_opy_(bstack11llllll111_opy_, bstack11lll1l1lll_opy_)
    return bstack11llllll111_opy_
def bstack11ll1ll1l11_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l1l111_opy_ (u"ࠥ࠮࠯࠰ࠪࠣᩴ")
    for value in d.values():
        if isinstance(value, dict):
            bstack11ll1ll1l11_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack11ll1ll1l11_opy_(item, keys)
def bstack11ll1ll11ll_opy_():
    bstack11ll1l11lll_opy_ = [os.environ.get(bstack1l1l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡎࡒࡅࡔࡡࡇࡍࡗࠨ᩵")), os.path.join(os.path.expanduser(bstack1l1l111_opy_ (u"ࠧࢄࠢ᩶")), bstack1l1l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭᩷")), os.path.join(bstack1l1l111_opy_ (u"ࠧ࠰ࡶࡰࡴࠬ᩸"), bstack1l1l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᩹"))]
    for path in bstack11ll1l11lll_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l1l111_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࠨࠤ᩺") + str(path) + bstack1l1l111_opy_ (u"ࠥࠫࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨ᩻"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l1l111_opy_ (u"ࠦࡌ࡯ࡶࡪࡰࡪࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠢࡩࡳࡷࠦࠧࠣ᩼") + str(path) + bstack1l1l111_opy_ (u"ࠧ࠭ࠢ᩽"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l1l111_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨ᩾") + str(path) + bstack1l1l111_opy_ (u"ࠢࠨࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡬ࡦࡹࠠࡵࡪࡨࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶ࠲᩿ࠧ"))
            else:
                logger.debug(bstack1l1l111_opy_ (u"ࠣࡅࡵࡩࡦࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࠩࠥ᪀") + str(path) + bstack1l1l111_opy_ (u"ࠤࠪࠤࡼ࡯ࡴࡩࠢࡺࡶ࡮ࡺࡥࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲ࠳ࠨ᪁"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l1l111_opy_ (u"ࠥࡓࡵ࡫ࡲࡢࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠢࡩࡳࡷࠦࠧࠣ᪂") + str(path) + bstack1l1l111_opy_ (u"ࠦࠬ࠴ࠢ᪃"))
            return path
        except Exception as e:
            logger.debug(bstack1l1l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡻࡰࠡࡨ࡬ࡰࡪࠦࠧࡼࡲࡤࡸ࡭ࢃࠧ࠻ࠢࠥ᪄") + str(e) + bstack1l1l111_opy_ (u"ࠨࠢ᪅"))
    logger.debug(bstack1l1l111_opy_ (u"ࠢࡂ࡮࡯ࠤࡵࡧࡴࡩࡵࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠦ᪆"))
    return None
@measure(event_name=EVENTS.bstack1l11111lll1_opy_, stage=STAGE.bstack1l1l1111l_opy_)
def bstack1llllllll11_opy_(binary_path, bstack1llllll111l_opy_, bs_config):
    logger.debug(bstack1l1l111_opy_ (u"ࠣࡅࡸࡶࡷ࡫࡮ࡵࠢࡆࡐࡎࠦࡐࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦ࠽ࠤࢀࢃࠢ᪇").format(binary_path))
    bstack11llllll1l1_opy_ = bstack1l1l111_opy_ (u"ࠩࠪ᪈")
    bstack11lll111111_opy_ = {
        bstack1l1l111_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ᪉"): __version__,
        bstack1l1l111_opy_ (u"ࠦࡴࡹࠢ᪊"): platform.system(),
        bstack1l1l111_opy_ (u"ࠧࡵࡳࡠࡣࡵࡧ࡭ࠨ᪋"): platform.machine(),
        bstack1l1l111_opy_ (u"ࠨࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠦ᪌"): bstack1l1l111_opy_ (u"ࠧ࠱ࠩ᪍"),
        bstack1l1l111_opy_ (u"ࠣࡵࡧ࡯ࡤࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠢ᪎"): bstack1l1l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ᪏")
    }
    try:
        if binary_path:
            bstack11lll111111_opy_[bstack1l1l111_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ᪐")] = subprocess.check_output([binary_path, bstack1l1l111_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧ᪑")]).strip().decode(bstack1l1l111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᪒"))
        response = requests.request(
            bstack1l1l111_opy_ (u"࠭ࡇࡆࡖࠪ᪓"),
            url=bstack11ll1111_opy_(bstack1l1111lll11_opy_),
            headers=None,
            auth=(bs_config[bstack1l1l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ᪔")], bs_config[bstack1l1l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ᪕")]),
            json=None,
            params=bstack11lll111111_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l1l111_opy_ (u"ࠩࡸࡶࡱ࠭᪖") in data.keys() and bstack1l1l111_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡧࡣࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ᪗") in data.keys():
            logger.debug(bstack1l1l111_opy_ (u"ࠦࡓ࡫ࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡨࡩ࡯ࡣࡵࡽ࠱ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠧ᪘").format(bstack11lll111111_opy_[bstack1l1l111_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪ᪙")]))
            bstack11lll1ll1ll_opy_ = bstack11ll11ll11l_opy_(data[bstack1l1l111_opy_ (u"࠭ࡵࡳ࡮ࠪ᪚")], bstack1llllll111l_opy_)
            bstack11llllll1l1_opy_ = os.path.join(bstack1llllll111l_opy_, bstack11lll1ll1ll_opy_)
            os.chmod(bstack11llllll1l1_opy_, 0o777) # bstack11ll1l111ll_opy_ permission
            return bstack11llllll1l1_opy_
    except Exception as e:
        logger.debug(bstack1l1l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡲࡪࡽࠠࡔࡆࡎࠤࢀࢃࠢ᪛").format(e))
    return binary_path
@measure(event_name=EVENTS.bstack1l1111l11ll_opy_, stage=STAGE.bstack1l1l1111l_opy_)
def bstack11ll11ll11l_opy_(bstack11lllll1l11_opy_, bstack11lll1lll11_opy_):
    logger.debug(bstack1l1l111_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭࠻ࠢࠥ᪜") + str(bstack11lllll1l11_opy_) + bstack1l1l111_opy_ (u"ࠤࠥ᪝"))
    zip_path = os.path.join(bstack11lll1lll11_opy_, bstack1l1l111_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࡟ࡧ࡫࡯ࡩ࠳ࢀࡩࡱࠤ᪞"))
    bstack11lll1ll1ll_opy_ = bstack1l1l111_opy_ (u"ࠫࠬ᪟")
    with requests.get(bstack11lllll1l11_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l1l111_opy_ (u"ࠧࡽࡢࠣ᪠")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l1l111_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿ࠮ࠣ᪡"))
    with zipfile.ZipFile(zip_path, bstack1l1l111_opy_ (u"ࠧࡳࠩ᪢")) as zip_ref:
        bstack11lllll1111_opy_ = zip_ref.namelist()
        if len(bstack11lllll1111_opy_) > 0:
            bstack11lll1ll1ll_opy_ = bstack11lllll1111_opy_[0] # bstack11ll1l11l1l_opy_ bstack1l1111ll1ll_opy_ will be bstack11ll1llll1l_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack11lll1lll11_opy_)
        logger.debug(bstack1l1l111_opy_ (u"ࠣࡈ࡬ࡰࡪࡹࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡥࡹࡶࡵࡥࡨࡺࡥࡥࠢࡷࡳࠥ࠭ࠢ᪣") + str(bstack11lll1lll11_opy_) + bstack1l1l111_opy_ (u"ࠤࠪࠦ᪤"))
    os.remove(zip_path)
    return bstack11lll1ll1ll_opy_
def get_cli_dir():
    bstack11llll11111_opy_ = bstack11ll1ll11ll_opy_()
    if bstack11llll11111_opy_:
        bstack1llllll111l_opy_ = os.path.join(bstack11llll11111_opy_, bstack1l1l111_opy_ (u"ࠥࡧࡱ࡯ࠢ᪥"))
        if not os.path.exists(bstack1llllll111l_opy_):
            os.makedirs(bstack1llllll111l_opy_, mode=0o777, exist_ok=True)
        return bstack1llllll111l_opy_
    else:
        raise FileNotFoundError(bstack1l1l111_opy_ (u"ࠦࡓࡵࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࡺࡨࡦࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾ࠴ࠢ᪦"))
def bstack1lll1lll1l1_opy_(bstack1llllll111l_opy_):
    bstack1l1l111_opy_ (u"ࠧࠨࠢࡈࡧࡷࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡳࠦࡡࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠢࠣࠤᪧ")
    bstack11ll1llllll_opy_ = [
        os.path.join(bstack1llllll111l_opy_, f)
        for f in os.listdir(bstack1llllll111l_opy_)
        if os.path.isfile(os.path.join(bstack1llllll111l_opy_, f)) and f.startswith(bstack1l1l111_opy_ (u"ࠨࡢࡪࡰࡤࡶࡾ࠳ࠢ᪨"))
    ]
    if len(bstack11ll1llllll_opy_) > 0:
        return max(bstack11ll1llllll_opy_, key=os.path.getmtime) # get bstack11llll111ll_opy_ binary
    return bstack1l1l111_opy_ (u"ࠢࠣ᪩")