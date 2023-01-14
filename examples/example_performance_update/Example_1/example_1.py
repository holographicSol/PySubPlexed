import time
import pysubplexed


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Compare this benchmark to example_1.py in example_performance_update Example 2. PySubPlexed
    should be slower here. And BenchProceduralPy should win for this expression type.

    Create some data: ( (1024 ** 1000) * 500) * 8 ) = 4000 operations of 1024^1000.
    """
    data = []
    for i in range(0, 500):
        data.append('1024**1000')
    chunks = pysubplexed.chunk_data(data, 8)
    t0 = time.perf_counter()
    r = []
    for chunk in chunks:
        r.append(PySubPlexed(chunk))
    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)


def BenchProceduralPy():
    """ Create some data: ( (1024 ** 1000) * 500) * 8 ) = 4000 operations of 1024^1000.
    """
    t0 = time.perf_counter()
    data = []
    for i in range(0, 500):
        data.append('1024**1000')
    results = []
    for datas in data:
        result = eval(datas)
        results.append(result)
    print('Time taken (Procedural Py):', time.perf_counter() - t0)


BenchPySubPlexed()
BenchProceduralPy()

""" This old version of PySubPlexed:"""

""" BenchPySubPlexed took me 14.891633699997328 seconds on my machine """
""" BenchProceduralPy took me 0.01701560000947211 seconds on my machine """

""" For pure math like expressions PySubPlexed is not as fast as BenchProceduralPy and
    that is because of stdout time. While PySubPlexing other infinite kinds of expressions
    can be much faster than BenchProceduralPy. """
