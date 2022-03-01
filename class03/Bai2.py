
def children(o:list):
    i = o.index(None)
    res = []
    if i not in (0,1,2):
        _o_cpy = o.copy()
        _o_cpy[i],_o_cpy[i-3] = _o_cpy[i-3],_o_cpy[i]
        res.append(_o_cpy)
    if i not in (6,7,8):
        _o_cpy = o.copy()
        _o_cpy[i],_o_cpy[i+3] = _o_cpy[i+3],_o_cpy[i]
        res.append(_o_cpy)
    if i not in (0,3,6):
        _o_cpy = o.copy()
        _o_cpy[i],_o_cpy[i-1] = _o_cpy[i-1],_o_cpy[i]
        res.append(_o_cpy)
    if i not in (2,5,8):
        _o_cpy = o.copy()
        _o_cpy[i],_o_cpy[i+1] = _o_cpy[i+1],_o_cpy[i]
        res.append(_o_cpy)
    return res



_start = [1,None,4,6,3,2,7,8,5]
_goal = [1,2,3,4,5,6,7,8,None]
_trace = {tuple(_start): None}
OK = False

_open = [_start]
_close = []

while _open:
    o = _open.pop()
    _close.append(o)

    if o == _goal:
        OK = True
        print(OK)
        break
    for child in children(o):
        if child not in _open and child not in _close:
            _open.append(child)
            _trace[tuple(child)] = tuple(o)
key = tuple(o)
import numpy as np
while key:
    print(key[:3])
    print(key[3:6])
    print(key[6:9])
    print()
    key = _trace[key]