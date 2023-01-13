""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: PySubPlex.
"""
import subprocess
from threading import Thread

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0
r = []
p = []


def dec(s):
    return str(s.decode("utf8").strip())


def results(n=str):
    global p, r
    co = []
    n = int(n)
    while True:
        o = p[n].stdout.readline()
        if o == '' and p[n].poll() is not None:
            break
        if o:
            co.append(dec(o))
        else:
            break
    if co:
        r.append(co)


def spawn(nt, _d, restrained=False, tag=True, sort=True):
    global p, r
    p = []
    r = []
    if restrained is False:
        d = 'python ./pysubplexed_daemon.py '
    elif restrained is True:
        d = 'python ./pysubplexed_daemon_restrained.py '
    com = []
    for n in range(0, nt):
        c = d + str(n) + ' ' + str(_d[n])
        com.append(c)
        x = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.append(x)
        t = Thread(target=results, args=str(n))
        t.start()
    while len(r) < nt:
        pass
    if sort is True:
        r = sorted(r, key=lambda x: x[0])
    z = []
    if tag is True:
        for x in r:
            a = str(*x)
            i = str(a).find(' ')
            b = str(a)[:i]
            c = str(a)[i+1:]
            z.append([b, c])
    else:
        for x in r:
            a = str(*x)
            i = str(a).find(' ')
            c = str(a)[i+1:]
            z.append(c)
    return z


def chunk_data(d, cs):
    ch = [d[x:x + cs] for x in range(0, len(d), cs)]
    d = []
    for c in ch:
        d.append(c)
    return d


def unchunk_data(data):
    nd = []
    for d in data:
        for x in d:
            nd.append(x)
    return nd
