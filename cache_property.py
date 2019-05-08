# -*- coding: utf-8 -*-
import time


class _Missing(object):
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'


_missing = _Missing()    # 伪单例


class cached_property(object):
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class TestCache(object):
    @cached_property
    def long_time_func(self):
        print('from function')
        time.sleep(1)
        return time.time()


def test():
    t = TestCache()
    print(t.long_time_func)
    print(t.long_time_func)
    print(t.long_time_func)


test()
