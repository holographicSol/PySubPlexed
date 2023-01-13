""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: PySubPlex.
"""
import os
import subprocess
from threading import Thread
import memory_reader

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
            o = dec(o)
            _o = o.split(' ')
            tag = _o[0]
            addr = _o[1]
            pid = _o[2]
            mem = memory_reader.memory_reader(pid, addr)
            fmem = memory_reader.find_mem(mem, 'FOOBAR_1', 'FOOBAR_2')
            co.append(str(tag) + ' ' + str(fmem))
            """ no need to keep reading because our evaluation is in memory and we have the address """
            break
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
    if tag is True:
        nr = []
        for d in r:
            d = str(*d)
            idx = d.find(' ')
            a = d[:idx]
            b = d[idx:]
            nr.append([a, b])
        r = nr
    elif tag is False:
        nr = []
        for d in r:
            d = str(*d)
            idx = d.find(' ')
            b = d[idx+1:]
            nr.append([b])
        r = nr
    return r


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
