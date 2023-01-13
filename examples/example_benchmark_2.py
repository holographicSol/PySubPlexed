import time
import pysubplexed


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Provide an insufficient workload to PySubPlexed and procedural Py should be faster. """

    data = ['1024**1000', '1024**1000', '1024**1000', '1024**1000']

    t0 = time.perf_counter()
    chunk = pysubplexed.chunk_data(data, 4)
    result = PySubPlexed(chunk)
    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)


def BenchProceduralPy():
    t0 = time.perf_counter()
    results = []
    x = eval('1024**1000')
    results.append(x)
    y = eval('1024**1000')
    results.append(y)
    z = eval('1024**1000')
    results.append(z)
    a = eval('1024**1000')
    results.append(a)
    print('Time taken (Procedural Py):', time.perf_counter() - t0)


BenchPySubPlexed()
BenchProceduralPy()
