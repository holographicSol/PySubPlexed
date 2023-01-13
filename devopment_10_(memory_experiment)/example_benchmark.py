import os
import time
import pysubplexed


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Experiment.
    """
    t0 = time.perf_counter()

    data = ['1024**100000', '1024**100000', '1024**100000', '1024**100000',
            '1024**100000', '1024**100000', '1024**100000', '1024**100000']
    PySubPlexed(data)
    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)


def BenchProceduralPy():
    t0 = time.perf_counter()
    results = []
    a = eval('1024**100000')
    results.append(a)
    b = eval('1024**100000')
    results.append(b)
    c = eval('1024**100000')
    results.append(c)
    d = eval('1024**100000')
    results.append(d)

    a = eval('1024**100000')
    results.append(a)
    b = eval('1024**100000')
    results.append(b)
    c = eval('1024**100000')
    results.append(c)
    d = eval('1024**100000')
    results.append(d)

    print('Time taken (Procedural Py):', time.perf_counter() - t0)


BenchPySubPlexed()
BenchProceduralPy()
