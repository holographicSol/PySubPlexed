import time
import pysubplexed


def PySubPlexed(_data):
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


def BenchPySubPlexed():
    """ Experiment.
    """

    data = ['1024**10000', '1024**10000', '1024**10000', '1024**10000',
            '1024**10000', '1024**10000', '1024**10000', '1024**10000']

    """ Chunk the data """
    chunks = pysubplexed.chunk_data(data, 8)

    """ Feed the chunks into PySubPlexed one by one """
    r = []
    for chunk in chunks:
        result = PySubPlexed(chunk)
        r.append(result)
        print(result)


def BenchProceduralPy():
    results = []
    a = eval('1024**10000')
    results.append(a)
    print(a)

    b = eval('1024**10000')
    results.append(b)
    print(b)

    c = eval('1024**10000')
    results.append(c)
    print(c)

    d = eval('1024**10000')
    results.append(d)
    print(d)

    e = eval('1024**10000')
    results.append(e)
    print(e)

    f = eval('1024**10000')
    results.append(f)
    print(f)

    g = eval('1024**10000')
    results.append(g)
    print(g)

    h = eval('1024**10000')
    results.append(h)
    print(h)


t0 = time.perf_counter()
BenchPySubPlexed()
t00 = time.perf_counter()
BenchProceduralPy()

print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)
print('Time taken (Procedural Py):', time.perf_counter() - t00)
