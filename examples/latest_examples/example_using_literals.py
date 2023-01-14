import os
import time
import pysubplexed
import ast


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, allow_literals=True, tag=True, sort=True)


def LiteralsPySubPlexed():
    """ In this example pss a bag of literals in to PySubPlexed.
    """

    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]

    data = ['1024**_literals ' + str(x), '1024**_literals ' + str(y), '1024**_literals ' + str(z)]

    chunks = pysubplexed.chunk_data(data, 8)
    results = []
    t0 = time.perf_counter()
    for chunk in chunks:
        result = PySubPlexed(chunk)
        results.append(result)
    print('Results:', results)
    print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)


LiteralsPySubPlexed()

