""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
Summary: PySubPlexed.
"""
import ast
import time
import sys
import subprocess

# print(sys.argv)

""" Parse sys.argv for input arguments """
tag = str(sys.argv[1])
invocation = str(sys.argv[2])

_literal = ''
i = 0
for _ in sys.argv:
    if i > 2:
        _literal = _literal + _
    i += 1
_literal = ast.literal_eval(_literal)

ev = ''
try:
    for _literals in _literal:
        ev = eval(invocation)
        print(str(tag) + ' ' + str(ev))
except Exception as e:
    ev = str(tag + ' ' + str(e))
    print(ev)
