"""
Author: Written and designed by Benjamin Jack Cullen.
Module: PySubPlexed.
Intention: This module distributes workloads to real processes and then waits on threads for results from the processes.
"""
import subprocess
from threading import Thread

""" Setup subprocess startupinfo argument to be daemonic (background process, no window) """
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


def spawn(n_thread, _data, restrained=False, allow_literals=False, _exec=False, tag=True, sort=True):
    """ Starts n process(s) each with their ID and then spawns n threads to wait for the results to come back in.
    N_Thread: Number of daemons to run simultaniously. int()

    Data: A Chunk of data expressions. list[]

    Restrained: Choose your daemon. The restrained daemon should have very limited namespace access (security). bool()

    Allow Literals: Changes the perceived order of STDIN for the daemon, allowing literals to be passed in too along
    with the invocation which should be passed anyway. bool()

    Allow_literals = False : _data = ['1024*1', '1024*2', '1024*3', '1024*4']
    Allow_literals = True : _data = ['1024*_literals '+ x, '1024*_literals '+ y, '1024*_literals ' + z] where x, y, z
    are type str() of list(s), for example: x = str([100, 200, 300]).

    Exec: True : Calls exec().
    Exec: False : Calls eval().

    Tag: Keeps results tagged on the way out of PySubPlexed. bool()

    Sort: Useful because one daemon could finnish before another. Intends to structure results in accordance with
    structure of expressions in. Tags can be disabled on the way out of PySubPlexed and will still be used internally
    for this reason, order.
    """

    global procs, res
    procs = []
    res = []

    """ Use specified daemon (restricted/unrestricted) """
    PySubPlexCommand = ''
    if restrained is False:
        PySubPlexCommand = 'python ./pysubplexed_daemon.py '
    elif restrained is True:
        PySubPlexCommand = 'python ./pysubplexed_daemon_restrained.py '

    """ Spawn and instruct the daemons """
    commands = []
    for n in range(0, n_thread):
        cmd = PySubPlexCommand + str(n) + ' ' + str(allow_literals) + ' ' + str(_exec) + ' ' + str(_data[n])
        commands.append(cmd)
    procs = [subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) for i in commands]

    """ Spawn threads to wait for results back from daemons (thread per daemon) """
    for n in range(0, n_thread):
        thread = Thread(target=results, args=str(n))
        thread.start()
    while len(res) < n_thread:
        pass

    """ Sort the results by tags """
    if sort is True:
        res = sorted(res, key=lambda x: x[0])

    """ Data structure. Make tagged/un-tagged results """
    if _exec is False:
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
    elif _exec is True:
        multiplexed_results = res

    return multiplexed_results


def chunk_data(data, chunk_size):
    """ Return as a single list of lists with each sublist length pertaining to chunk_size.
    Data structuring.
    data : list[]
    chunk_size : int()
    """

    chunks = [data[x:x + chunk_size] for x in range(0, len(data), chunk_size)]

    data = []
    for chunk in chunks:
        data.append(chunk)

    return data


def unchunk_data(data, depth=1):
    """ Un-chunk the data when and if required.
    Data : list/list(s) of list(s). list[].
    Depth : Iterations / Cycles. int.
    """

    new_data = data
    for i in range(0, depth):
        new_sub_data = []
        for dat in new_data:
            for x in dat:
                new_sub_data.append(x)
        new_data = new_sub_data
    return new_data
