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


def spawn(n_thread, _data, restrained=False, tag=True):
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
    res = sorted(res, key=lambda x: x[0])

    """ Data structure
    List alignment and data structure.
    Results should unless where tagging is removed always be a list
    of lists. One list of lists. Never a list of lists inside a list
    for example. One list of lists.
    Alignment. Results indexes should always be a one to one alignment
    with expressions in. Regardless of sub-listing (used when tagging) where
    the one to one alignment is one to one within a sub index.
    
    Tag=True: Useful to determine if your expression(s) list items will
    always result in a one to one with results list. List alignment between
    expression list and results list.
    
    Tag=False: Useful for a one to one expressions list with results list
    without having to sub-index the results (no tags).
    
    Tag bool should be considered carefully. While tag=False assumes developer
    is comfortable the data/expressions in will always align with the results
    list by a one to one index.
    
    This module does a lot that can be avoided from being put in every program
    but it cannot keep foo out of your expressions and data.
    
    Use tagging unless tagging is not required. If there is foo in your data
    of foo in your expressions, variable or not, tagging can help you see
    where in any given chunk the foo occurred and therefore what and how many
    items in any given chunk are not aligned with the input expressions/data
    list.
    
    If tag=False internal tagging will still occur internally for 
    expression/result list alignment because one daemon could finnish before
    any other given daemon in any given chunk. And list alignment is often 
    important.
    Tag=False does not disable internal tagging, only results in a results list
    that does not contain tags. For a one to one expressions list with results
    list without sub indexing the results list.
    
    Tagging may be completely disabled optionally in the future. Where certain
    operations do not require list alignments.
    """
    multiplexed_results = []
    if tag is True:
        for r in res:
            a = str(*r)
            idx = str(a).find(' ')
            b = str(a)[:idx]
            c = str(a)[idx:]
            multiplexed_results.append([b, c])
    else:
        for r in res:
            a = str(*r)
            idx = str(a).find(' ')
            c = str(a)[idx:]
            multiplexed_results.append(c)

    return multiplexed_results


def chunk_data(data, chunk_size):
    """ Break up lists into chunks of n and return as a single list of specified chunks """

    chunks = [data[x:x + chunk_size] for x in range(0, len(data), chunk_size)]

    data = []
    for chunk in chunks:
        data.append(chunk)

    return data
