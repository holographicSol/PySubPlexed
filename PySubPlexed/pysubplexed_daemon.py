"""
Author: Written and designed by Benjamin Jack Cullen.
Module: PySubPlexed.
Intention: This program runs as n subprocess(s) to do work for a program.
Version: Unrestricted namespace access for eval(). Use with caution.
"""
import ast
import sys
import subprocess


def _eval(_tag, _invocation):
    try:
        ev = eval(_invocation)
        # Output for STDOUT reader (results --> PySubPlexed)
        print(str(_tag) + ' ' + str(ev))
    except Exception as e:
        # Output for STDOUT reader (errors --> PySubPlexed)
        print(str(_tag + ' ' + str(e)))


# Parse sys.argv for input arguments
tag = str(sys.argv[1])
allow_literals = str(sys.argv[2])

# No Literals (call eval once and exit).
if allow_literals == 'False':
    invocation = ''
    # Include everything after allow_literals as invocation.
    i = 0
    for _ in sys.argv:
        if i > 2:
            invocation = invocation + _
        i += 1
    _eval(tag, invocation)


# Literals (keep calling eval until literals are exhausted).
elif allow_literals == 'True':
    invocation = str(sys.argv[3])
    _literal = ''
    # Include everything after invocation as _literal.
    i = 0
    for _ in sys.argv:
        if i > 3:
            _literal = _literal + _
        i += 1
    _literal = ast.literal_eval(_literal)
    for _literals in _literal:
        _eval(tag, invocation)
