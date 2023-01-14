""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: PySubPlex.
"""
import subprocess
from threading import Thread

""" Setup subprocess startupinfo argument to be daemonic """
info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

res = []
procs = []


def results(n=str):
    """ Wait on n threads for results to come back in from real processes. """

    global procs, res
    cmd_output = []
    n = int(n)
    while True:
        output = procs[n].stdout.readline()
        if output == '' and procs[n].poll() is not None:
            break
        if output:
            cmd_output.append(str(output.decode("utf-8").strip()))
        else:
            break
    rc = procs[n].poll()
    if cmd_output:
        res.append(cmd_output)


def spawn(n_thread, _data, restrained=False, allow_literals=False, tag=True, sort=True):
    """ Starts n process(s) each with their ID and then spawns n threads to wait for the results come back in.
    N_Thread: Number of daemons to run simultaniously.

    Data: A Chunk of data expressions.

    Retrained: Choose your daemon. The restrained daemon should have very limited namespace access.

    Allow Literals: Changes the perceived order of STDIN for the daemon, allowing literals to be passed in too along
    with the invocation which should be passed anyway.
    Allow_literals=False : _data = ['1024*1', '1024*2', '1024*3', '1024*4']
    Allow_literals=True : _data = ['1024*_literals '+ x, '1024*_literals '+ y, '1024*_literals ' + z] where x, y, z
    are type str of list(s) example x = str([100, 200, 300]). STDIN limitations may pertain to argument length in this
    case.

    Tag: Keeps results tagged on the way out of PySubPlexed.

    Sort: Useful because one daemon could finnish before another. Intends to structure results in accordance with
    structure of expressions in.
    """

    global procs, res
    procs = []
    res = []

    """ Use specified daemon """
    PySubPlexCommand = ''
    if restrained is False:
        PySubPlexCommand = 'python ./pysubplexed_daemon.py '
    elif restrained is True:
        PySubPlexCommand = 'python ./pysubplexed_daemon_restrained.py '

    """ Spawn and instruct daemons """
    commands = []
    for n in range(0, n_thread):
        cmd = PySubPlexCommand + str(n) + ' ' + str(allow_literals) + ' ' + str(_data[n])
        commands.append(cmd)
    procs = [subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) for i in commands]

    """ Spawn threads and wait for results back from daemons """
    for n in range(0, n_thread):
        thread = Thread(target=results, args=str(n))
        thread.start()
    while len(res) < n_thread:
        pass

    """ Sort the results by tags """
    if sort is True:
        res = sorted(res, key=lambda x: x[0])

    """ Data structure return tagged/un-tagged results """
    multiplexed_results = []
    if tag is True:
        for r in res:
            for rs in r:
                a = str(rs)
                idx = str(a).find(' ')
                b = str(a)[:idx]
                c = str(a)[idx+1:]
                multiplexed_results.append([b, c])
    else:
        for r in res:
            for rs in r:
                a = str(rs)
                idx = str(a).find(' ')
                c = str(a)[idx+1:]
                multiplexed_results.append(c)

    return multiplexed_results


def chunk_data(data, chunk_size):
    """ Break up lists into chunks of n and return as a single list of specified chunks """

    chunks = [data[x:x + chunk_size] for x in range(0, len(data), chunk_size)]

    data = []
    for chunk in chunks:
        data.append(chunk)

    return data


def unchunk_data(data):
    """ Un-chunk the data when and if required. Requires tag=False during spawn(). """

    new_data = []
    for dat in data:
        for x in dat:
            new_data.append(x)
    return new_data
