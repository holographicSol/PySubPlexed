""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
Summary: PySubPlexed.
"""
import ast
import sys
import subprocess

""" Parse sys.argv for input arguments """
tag = str(sys.argv[1])
allow_literals = str(sys.argv[2])
invocation = str(sys.argv[3])


def _eval(_tag, _invocation):
    try:
        ev = eval(_invocation)
        # Output for STDOUT reader (results --> PySubPlexed)
        print(str(_tag) + ' ' + str(ev))
    except Exception as e:
        # Output for STDOUT reader (errors --> PySubPlexed)
        print(str(_tag + ' ' + str(e)))


# No Literals (call eval once and exit).
if allow_literals == 'False':
    invocation = ''
    i = 0
    for _ in sys.argv:
        if i > 1:
            invocation = invocation + _
        i += 1
    _eval(tag, invocation)


# Literals (keep calling eval until literals are exhausted).
elif allow_literals == 'True':
    _literal = ''
    i = 0
    for _ in sys.argv:
        if i > 3:
            _literal = _literal + _
        i += 1
    _literal = ast.literal_eval(_literal)
    for _literals in _literal:
        _eval(tag, invocation)
