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
        mname = '.'.join((pkg, '_SPP')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_SPP')
    _SPP = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_SPP', [dirname(__file__)])
        except ImportError:
            import _SPP
            return _SPP
        try:
            _mod = imp.load_module('_SPP', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _SPP = swig_import_helper()
    del swig_import_helper
else:
    import _SPP
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

import collections
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _SPP.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _SPP.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _SPP.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _SPP.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _SPP.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _SPP.SwigPyIterator_equal(self, x)

    def copy(self):
        return _SPP.SwigPyIterator_copy(self)

    def next(self):
        return _SPP.SwigPyIterator_next(self)

    def __next__(self):
        return _SPP.SwigPyIterator___next__(self)

    def previous(self):
        return _SPP.SwigPyIterator_previous(self)

    def advance(self, n):
        return _SPP.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _SPP.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _SPP.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _SPP.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _SPP.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _SPP.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _SPP.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _SPP.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VecFloat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecFloat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecFloat, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _SPP.VecFloat_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _SPP.VecFloat___nonzero__(self)

    def __bool__(self):
        return _SPP.VecFloat___bool__(self)

    def __len__(self):
        return _SPP.VecFloat___len__(self)

    def __getslice__(self, i, j):
        return _SPP.VecFloat___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _SPP.VecFloat___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _SPP.VecFloat___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _SPP.VecFloat___delitem__(self, *args)

    def __getitem__(self, *args):
        return _SPP.VecFloat___getitem__(self, *args)

    def __setitem__(self, *args):
        return _SPP.VecFloat___setitem__(self, *args)

    def pop(self):
        return _SPP.VecFloat_pop(self)

    def append(self, x):
        return _SPP.VecFloat_append(self, x)

    def empty(self):
        return _SPP.VecFloat_empty(self)

    def size(self):
        return _SPP.VecFloat_size(self)

    def swap(self, v):
        return _SPP.VecFloat_swap(self, v)

    def begin(self):
        return _SPP.VecFloat_begin(self)

    def end(self):
        return _SPP.VecFloat_end(self)

    def rbegin(self):
        return _SPP.VecFloat_rbegin(self)

    def rend(self):
        return _SPP.VecFloat_rend(self)

    def clear(self):
        return _SPP.VecFloat_clear(self)

    def get_allocator(self):
        return _SPP.VecFloat_get_allocator(self)

    def pop_back(self):
        return _SPP.VecFloat_pop_back(self)

    def erase(self, *args):
        return _SPP.VecFloat_erase(self, *args)

    def __init__(self, *args):
        this = _SPP.new_VecFloat(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _SPP.VecFloat_push_back(self, x)

    def front(self):
        return _SPP.VecFloat_front(self)

    def back(self):
        return _SPP.VecFloat_back(self)

    def assign(self, n, x):
        return _SPP.VecFloat_assign(self, n, x)

    def resize(self, *args):
        return _SPP.VecFloat_resize(self, *args)

    def insert(self, *args):
        return _SPP.VecFloat_insert(self, *args)

    def reserve(self, n):
        return _SPP.VecFloat_reserve(self, n)

    def capacity(self):
        return _SPP.VecFloat_capacity(self)
    __swig_destroy__ = _SPP.delete_VecFloat
    __del__ = lambda self: None
VecFloat_swigregister = _SPP.VecFloat_swigregister
VecFloat_swigregister(VecFloat)

class VecVecFloat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecVecFloat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecVecFloat, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _SPP.VecVecFloat_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _SPP.VecVecFloat___nonzero__(self)

    def __bool__(self):
        return _SPP.VecVecFloat___bool__(self)

    def __len__(self):
        return _SPP.VecVecFloat___len__(self)

    def __getslice__(self, i, j):
        return _SPP.VecVecFloat___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _SPP.VecVecFloat___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _SPP.VecVecFloat___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _SPP.VecVecFloat___delitem__(self, *args)

    def __getitem__(self, *args):
        return _SPP.VecVecFloat___getitem__(self, *args)

    def __setitem__(self, *args):
        return _SPP.VecVecFloat___setitem__(self, *args)

    def pop(self):
        return _SPP.VecVecFloat_pop(self)

    def append(self, x):
        return _SPP.VecVecFloat_append(self, x)

    def empty(self):
        return _SPP.VecVecFloat_empty(self)

    def size(self):
        return _SPP.VecVecFloat_size(self)

    def swap(self, v):
        return _SPP.VecVecFloat_swap(self, v)

    def begin(self):
        return _SPP.VecVecFloat_begin(self)

    def end(self):
        return _SPP.VecVecFloat_end(self)

    def rbegin(self):
        return _SPP.VecVecFloat_rbegin(self)

    def rend(self):
        return _SPP.VecVecFloat_rend(self)

    def clear(self):
        return _SPP.VecVecFloat_clear(self)

    def get_allocator(self):
        return _SPP.VecVecFloat_get_allocator(self)

    def pop_back(self):
        return _SPP.VecVecFloat_pop_back(self)

    def erase(self, *args):
        return _SPP.VecVecFloat_erase(self, *args)

    def __init__(self, *args):
        this = _SPP.new_VecVecFloat(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _SPP.VecVecFloat_push_back(self, x)

    def front(self):
        return _SPP.VecVecFloat_front(self)

    def back(self):
        return _SPP.VecVecFloat_back(self)

    def assign(self, n, x):
        return _SPP.VecVecFloat_assign(self, n, x)

    def resize(self, *args):
        return _SPP.VecVecFloat_resize(self, *args)

    def insert(self, *args):
        return _SPP.VecVecFloat_insert(self, *args)

    def reserve(self, n):
        return _SPP.VecVecFloat_reserve(self, n)

    def capacity(self):
        return _SPP.VecVecFloat_capacity(self)
    __swig_destroy__ = _SPP.delete_VecVecFloat
    __del__ = lambda self: None
VecVecFloat_swigregister = _SPP.VecVecFloat_swigregister
VecVecFloat_swigregister(VecVecFloat)

PI = _SPP.PI

def normalize(x, y, z):
    return _SPP.normalize(x, y, z)
normalize = _SPP.normalize

def point_plane_distance(point, plane_norm, plane_point):
    return _SPP.point_plane_distance(point, plane_norm, plane_point)
point_plane_distance = _SPP.point_plane_distance

def to_spherical(dir):
    return _SPP.to_spherical(dir)
to_spherical = _SPP.to_spherical

def to_polar(dir):
    return _SPP.to_polar(dir)
to_polar = _SPP.to_polar

def to_2Dcartesian(theta):
    return _SPP.to_2Dcartesian(theta)
to_2Dcartesian = _SPP.to_2Dcartesian

def to_3Dcartesian(theta, phi):
    return _SPP.to_3Dcartesian(theta, phi)
to_3Dcartesian = _SPP.to_3Dcartesian
class SPP(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SPP, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SPP, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cell_centers"] = _SPP.SPP_cell_centers_set
    __swig_getmethods__["cell_centers"] = _SPP.SPP_cell_centers_get
    if _newclass:
        cell_centers = _swig_property(_SPP.SPP_cell_centers_get, _SPP.SPP_cell_centers_set)
    __swig_setmethods__["cell_directions"] = _SPP.SPP_cell_directions_set
    __swig_getmethods__["cell_directions"] = _SPP.SPP_cell_directions_get
    if _newclass:
        cell_directions = _swig_property(_SPP.SPP_cell_directions_get, _SPP.SPP_cell_directions_set)
    __swig_setmethods__["plane_pts"] = _SPP.SPP_plane_pts_set
    __swig_getmethods__["plane_pts"] = _SPP.SPP_plane_pts_get
    if _newclass:
        plane_pts = _swig_property(_SPP.SPP_plane_pts_get, _SPP.SPP_plane_pts_set)
    __swig_setmethods__["plane_norms"] = _SPP.SPP_plane_norms_set
    __swig_getmethods__["plane_norms"] = _SPP.SPP_plane_norms_get
    if _newclass:
        plane_norms = _swig_property(_SPP.SPP_plane_norms_get, _SPP.SPP_plane_norms_set)
    __swig_setmethods__["dt"] = _SPP.SPP_dt_set
    __swig_getmethods__["dt"] = _SPP.SPP_dt_get
    if _newclass:
        dt = _swig_property(_SPP.SPP_dt_get, _SPP.SPP_dt_set)
    __swig_setmethods__["radius"] = _SPP.SPP_radius_set
    __swig_getmethods__["radius"] = _SPP.SPP_radius_get
    if _newclass:
        radius = _swig_property(_SPP.SPP_radius_get, _SPP.SPP_radius_set)

    def __init__(self, dt_c=0.01, gamma_c=1, gamma_s_c=1, radius_c=1, W_s_c=1, W_c_c=1, f_pol_c=1, D_r_c=0.001, F_m_c=1, z_axis_c=True):
        this = _SPP.new_SPP(dt_c, gamma_c, gamma_s_c, radius_c, W_s_c, W_c_c, f_pol_c, D_r_c, F_m_c, z_axis_c)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def addCell(self, pos_x=0, pos_y=0, pos_z=0, dir_1=0, dir_2=0, dir_3=0):
        return _SPP.SPP_addCell(self, pos_x, pos_y, pos_z, dir_1, dir_2, dir_3)

    def addPlane(self, p_x, p_y, p_z, n_x, n_y, n_z):
        return _SPP.SPP_addPlane(self, p_x, p_y, p_z, n_x, n_y, n_z)

    def step(self):
        return _SPP.SPP_step(self)

    def find_cell_contacts(self):
        return _SPP.SPP_find_cell_contacts(self)

    def find_plane_contacts(self):
        return _SPP.SPP_find_plane_contacts(self)

    def move_cells(self, cell_contacts, plane_contacts):
        return _SPP.SPP_move_cells(self, cell_contacts, plane_contacts)

    def repolarize(self):
        return _SPP.SPP_repolarize(self)
    __swig_destroy__ = _SPP.delete_SPP
    __del__ = lambda self: None
SPP_swigregister = _SPP.SPP_swigregister
SPP_swigregister(SPP)

# This file is compatible with both classic and new-style classes.


