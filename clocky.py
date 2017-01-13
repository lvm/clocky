#!/usr/bin/env python

import time

def clocky(f):
    def tick(*args, **kwargs):
        _start = time.time()
        _func = f(*args, **kwargs)
        _end = time.time()

        t_sec = round(_end-_start)
        (t_min, t_sec) = divmod(t_sec,60)
        (t_hour,t_min) = divmod(t_min,60)
        print ("Time passed: {:02d}:{:02d}:{:02d}".format(*map(int, (t_hour,t_min,t_sec))))

        return _func
    return tick
