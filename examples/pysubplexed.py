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


def spawn(n_thread, _data, restrained=False):
    """ Starts n process(s) each with their ID and then spawns n threads to wait for the results come back in. """

    global procs, res
    res = []

    if restrained is False:
        PySubPlexCommand = 'python ./pysubplexed_daemon.py '
    elif restrained is True:
        PySubPlexCommand = 'python ./pysubplexed_daemon_restrained.py '

    """ Spawn and instruct daemons """
    commands = []
    for n in range(0, n_thread):
        cmd = PySubPlexCommand + str(n) + ' ' + str(_data[n])
        commands.append(cmd)
    procs = [subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) for i in commands]

    """ Spawn threads and wait for results """
    for n in range(0, n_thread):
        thread = Thread(target=results, args=str(n))
        thread.start()
    while len(res) < n_thread:
        pass

    """ Sort the results by IDs and return (getting updated, return res as it is) """
    multiplexed_results = res
    multiplexed_results = sorted(multiplexed_results, key=lambda x: x[0])

    return multiplexed_results


def chunk_data(data, chunk_size):
    """ Break up lists into chunks of n and return as a single list of specified chunks """

    chunks = [data[x:x + chunk_size] for x in range(0, len(data), chunk_size)]

    data = []
    for chunk in chunks:
        data.append(chunk)

    return data
