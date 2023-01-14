import os
import time
import pysubplexed
import ast


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Experiment.
    """

    """ Create some data (n items of data in a list)
    ( (1024 ** 10,000) * 10) * 8 ).
    """
    x = []
    for i in range(0, 1000):
        x.append(1000)
    x = str(x)
    data = ['1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x,
            '1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x, '1024**_literals ' + x]

    chunks = pysubplexed.chunk_data(data, 8)
    results = []
    i_results = 0
    t0 = time.perf_counter()
    for chunk in chunks:
        result = PySubPlexed(chunk)
        results.append(result)
        i_results += 1

    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)
    print('Items in results:', i_results)


def BenchProceduralPy():
    x = []
    for i in range(0, 1000):
        x.append(1000)
    x = str(x)

    t0 = time.perf_counter()
    results = []
    i_results = 0

    for i in range(0, 8):
        _literal = ast.literal_eval(x)
        invocation = '1024**_literals'
        for _literals in _literal:
            result = eval(invocation)
            results.append(result)
            i_results += 1

    print('Time taken (Procedural Py):', time.perf_counter() - t0)
    print('Items in results:', i_results)


BenchPySubPlexed()
BenchProceduralPy()
