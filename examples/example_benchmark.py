import time
import pysubplexed

evalutate_this = '1024**100000000'


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Provide a sufficient workload to PySubPlexed to make it worth it.
    Try adding more zero's to evaluate_this (one at a time).
    """
    data = [evalutate_this, evalutate_this, evalutate_this, evalutate_this]

    t0 = time.perf_counter()
    chunk = pysubplexed.chunk_data(data, 4)
    result = PySubPlexed(chunk)
    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)


def BenchProceduralPy():
    t0 = time.perf_counter()
    results = []
    x = eval(evalutate_this)
    results.append(x)
    y = eval(evalutate_this)
    results.append(y)
    z = eval(evalutate_this)
    results.append(z)
    a = eval(evalutate_this)
    results.append(a)
    print('Time taken (Procedural Py):', time.perf_counter() - t0)


BenchPySubPlexed()
BenchProceduralPy()
