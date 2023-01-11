""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
Summary: PySubPlexed.
"""
import sys
import subprocess

retry_max = 10

""" Parse sys.argv for input arguments """
tag = str(sys.argv[1])
invocation = str(sys.argv[2])

ev = ''
try:
    ev = eval(invocation)
    print(tag, ev)
except Exception as e:
    ev = str(tag, e)
