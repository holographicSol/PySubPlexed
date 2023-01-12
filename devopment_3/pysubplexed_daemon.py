""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
Summary: PySubPlexed.
"""
import sys
import subprocess

""" Parse sys.argv for input arguments """
tag = str(sys.argv[1])
invocation = ''

i = 0
for _ in sys.argv:
    if i > 1:
        invocation = invocation + _
    i += 1
print(invocation, '')

ev = ''
try:
    ev = eval(invocation)
    print(str(tag) + ' ' + str(ev))
except Exception as e:
    ev = str(tag + ' ' + str(e))
