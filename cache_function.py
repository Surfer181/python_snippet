# -*- coding: utf-8 -*-
import time
from functools import wraps

def cache(func):
    memo = {}

    @wraps(func)
    def _wrapper(*args):
        res = memo.get(args, None)
        if res is not None:
            return res
        else:
            res = func(*args)
            memo[args] = res
            # print(memo)
        return res
    return _wrapper


@cache
def long_time_fun(n):
    time.sleep(1)
    return n


if __name__ == '__main__':
    for i in range(3) + range(3):
        print(long_time_fun(i))
