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
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1llll_opy_
bstack111l11l1l_opy_ = Config.bstack11lll1ll_opy_()
def bstack11l111l11ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l111l111l_opy_(bstack11l111l1l1l_opy_, bstack11l1111llll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l111l1l1l_opy_):
        with open(bstack11l111l1l1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l111l11ll_opy_(bstack11l111l1l1l_opy_):
        pac = get_pac(url=bstack11l111l1l1l_opy_)
    else:
        raise Exception(bstack1l1l111_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭᯿").format(bstack11l111l1l1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l1l111_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᰀ"), 80))
        bstack11l111l1l11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l111l1l11_opy_ = bstack1l1l111_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᰁ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1111llll_opy_, bstack11l111l1l11_opy_)
    return proxy_url
def bstack111lll1l1_opy_(config):
    return bstack1l1l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᰂ") in config or bstack1l1l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᰃ") in config
def bstack11lll11l_opy_(config):
    if not bstack111lll1l1_opy_(config):
        return
    if config.get(bstack1l1l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᰄ")):
        return config.get(bstack1l1l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᰅ"))
    if config.get(bstack1l1l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᰆ")):
        return config.get(bstack1l1l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᰇ"))
def bstack11ll1llll1_opy_(config, bstack11l1111llll_opy_):
    proxy = bstack11lll11l_opy_(config)
    proxies = {}
    if config.get(bstack1l1l111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᰈ")) or config.get(bstack1l1l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᰉ")):
        if proxy.endswith(bstack1l1l111_opy_ (u"ࠪ࠲ࡵࡧࡣࠨᰊ")):
            proxies = bstack1l11ll1l_opy_(proxy, bstack11l1111llll_opy_)
        else:
            proxies = {
                bstack1l1l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᰋ"): proxy
            }
    bstack111l11l1l_opy_.bstack11lll11111_opy_(bstack1l1l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬᰌ"), proxies)
    return proxies
def bstack1l11ll1l_opy_(bstack11l111l1l1l_opy_, bstack11l1111llll_opy_):
    proxies = {}
    global bstack11l111l11l1_opy_
    if bstack1l1l111_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩᰍ") in globals():
        return bstack11l111l11l1_opy_
    try:
        proxy = bstack11l111l111l_opy_(bstack11l111l1l1l_opy_, bstack11l1111llll_opy_)
        if bstack1l1l111_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢᰎ") in proxy:
            proxies = {}
        elif bstack1l1l111_opy_ (u"ࠣࡊࡗࡘࡕࠨᰏ") in proxy or bstack1l1l111_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣᰐ") in proxy or bstack1l1l111_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤᰑ") in proxy:
            bstack11l111l1111_opy_ = proxy.split(bstack1l1l111_opy_ (u"ࠦࠥࠨᰒ"))
            if bstack1l1l111_opy_ (u"ࠧࡀ࠯࠰ࠤᰓ") in bstack1l1l111_opy_ (u"ࠨࠢᰔ").join(bstack11l111l1111_opy_[1:]):
                proxies = {
                    bstack1l1l111_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᰕ"): bstack1l1l111_opy_ (u"ࠣࠤᰖ").join(bstack11l111l1111_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᰗ"): str(bstack11l111l1111_opy_[0]).lower() + bstack1l1l111_opy_ (u"ࠥ࠾࠴࠵ࠢᰘ") + bstack1l1l111_opy_ (u"ࠦࠧᰙ").join(bstack11l111l1111_opy_[1:])
                }
        elif bstack1l1l111_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦᰚ") in proxy:
            bstack11l111l1111_opy_ = proxy.split(bstack1l1l111_opy_ (u"ࠨࠠࠣᰛ"))
            if bstack1l1l111_opy_ (u"ࠢ࠻࠱࠲ࠦᰜ") in bstack1l1l111_opy_ (u"ࠣࠤᰝ").join(bstack11l111l1111_opy_[1:]):
                proxies = {
                    bstack1l1l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᰞ"): bstack1l1l111_opy_ (u"ࠥࠦᰟ").join(bstack11l111l1111_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᰠ"): bstack1l1l111_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᰡ") + bstack1l1l111_opy_ (u"ࠨࠢᰢ").join(bstack11l111l1111_opy_[1:])
                }
        else:
            proxies = {
                bstack1l1l111_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᰣ"): proxy
            }
    except Exception as e:
        print(bstack1l1l111_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧᰤ"), bstack11l1ll1llll_opy_.format(bstack11l111l1l1l_opy_, str(e)))
    bstack11l111l11l1_opy_ = proxies
    return proxies