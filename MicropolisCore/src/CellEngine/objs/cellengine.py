# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_cellengine')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_cellengine')
    _cellengine = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cellengine', [dirname(__file__)])
        except ImportError:
            import _cellengine
            return _cellengine
        try:
            _mod = imp.load_module('_cellengine', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _cellengine = swig_import_helper()
    del swig_import_helper
else:
    import _cellengine
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

_LINUXCOMPAT_H_ = _cellengine._LINUXCOMPAT_H_
class RECT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RECT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RECT, name)
    __repr__ = _swig_repr
    __swig_setmethods__["left"] = _cellengine.RECT_left_set
    __swig_getmethods__["left"] = _cellengine.RECT_left_get
    if _newclass:
        left = _swig_property(_cellengine.RECT_left_get, _cellengine.RECT_left_set)
    __swig_setmethods__["right"] = _cellengine.RECT_right_set
    __swig_getmethods__["right"] = _cellengine.RECT_right_get
    if _newclass:
        right = _swig_property(_cellengine.RECT_right_get, _cellengine.RECT_right_set)
    __swig_setmethods__["top"] = _cellengine.RECT_top_set
    __swig_getmethods__["top"] = _cellengine.RECT_top_get
    if _newclass:
        top = _swig_property(_cellengine.RECT_top_get, _cellengine.RECT_top_set)
    __swig_setmethods__["bottom"] = _cellengine.RECT_bottom_set
    __swig_getmethods__["bottom"] = _cellengine.RECT_bottom_get
    if _newclass:
        bottom = _swig_property(_cellengine.RECT_bottom_get, _cellengine.RECT_bottom_set)

    def __init__(self):
        this = _cellengine.new_RECT()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cellengine.delete_RECT
    __del__ = lambda self: None
RECT_swigregister = _cellengine.RECT_swigregister
RECT_swigregister(RECT)

CELLENGINE_VERSION = _cellengine.CELLENGINE_VERSION

def Rand32():
    return _cellengine.Rand32()
Rand32 = _cellengine.Rand32

def Rand16():
    return _cellengine.Rand16()
Rand16 = _cellengine.Rand16

def Rand8():
    return _cellengine.Rand8()
Rand8 = _cellengine.Rand8

def PrimeRandoms():
    return _cellengine.PrimeRandoms()
PrimeRandoms = _cellengine.PrimeRandoms

def FeedRandom(food):
    return _cellengine.FeedRandom(food)
FeedRandom = _cellengine.FeedRandom
class CellEngine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CellEngine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CellEngine, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _cellengine.CellEngine_name_set
    __swig_getmethods__["name"] = _cellengine.CellEngine_name_get
    if _newclass:
        name = _swig_property(_cellengine.CellEngine_name_get, _cellengine.CellEngine_name_set)
    __swig_setmethods__["screenMem"] = _cellengine.CellEngine_screenMem_set
    __swig_getmethods__["screenMem"] = _cellengine.CellEngine_screenMem_get
    if _newclass:
        screenMem = _swig_property(_cellengine.CellEngine_screenMem_get, _cellengine.CellEngine_screenMem_set)
    __swig_setmethods__["screenWidth"] = _cellengine.CellEngine_screenWidth_set
    __swig_getmethods__["screenWidth"] = _cellengine.CellEngine_screenWidth_get
    if _newclass:
        screenWidth = _swig_property(_cellengine.CellEngine_screenWidth_get, _cellengine.CellEngine_screenWidth_set)
    __swig_setmethods__["screenHeight"] = _cellengine.CellEngine_screenHeight_set
    __swig_getmethods__["screenHeight"] = _cellengine.CellEngine_screenHeight_get
    if _newclass:
        screenHeight = _swig_property(_cellengine.CellEngine_screenHeight_get, _cellengine.CellEngine_screenHeight_set)
    __swig_setmethods__["screenRowBytes"] = _cellengine.CellEngine_screenRowBytes_set
    __swig_getmethods__["screenRowBytes"] = _cellengine.CellEngine_screenRowBytes_get
    if _newclass:
        screenRowBytes = _swig_property(_cellengine.CellEngine_screenRowBytes_get, _cellengine.CellEngine_screenRowBytes_set)
    __swig_setmethods__["backMem"] = _cellengine.CellEngine_backMem_set
    __swig_getmethods__["backMem"] = _cellengine.CellEngine_backMem_get
    if _newclass:
        backMem = _swig_property(_cellengine.CellEngine_backMem_get, _cellengine.CellEngine_backMem_set)
    __swig_setmethods__["backSize"] = _cellengine.CellEngine_backSize_set
    __swig_getmethods__["backSize"] = _cellengine.CellEngine_backSize_get
    if _newclass:
        backSize = _swig_property(_cellengine.CellEngine_backSize_get, _cellengine.CellEngine_backSize_set)
    __swig_setmethods__["backRowBytes"] = _cellengine.CellEngine_backRowBytes_set
    __swig_getmethods__["backRowBytes"] = _cellengine.CellEngine_backRowBytes_get
    if _newclass:
        backRowBytes = _swig_property(_cellengine.CellEngine_backRowBytes_get, _cellengine.CellEngine_backRowBytes_set)
    __swig_setmethods__["backWidth"] = _cellengine.CellEngine_backWidth_set
    __swig_getmethods__["backWidth"] = _cellengine.CellEngine_backWidth_get
    if _newclass:
        backWidth = _swig_property(_cellengine.CellEngine_backWidth_get, _cellengine.CellEngine_backWidth_set)
    __swig_setmethods__["backHeight"] = _cellengine.CellEngine_backHeight_set
    __swig_getmethods__["backHeight"] = _cellengine.CellEngine_backHeight_get
    if _newclass:
        backHeight = _swig_property(_cellengine.CellEngine_backHeight_get, _cellengine.CellEngine_backHeight_set)
    __swig_setmethods__["backBorder"] = _cellengine.CellEngine_backBorder_set
    __swig_getmethods__["backBorder"] = _cellengine.CellEngine_backBorder_get
    if _newclass:
        backBorder = _swig_property(_cellengine.CellEngine_backBorder_get, _cellengine.CellEngine_backBorder_set)
    __swig_setmethods__["frontMem"] = _cellengine.CellEngine_frontMem_set
    __swig_getmethods__["frontMem"] = _cellengine.CellEngine_frontMem_get
    if _newclass:
        frontMem = _swig_property(_cellengine.CellEngine_frontMem_get, _cellengine.CellEngine_frontMem_set)
    __swig_setmethods__["maskMem"] = _cellengine.CellEngine_maskMem_set
    __swig_getmethods__["maskMem"] = _cellengine.CellEngine_maskMem_get
    if _newclass:
        maskMem = _swig_property(_cellengine.CellEngine_maskMem_get, _cellengine.CellEngine_maskMem_set)
    __swig_setmethods__["maskRowBytes"] = _cellengine.CellEngine_maskRowBytes_set
    __swig_getmethods__["maskRowBytes"] = _cellengine.CellEngine_maskRowBytes_get
    if _newclass:
        maskRowBytes = _swig_property(_cellengine.CellEngine_maskRowBytes_get, _cellengine.CellEngine_maskRowBytes_set)
    __swig_setmethods__["maskWidth"] = _cellengine.CellEngine_maskWidth_set
    __swig_getmethods__["maskWidth"] = _cellengine.CellEngine_maskWidth_get
    if _newclass:
        maskWidth = _swig_property(_cellengine.CellEngine_maskWidth_get, _cellengine.CellEngine_maskWidth_set)
    __swig_setmethods__["maskHeight"] = _cellengine.CellEngine_maskHeight_set
    __swig_getmethods__["maskHeight"] = _cellengine.CellEngine_maskHeight_get
    if _newclass:
        maskHeight = _swig_property(_cellengine.CellEngine_maskHeight_get, _cellengine.CellEngine_maskHeight_set)
    __swig_setmethods__["masked"] = _cellengine.CellEngine_masked_set
    __swig_getmethods__["masked"] = _cellengine.CellEngine_masked_get
    if _newclass:
        masked = _swig_property(_cellengine.CellEngine_masked_get, _cellengine.CellEngine_masked_set)
    __swig_setmethods__["neighborhood"] = _cellengine.CellEngine_neighborhood_set
    __swig_getmethods__["neighborhood"] = _cellengine.CellEngine_neighborhood_get
    if _newclass:
        neighborhood = _swig_property(_cellengine.CellEngine_neighborhood_get, _cellengine.CellEngine_neighborhood_set)
    __swig_setmethods__["rule"] = _cellengine.CellEngine_rule_set
    __swig_getmethods__["rule"] = _cellengine.CellEngine_rule_get
    if _newclass:
        rule = _swig_property(_cellengine.CellEngine_rule_get, _cellengine.CellEngine_rule_set)
    __swig_setmethods__["ruleStatic"] = _cellengine.CellEngine_ruleStatic_set
    __swig_getmethods__["ruleStatic"] = _cellengine.CellEngine_ruleStatic_get
    if _newclass:
        ruleStatic = _swig_property(_cellengine.CellEngine_ruleStatic_get, _cellengine.CellEngine_ruleStatic_set)
    __swig_setmethods__["ruleSize"] = _cellengine.CellEngine_ruleSize_set
    __swig_getmethods__["ruleSize"] = _cellengine.CellEngine_ruleSize_get
    if _newclass:
        ruleSize = _swig_property(_cellengine.CellEngine_ruleSize_get, _cellengine.CellEngine_ruleSize_set)
    __swig_setmethods__["ruleName"] = _cellengine.CellEngine_ruleName_set
    __swig_getmethods__["ruleName"] = _cellengine.CellEngine_ruleName_get
    if _newclass:
        ruleName = _swig_property(_cellengine.CellEngine_ruleName_get, _cellengine.CellEngine_ruleName_set)
    __swig_setmethods__["x"] = _cellengine.CellEngine_x_set
    __swig_getmethods__["x"] = _cellengine.CellEngine_x_get
    if _newclass:
        x = _swig_property(_cellengine.CellEngine_x_get, _cellengine.CellEngine_x_set)
    __swig_setmethods__["y"] = _cellengine.CellEngine_y_set
    __swig_getmethods__["y"] = _cellengine.CellEngine_y_get
    if _newclass:
        y = _swig_property(_cellengine.CellEngine_y_get, _cellengine.CellEngine_y_set)
    __swig_setmethods__["dx"] = _cellengine.CellEngine_dx_set
    __swig_getmethods__["dx"] = _cellengine.CellEngine_dx_get
    if _newclass:
        dx = _swig_property(_cellengine.CellEngine_dx_get, _cellengine.CellEngine_dx_set)
    __swig_setmethods__["dy"] = _cellengine.CellEngine_dy_set
    __swig_getmethods__["dy"] = _cellengine.CellEngine_dy_get
    if _newclass:
        dy = _swig_property(_cellengine.CellEngine_dy_get, _cellengine.CellEngine_dy_set)
    __swig_setmethods__["width"] = _cellengine.CellEngine_width_set
    __swig_getmethods__["width"] = _cellengine.CellEngine_width_get
    if _newclass:
        width = _swig_property(_cellengine.CellEngine_width_get, _cellengine.CellEngine_width_set)
    __swig_setmethods__["height"] = _cellengine.CellEngine_height_set
    __swig_getmethods__["height"] = _cellengine.CellEngine_height_get
    if _newclass:
        height = _swig_property(_cellengine.CellEngine_height_get, _cellengine.CellEngine_height_set)
    __swig_setmethods__["idealWidth"] = _cellengine.CellEngine_idealWidth_set
    __swig_getmethods__["idealWidth"] = _cellengine.CellEngine_idealWidth_get
    if _newclass:
        idealWidth = _swig_property(_cellengine.CellEngine_idealWidth_get, _cellengine.CellEngine_idealWidth_set)
    __swig_setmethods__["idealHeight"] = _cellengine.CellEngine_idealHeight_set
    __swig_getmethods__["idealHeight"] = _cellengine.CellEngine_idealHeight_get
    if _newclass:
        idealHeight = _swig_property(_cellengine.CellEngine_idealHeight_get, _cellengine.CellEngine_idealHeight_set)
    __swig_setmethods__["phase"] = _cellengine.CellEngine_phase_set
    __swig_getmethods__["phase"] = _cellengine.CellEngine_phase_get
    if _newclass:
        phase = _swig_property(_cellengine.CellEngine_phase_get, _cellengine.CellEngine_phase_set)
    __swig_setmethods__["ticks"] = _cellengine.CellEngine_ticks_set
    __swig_getmethods__["ticks"] = _cellengine.CellEngine_ticks_get
    if _newclass:
        ticks = _swig_property(_cellengine.CellEngine_ticks_get, _cellengine.CellEngine_ticks_set)
    __swig_setmethods__["wrap"] = _cellengine.CellEngine_wrap_set
    __swig_getmethods__["wrap"] = _cellengine.CellEngine_wrap_get
    if _newclass:
        wrap = _swig_property(_cellengine.CellEngine_wrap_get, _cellengine.CellEngine_wrap_set)
    __swig_setmethods__["steps"] = _cellengine.CellEngine_steps_set
    __swig_getmethods__["steps"] = _cellengine.CellEngine_steps_get
    if _newclass:
        steps = _swig_property(_cellengine.CellEngine_steps_get, _cellengine.CellEngine_steps_set)
    __swig_setmethods__["frob"] = _cellengine.CellEngine_frob_set
    __swig_getmethods__["frob"] = _cellengine.CellEngine_frob_get
    if _newclass:
        frob = _swig_property(_cellengine.CellEngine_frob_get, _cellengine.CellEngine_frob_set)
    __swig_setmethods__["rumble"] = _cellengine.CellEngine_rumble_set
    __swig_getmethods__["rumble"] = _cellengine.CellEngine_rumble_get
    if _newclass:
        rumble = _swig_property(_cellengine.CellEngine_rumble_get, _cellengine.CellEngine_rumble_set)
    __swig_setmethods__["rumblemax"] = _cellengine.CellEngine_rumblemax_set
    __swig_getmethods__["rumblemax"] = _cellengine.CellEngine_rumblemax_get
    if _newclass:
        rumblemax = _swig_property(_cellengine.CellEngine_rumblemax_get, _cellengine.CellEngine_rumblemax_set)
    __swig_setmethods__["hubba"] = _cellengine.CellEngine_hubba_set
    __swig_getmethods__["hubba"] = _cellengine.CellEngine_hubba_get
    if _newclass:
        hubba = _swig_property(_cellengine.CellEngine_hubba_get, _cellengine.CellEngine_hubba_set)
    __swig_setmethods__["inflation"] = _cellengine.CellEngine_inflation_set
    __swig_getmethods__["inflation"] = _cellengine.CellEngine_inflation_get
    if _newclass:
        inflation = _swig_property(_cellengine.CellEngine_inflation_get, _cellengine.CellEngine_inflation_set)
    __swig_setmethods__["high"] = _cellengine.CellEngine_high_set
    __swig_getmethods__["high"] = _cellengine.CellEngine_high_get
    if _newclass:
        high = _swig_property(_cellengine.CellEngine_high_get, _cellengine.CellEngine_high_set)
    __swig_setmethods__["low"] = _cellengine.CellEngine_low_set
    __swig_getmethods__["low"] = _cellengine.CellEngine_low_get
    if _newclass:
        low = _swig_property(_cellengine.CellEngine_low_get, _cellengine.CellEngine_low_set)
    __swig_setmethods__["maskClip"] = _cellengine.CellEngine_maskClip_set
    __swig_getmethods__["maskClip"] = _cellengine.CellEngine_maskClip_get
    if _newclass:
        maskClip = _swig_property(_cellengine.CellEngine_maskClip_get, _cellengine.CellEngine_maskClip_set)
    __swig_setmethods__["moveImage"] = _cellengine.CellEngine_moveImage_set
    __swig_getmethods__["moveImage"] = _cellengine.CellEngine_moveImage_get
    if _newclass:
        moveImage = _swig_property(_cellengine.CellEngine_moveImage_get, _cellengine.CellEngine_moveImage_set)
    __swig_setmethods__["numbera"] = _cellengine.CellEngine_numbera_set
    __swig_getmethods__["numbera"] = _cellengine.CellEngine_numbera_get
    if _newclass:
        numbera = _swig_property(_cellengine.CellEngine_numbera_get, _cellengine.CellEngine_numbera_set)
    __swig_setmethods__["numberb"] = _cellengine.CellEngine_numberb_set
    __swig_getmethods__["numberb"] = _cellengine.CellEngine_numberb_get
    if _newclass:
        numberb = _swig_property(_cellengine.CellEngine_numberb_get, _cellengine.CellEngine_numberb_set)
    __swig_setmethods__["numberc"] = _cellengine.CellEngine_numberc_set
    __swig_getmethods__["numberc"] = _cellengine.CellEngine_numberc_get
    if _newclass:
        numberc = _swig_property(_cellengine.CellEngine_numberc_get, _cellengine.CellEngine_numberc_set)
    __swig_setmethods__["anglea"] = _cellengine.CellEngine_anglea_set
    __swig_getmethods__["anglea"] = _cellengine.CellEngine_anglea_get
    if _newclass:
        anglea = _swig_property(_cellengine.CellEngine_anglea_get, _cellengine.CellEngine_anglea_set)
    __swig_setmethods__["angleb"] = _cellengine.CellEngine_angleb_set
    __swig_getmethods__["angleb"] = _cellengine.CellEngine_angleb_get
    if _newclass:
        angleb = _swig_property(_cellengine.CellEngine_angleb_get, _cellengine.CellEngine_angleb_set)
    __swig_setmethods__["anglec"] = _cellengine.CellEngine_anglec_set
    __swig_getmethods__["anglec"] = _cellengine.CellEngine_anglec_get
    if _newclass:
        anglec = _swig_property(_cellengine.CellEngine_anglec_get, _cellengine.CellEngine_anglec_set)
    __swig_setmethods__["pointax"] = _cellengine.CellEngine_pointax_set
    __swig_getmethods__["pointax"] = _cellengine.CellEngine_pointax_get
    if _newclass:
        pointax = _swig_property(_cellengine.CellEngine_pointax_get, _cellengine.CellEngine_pointax_set)
    __swig_setmethods__["pointay"] = _cellengine.CellEngine_pointay_set
    __swig_getmethods__["pointay"] = _cellengine.CellEngine_pointay_get
    if _newclass:
        pointay = _swig_property(_cellengine.CellEngine_pointay_get, _cellengine.CellEngine_pointay_set)
    __swig_setmethods__["pointbx"] = _cellengine.CellEngine_pointbx_set
    __swig_getmethods__["pointbx"] = _cellengine.CellEngine_pointbx_get
    if _newclass:
        pointbx = _swig_property(_cellengine.CellEngine_pointbx_get, _cellengine.CellEngine_pointbx_set)
    __swig_setmethods__["pointby"] = _cellengine.CellEngine_pointby_set
    __swig_getmethods__["pointby"] = _cellengine.CellEngine_pointby_get
    if _newclass:
        pointby = _swig_property(_cellengine.CellEngine_pointby_get, _cellengine.CellEngine_pointby_set)
    __swig_setmethods__["pointcx"] = _cellengine.CellEngine_pointcx_set
    __swig_getmethods__["pointcx"] = _cellengine.CellEngine_pointcx_get
    if _newclass:
        pointcx = _swig_property(_cellengine.CellEngine_pointcx_get, _cellengine.CellEngine_pointcx_set)
    __swig_setmethods__["pointcy"] = _cellengine.CellEngine_pointcy_set
    __swig_getmethods__["pointcy"] = _cellengine.CellEngine_pointcy_get
    if _newclass:
        pointcy = _swig_property(_cellengine.CellEngine_pointcy_get, _cellengine.CellEngine_pointcy_set)
    __swig_setmethods__["clipRects"] = _cellengine.CellEngine_clipRects_set
    __swig_getmethods__["clipRects"] = _cellengine.CellEngine_clipRects_get
    if _newclass:
        clipRects = _swig_property(_cellengine.CellEngine_clipRects_get, _cellengine.CellEngine_clipRects_set)
    __swig_setmethods__["rectList"] = _cellengine.CellEngine_rectList_set
    __swig_getmethods__["rectList"] = _cellengine.CellEngine_rectList_get
    if _newclass:
        rectList = _swig_property(_cellengine.CellEngine_rectList_get, _cellengine.CellEngine_rectList_set)
    __swig_setmethods__["skips"] = _cellengine.CellEngine_skips_set
    __swig_getmethods__["skips"] = _cellengine.CellEngine_skips_get
    if _newclass:
        skips = _swig_property(_cellengine.CellEngine_skips_get, _cellengine.CellEngine_skips_set)
    __swig_setmethods__["skip"] = _cellengine.CellEngine_skip_set
    __swig_getmethods__["skip"] = _cellengine.CellEngine_skip_get
    if _newclass:
        skip = _swig_property(_cellengine.CellEngine_skip_get, _cellengine.CellEngine_skip_set)
    __swig_setmethods__["total"] = _cellengine.CellEngine_total_set
    __swig_getmethods__["total"] = _cellengine.CellEngine_total_get
    if _newclass:
        total = _swig_property(_cellengine.CellEngine_total_get, _cellengine.CellEngine_total_set)
    __swig_setmethods__["tracking"] = _cellengine.CellEngine_tracking_set
    __swig_getmethods__["tracking"] = _cellengine.CellEngine_tracking_get
    if _newclass:
        tracking = _swig_property(_cellengine.CellEngine_tracking_get, _cellengine.CellEngine_tracking_set)
    __swig_setmethods__["action"] = _cellengine.CellEngine_action_set
    __swig_getmethods__["action"] = _cellengine.CellEngine_action_get
    if _newclass:
        action = _swig_property(_cellengine.CellEngine_action_get, _cellengine.CellEngine_action_set)
    __swig_setmethods__["downx"] = _cellengine.CellEngine_downx_set
    __swig_getmethods__["downx"] = _cellengine.CellEngine_downx_get
    if _newclass:
        downx = _swig_property(_cellengine.CellEngine_downx_get, _cellengine.CellEngine_downx_set)
    __swig_setmethods__["downy"] = _cellengine.CellEngine_downy_set
    __swig_getmethods__["downy"] = _cellengine.CellEngine_downy_get
    if _newclass:
        downy = _swig_property(_cellengine.CellEngine_downy_get, _cellengine.CellEngine_downy_set)
    __swig_setmethods__["grabx"] = _cellengine.CellEngine_grabx_set
    __swig_getmethods__["grabx"] = _cellengine.CellEngine_grabx_get
    if _newclass:
        grabx = _swig_property(_cellengine.CellEngine_grabx_get, _cellengine.CellEngine_grabx_set)
    __swig_setmethods__["graby"] = _cellengine.CellEngine_graby_set
    __swig_getmethods__["graby"] = _cellengine.CellEngine_graby_get
    if _newclass:
        graby = _swig_property(_cellengine.CellEngine_graby_get, _cellengine.CellEngine_graby_set)
    __swig_setmethods__["lastx"] = _cellengine.CellEngine_lastx_set
    __swig_getmethods__["lastx"] = _cellengine.CellEngine_lastx_get
    if _newclass:
        lastx = _swig_property(_cellengine.CellEngine_lastx_get, _cellengine.CellEngine_lastx_set)
    __swig_setmethods__["lasty"] = _cellengine.CellEngine_lasty_set
    __swig_getmethods__["lasty"] = _cellengine.CellEngine_lasty_get
    if _newclass:
        lasty = _swig_property(_cellengine.CellEngine_lasty_get, _cellengine.CellEngine_lasty_set)
    __swig_setmethods__["saveskips"] = _cellengine.CellEngine_saveskips_set
    __swig_getmethods__["saveskips"] = _cellengine.CellEngine_saveskips_get
    if _newclass:
        saveskips = _swig_property(_cellengine.CellEngine_saveskips_get, _cellengine.CellEngine_saveskips_set)
    __swig_setmethods__["still"] = _cellengine.CellEngine_still_set
    __swig_getmethods__["still"] = _cellengine.CellEngine_still_get
    if _newclass:
        still = _swig_property(_cellengine.CellEngine_still_get, _cellengine.CellEngine_still_set)
    __swig_setmethods__["gravx"] = _cellengine.CellEngine_gravx_set
    __swig_getmethods__["gravx"] = _cellengine.CellEngine_gravx_get
    if _newclass:
        gravx = _swig_property(_cellengine.CellEngine_gravx_get, _cellengine.CellEngine_gravx_set)
    __swig_setmethods__["gravy"] = _cellengine.CellEngine_gravy_set
    __swig_getmethods__["gravy"] = _cellengine.CellEngine_gravy_get
    if _newclass:
        gravy = _swig_property(_cellengine.CellEngine_gravy_get, _cellengine.CellEngine_gravy_set)
    __swig_setmethods__["grabbable"] = _cellengine.CellEngine_grabbable_set
    __swig_getmethods__["grabbable"] = _cellengine.CellEngine_grabbable_get
    if _newclass:
        grabbable = _swig_property(_cellengine.CellEngine_grabbable_get, _cellengine.CellEngine_grabbable_set)
    __swig_setmethods__["data"] = _cellengine.CellEngine_data_set
    __swig_getmethods__["data"] = _cellengine.CellEngine_data_get
    if _newclass:
        data = _swig_property(_cellengine.CellEngine_data_get, _cellengine.CellEngine_data_set)

    def __init__(self):
        this = _cellengine.new_CellEngine()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cellengine.delete_CellEngine
    __del__ = lambda self: None

    def Init(self):
        return _cellengine.CellEngine_Init(self)

    def InitScreen(self, ww, hh):
        return _cellengine.CellEngine_InitScreen(self, ww, hh)

    def SetRect(self, xx, yy, ww, hh):
        return _cellengine.CellEngine_SetRect(self, xx, yy, ww, hh)

    def SetPos(self, xx, yy):
        return _cellengine.CellEngine_SetPos(self, xx, yy)

    def SetSize(self, ww, hh):
        return _cellengine.CellEngine_SetSize(self, ww, hh)

    def ForceOnScreen(self):
        return _cellengine.CellEngine_ForceOnScreen(self)

    def OnScreen(self):
        return _cellengine.CellEngine_OnScreen(self)

    def Garble(self):
        return _cellengine.CellEngine_Garble(self)

    def GarbleRect(self, xx, yy, ww, hh):
        return _cellengine.CellEngine_GarbleRect(self, xx, yy, ww, hh)

    def Fill(self, c):
        return _cellengine.CellEngine_Fill(self, c)

    def FillRect(self, c, xx, yy, ww, hh):
        return _cellengine.CellEngine_FillRect(self, c, xx, yy, ww, hh)

    def ResetMask(self):
        return _cellengine.CellEngine_ResetMask(self)

    def SetMask(self, ww, hh, data, rb):
        return _cellengine.CellEngine_SetMask(self, ww, hh, data, rb)

    def UpdateClip(self):
        return _cellengine.CellEngine_UpdateClip(self)

    def LoadRule(self, name):
        return _cellengine.CellEngine_LoadRule(self, name)

    def LoadRuleData(self, stream):
        return _cellengine.CellEngine_LoadRuleData(self, stream)

    def LoadStaticRuleData(self, stream):
        return _cellengine.CellEngine_LoadStaticRuleData(self, stream)

    def SetRuleTable(self, rule, ruleSize, neigh):
        return _cellengine.CellEngine_SetRuleTable(self, rule, ruleSize, neigh)

    def CountRules(self):
        return _cellengine.CellEngine_CountRules(self)

    def GetRuleName(self, i):
        return _cellengine.CellEngine_GetRuleName(self, i)

    def GetRuleData(self, i):
        return _cellengine.CellEngine_GetRuleData(self, i)

    def DoPhysics(self):
        return _cellengine.CellEngine_DoPhysics(self)

    def DoRule(self):
        return _cellengine.CellEngine_DoRule(self)

    def PostRule(self):
        return _cellengine.CellEngine_PostRule(self)

    def CopyToBack(self):
        return _cellengine.CellEngine_CopyToBack(self)

    def PumpToFront(self):
        return _cellengine.CellEngine_PumpToFront(self)

    def GetCell(self, col, row):
        return _cellengine.CellEngine_GetCell(self, col, row)

    def SetCell(self, col, row, cell):
        return _cellengine.CellEngine_SetCell(self, col, row, cell)

    def GetCellBuffer(self):
        return _cellengine.CellEngine_GetCellBuffer(self)

    def n_moore_a(self):
        return _cellengine.CellEngine_n_moore_a(self)

    def n_moore_ab(self):
        return _cellengine.CellEngine_n_moore_ab(self)

    def n_vonn_neumann(self):
        return _cellengine.CellEngine_n_vonn_neumann(self)

    def n_margolis(self):
        return _cellengine.CellEngine_n_margolis(self)

    def n_margolis_ph(self):
        return _cellengine.CellEngine_n_margolis_ph(self)

    def n_margolis_hv(self):
        return _cellengine.CellEngine_n_margolis_hv(self)

    def n_life(self):
        return _cellengine.CellEngine_n_life(self)

    def n_brain(self):
        return _cellengine.CellEngine_n_brain(self)

    def n_heat(self):
        return _cellengine.CellEngine_n_heat(self)

    def n_dheat(self):
        return _cellengine.CellEngine_n_dheat(self)

    def n_lheat(self):
        return _cellengine.CellEngine_n_lheat(self)

    def n_ldheat(self):
        return _cellengine.CellEngine_n_ldheat(self)

    def n_abdheat(self):
        return _cellengine.CellEngine_n_abdheat(self)

    def n_abcdheat(self):
        return _cellengine.CellEngine_n_abcdheat(self)

    def n_edheat(self):
        return _cellengine.CellEngine_n_edheat(self)

    def n_ranch(self):
        return _cellengine.CellEngine_n_ranch(self)

    def n_anneal(self):
        return _cellengine.CellEngine_n_anneal(self)

    def n_anneal4(self):
        return _cellengine.CellEngine_n_anneal4(self)

    def n_anneal8(self):
        return _cellengine.CellEngine_n_anneal8(self)

    def n_eco(self):
        return _cellengine.CellEngine_n_eco(self)

    def n_torben(self):
        return _cellengine.CellEngine_n_torben(self)

    def n_torben2(self):
        return _cellengine.CellEngine_n_torben2(self)

    def n_torben3(self):
        return _cellengine.CellEngine_n_torben3(self)

    def n_torben4(self):
        return _cellengine.CellEngine_n_torben4(self)

    def n_ball(self):
        return _cellengine.CellEngine_n_ball(self)

    def n_fdheat(self):
        return _cellengine.CellEngine_n_fdheat(self)

    def n_fabcdheat(self):
        return _cellengine.CellEngine_n_fabcdheat(self)

    def n_risca(self):
        return _cellengine.CellEngine_n_risca(self)

    def n_insert(self):
        return _cellengine.CellEngine_n_insert(self)

    def n_heaco(self):
        return _cellengine.CellEngine_n_heaco(self)

    def n_marble(self):
        return _cellengine.CellEngine_n_marble(self)

    def n_smarble(self):
        return _cellengine.CellEngine_n_smarble(self)

    def n_farble(self):
        return _cellengine.CellEngine_n_farble(self)

    def n_garble(self):
        return _cellengine.CellEngine_n_garble(self)

    def n_garblebug(self):
        return _cellengine.CellEngine_n_garblebug(self)

    def n_twoheats(self):
        return _cellengine.CellEngine_n_twoheats(self)

    def n_spin(self):
        return _cellengine.CellEngine_n_spin(self)

    def n_driven(self):
        return _cellengine.CellEngine_n_driven(self)

    def n_daft(self):
        return _cellengine.CellEngine_n_daft(self)

    def n_spinsonly(self):
        return _cellengine.CellEngine_n_spinsonly(self)

    def n_spinsbank(self):
        return _cellengine.CellEngine_n_spinsbank(self)

    def n_spinsheat(self):
        return _cellengine.CellEngine_n_spinsheat(self)

    def n_spinglass(self):
        return _cellengine.CellEngine_n_spinglass(self)

    def n_glassbonds(self):
        return _cellengine.CellEngine_n_glassbonds(self)

    def n_glassheat(self):
        return _cellengine.CellEngine_n_glassheat(self)

    def n_faders(self):
        return _cellengine.CellEngine_n_faders(self)

    def n_harble(self):
        return _cellengine.CellEngine_n_harble(self)

    def n_perlin(self):
        return _cellengine.CellEngine_n_perlin(self)

    def n_dendrite(self):
        return _cellengine.CellEngine_n_dendrite(self)

    def n_vanneal(self):
        return _cellengine.CellEngine_n_vanneal(self)

    def n_vanneal8(self):
        return _cellengine.CellEngine_n_vanneal8(self)

    def n_jvn29(self):
        return _cellengine.CellEngine_n_jvn29(self)

    def SetRuleBuffer(self, buf, neigh):
        return _cellengine.CellEngine_SetRuleBuffer(self, buf, neigh)
CellEngine_swigregister = _cellengine.CellEngine_swigregister
CellEngine_swigregister(CellEngine)

EVENT_BOUNCE_TOP = _cellengine.EVENT_BOUNCE_TOP
EVENT_BOUNCE_BOTTOM = _cellengine.EVENT_BOUNCE_BOTTOM
EVENT_BOUNCE_LEFT = _cellengine.EVENT_BOUNCE_LEFT
EVENT_BOUNCE_RIGHT = _cellengine.EVENT_BOUNCE_RIGHT
EVENT_MOVE = _cellengine.EVENT_MOVE
sNORTHWEST = _cellengine.sNORTHWEST
sNORTH = _cellengine.sNORTH
sNORTHEAST = _cellengine.sNORTHEAST
sWEST = _cellengine.sWEST
sCENTER = _cellengine.sCENTER
sEAST = _cellengine.sEAST
sSOUTHWEST = _cellengine.sSOUTHWEST
sSOUTH = _cellengine.sSOUTH
sSOUTHEAST = _cellengine.sSOUTHEAST
# This file is compatible with both classic and new-style classes.


