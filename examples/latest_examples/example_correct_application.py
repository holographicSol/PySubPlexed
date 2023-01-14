""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed."""
import pysubplexed


def PySubPlexed(_data):

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, allow_literals=False, tag=False, sort=True)


def UsingPySubPlexed():
    """ Having covered all previous examples, you should notice that PySubPlexed is extremely beneficial for some
    things and not others in python.

    PySubPlexed is perfect for spawning n subprocesses for example, handling them, sorting results, and keeping all
    the results in order when results come back in from the daemons. All in one line inside a program that leverages
    PySubPlexed in this way.

    PySubPlexed is not great or the best thing to use for normal math expressions for example, at least not yet. Such
    expressions could be performed faster in other ways.

    Example application of PysubPlexed module:
    For example 2 default pings in half the time or 8 in the time of 1, or 32 in the time of 3 which is massive time
    savings and handling for one line. This is how one should think about applying PySubPlexed, because all the
    handling is done and in one line everything comes back into one variable in order and tagged if specified.
    And the ping example could be anything sub-processed that is faster in parallel. Its just one example.

    """

    data = ['"subprocess.getoutput(\'powershell ping 8.8.8.8\')"',
            '"subprocess.getoutput(\'powershell ping 9.9.9.9\')"']

    chunks = pysubplexed.chunk_data(data, 4)
    results = []
    for chunk in chunks:
        results.append(PySubPlexed(chunk))
    print(results)


UsingPySubPlexed()
