""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: PySubPlex.
"""
import os
import sys
import subprocess
import time

pid = os.getpid()
tag = str(sys.argv[1])
invocation = ''
i = 0
for _ in sys.argv:
    if i > 1:
        invocation = invocation + _
    i += 1

ev = ''
try:
    ev = eval(invocation)
    ev = 'FOOBAR_1' + str(ev) + 'FOOBAR_2'
    address = id(ev)
    print(str(tag) + ' ' + str(hex(address)) + ' ' + str(pid))
except Exception as e:
    ev = str(tag + ' ' + str(e))
time.sleep(2)
