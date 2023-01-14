import os
import time
import pysubplexed
import ast


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Performance upgrade. PySubPlexed daemons can now accept literals. This makes the newer versions
    of PySubPlexed extremely faster than previous versions for pure math like expressions (but still not
    faster than procedural py for pure math expressions because of stdout time).

    Running this benchmark and the example_benchmark.py in example_development_8 should illustrate the performance
    increase in the latest developments of PySubPlexed.

    Create some data: ( (1024 ** 1000) * 500) * 8 ) = 4000 operations of 1024^1000.
    """
    x = []
    for i in range(0, 500):
        x.append(1000)
    x = str(x)
    data = ['1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x,
            '1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x]
    chunks = pysubplexed.chunk_data(data, 8)
    results = []
    t0 = time.perf_counter()
    for chunk in chunks:
        result = PySubPlexed(chunk)
        results.append(result)
    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)


def BenchProceduralPy():
    """ Create some data: ( (1024 ** 1000) * 500) * 8 ) = 4000 operations of 1024^1000.
    """
    x = []
    for i in range(0, 500):
        x.append(1000)
    x = str(x)
    t0 = time.perf_counter()
    results = []
    for i in range(0, 8):
        _literal = ast.literal_eval(x)
        invocation = '1024**_literals'
        for _literals in _literal:
            result = eval(invocation)
            results.append(result)
    print('Time taken (Procedural Py):', time.perf_counter() - t0)


BenchPySubPlexed()
BenchProceduralPy()

""" This updated version of PySubPlexed:"""

""" BenchPySubPlexed took me 2.3543013999878895 seconds on my machine """
""" BenchProceduralPy took me 0.13421519999974407 seconds on my machine """

""" For pure math like expressions PySubPlexed is not as fast as BenchProceduralPy and
    that is because of stdout time. While PySubPlexing other infinite kinds of expressions
    can be much faster than BenchProceduralPy. """
