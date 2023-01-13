""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
Summary: PySubPlexed.
"""
import time
import sys
import subprocess

# t0 = time.perf_counter()
""" Parse sys.argv for input arguments """
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
# print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)
