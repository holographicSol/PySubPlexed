""" Written by Benjamin Jack Cullen
Intention: This module (to be) distributes workloads to n spawned subprocesses and waits for values to be
           returned.
Summary: PySubPlex.
"""
import sys
import subprocess

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
    print(str(tag) + ' ' + str(ev))
except Exception as e:
    ev = str(tag + ' ' + str(e))
