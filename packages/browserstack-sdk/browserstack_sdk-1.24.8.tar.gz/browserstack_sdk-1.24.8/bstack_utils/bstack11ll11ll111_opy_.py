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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11lll1lllll_opy_
from browserstack_sdk.bstack11llll111_opy_ import bstack1l11l111_opy_
def _11ll11l1l1l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11ll11l111l_opy_:
    def __init__(self, handler):
        self._11ll11l11l1_opy_ = {}
        self._11ll111lll1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1l11l111_opy_.version()
        if bstack11lll1lllll_opy_(pytest_version, bstack1l1l111_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢ᪪")) >= 0:
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᪫")] = Module._register_setup_function_fixture
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᪬")] = Module._register_setup_module_fixture
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᪭")] = Class._register_setup_class_fixture
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᪮")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᪯"))
            Module._register_setup_module_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᪰"))
            Class._register_setup_class_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᪱"))
            Class._register_setup_method_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᪲"))
        else:
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᪳")] = Module._inject_setup_function_fixture
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᪴")] = Module._inject_setup_module_fixture
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩ᪵ࠬ")] = Class._inject_setup_class_fixture
            self._11ll11l11l1_opy_[bstack1l1l111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫᪶ࠧ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧ᪷ࠪ"))
            Module._inject_setup_module_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦ᪸ࠩ"))
            Class._inject_setup_class_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦ᪹ࠩ"))
            Class._inject_setup_method_fixture = self.bstack11ll111l1l1_opy_(bstack1l1l111_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ᪺ࠫ"))
    def bstack11ll111l11l_opy_(self, bstack11ll11l1l11_opy_, hook_type):
        bstack11ll11l1111_opy_ = id(bstack11ll11l1l11_opy_.__class__)
        if (bstack11ll11l1111_opy_, hook_type) in self._11ll111lll1_opy_:
            return
        meth = getattr(bstack11ll11l1l11_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11ll111lll1_opy_[(bstack11ll11l1111_opy_, hook_type)] = meth
            setattr(bstack11ll11l1l11_opy_, hook_type, self.bstack11ll111ll11_opy_(hook_type, bstack11ll11l1111_opy_))
    def bstack11ll11l1lll_opy_(self, instance, bstack11ll11l11ll_opy_):
        if bstack11ll11l11ll_opy_ == bstack1l1l111_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢ᪻"):
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨ᪼"))
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰ᪽ࠥ"))
        if bstack11ll11l11ll_opy_ == bstack1l1l111_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣ᪾"):
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ᪿࠢ"))
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨᫀࠦ"))
        if bstack11ll11l11ll_opy_ == bstack1l1l111_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥ᫁"):
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤ᫂"))
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨ᫃"))
        if bstack11ll11l11ll_opy_ == bstack1l1l111_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫᫄ࠢ"):
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨ᫅"))
            self.bstack11ll111l11l_opy_(instance.obj, bstack1l1l111_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥ᫆"))
    @staticmethod
    def bstack11ll111llll_opy_(hook_type, func, args):
        if hook_type in [bstack1l1l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨ᫇"), bstack1l1l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬ᫈")]:
            _11ll11l1l1l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11ll111ll11_opy_(self, hook_type, bstack11ll11l1111_opy_):
        def bstack11ll11l1ll1_opy_(arg=None):
            self.handler(hook_type, bstack1l1l111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ᫉"))
            result = None
            try:
                bstack11111lll11_opy_ = self._11ll111lll1_opy_[(bstack11ll11l1111_opy_, hook_type)]
                self.bstack11ll111llll_opy_(hook_type, bstack11111lll11_opy_, (arg,))
                result = Result(result=bstack1l1l111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨ᫊ࠬ"))
            except Exception as e:
                result = Result(result=bstack1l1l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᫋"), exception=e)
                self.handler(hook_type, bstack1l1l111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᫌ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1l111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᫍ"), result)
        def bstack11ll111ll1l_opy_(this, arg=None):
            self.handler(hook_type, bstack1l1l111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᫎ"))
            result = None
            exception = None
            try:
                self.bstack11ll111llll_opy_(hook_type, self._11ll111lll1_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l1l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᫏"))
            except Exception as e:
                result = Result(result=bstack1l1l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᫐"), exception=e)
                self.handler(hook_type, bstack1l1l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ᫑"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1l111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ᫒"), result)
        if hook_type in [bstack1l1l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭᫓"), bstack1l1l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪ᫔")]:
            return bstack11ll111ll1l_opy_
        return bstack11ll11l1ll1_opy_
    def bstack11ll111l1l1_opy_(self, bstack11ll11l11ll_opy_):
        def bstack11ll111l1ll_opy_(this, *args, **kwargs):
            self.bstack11ll11l1lll_opy_(this, bstack11ll11l11ll_opy_)
            self._11ll11l11l1_opy_[bstack11ll11l11ll_opy_](this, *args, **kwargs)
        return bstack11ll111l1ll_opy_