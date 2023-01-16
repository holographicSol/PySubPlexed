""" Written by Benjamin Jack Cullen
Intention: Testing."""
import time
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, allow_literals=False, _exec=True, tag=True, sort=True)


def UsingExec():
    """ PySubPlex exec()

    In this example lets PySubPlex functions (parallel functions) using exec() in the daemon(s).

    Setting _exec=True will force the daemon(s) to use exec(), while in contrast if _exec=False then the daemon(s)
    will use eval().

    """

    data = ['"[print(\'my excellent foobar\') for i in range(0, 3)]"',
            '"[print(\'my excellent foobar\') for i in range(0, 3)]"']

    """ Pre-chunk the data as usual """
    chunks = pysubplexed.chunk_data(data, 8)

    """ Feed the chunks into PySubPlexed one by one """
    print('Starting Program X: Using PySubPlexed to compute...')
    results = []
    t0 = time.perf_counter()
    for chunk in chunks:
        result = PySubPlexed(chunk)
        results.append(result)
    print('Time taken:', time.perf_counter() - t0)

    un_chunked_data = pysubplexed.unchunk_data(data=results, depth=1)
    for _ in un_chunked_data:
        print(_)


UsingExec()
