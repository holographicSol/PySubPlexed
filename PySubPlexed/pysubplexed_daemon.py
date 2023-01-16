"""
Author: Written and designed by Benjamin Jack Cullen.
Module: PySubPlexed.
Intention: This program runs as n subprocess(s) to do work as a real process for PySubPlexed.
Version: Unrestricted namespace access for eval() and exec() Use with caution.
"""
import ast
import sys
import subprocess


def _eval(_exec, _tag, _invocation):
    try:
        # uncomment to view
        # print('_invocation:', _invocation)
        if _exec == 'False':
            # call eval
            ev = eval(_invocation)
            print(str(_tag) + ' ' + str(ev))

        elif _exec == 'True':
            # call exec
            _invocation = compile(_invocation, 'x', 'exec')
            print(str(_tag))
            exec(_invocation)

        # Output for STDOUT reader (results --> PySubPlexed)
    except Exception as e:
        # Output for STDOUT reader (errors --> PySubPlexed)
        print(str(_tag + ' ' + str(e)))


# Parse sys.argv for input arguments
tag = str(sys.argv[1])
allow_literals = str(sys.argv[2])
_exec = str(sys.argv[3])

# uncomment to view
# print('tag:', tag)
# print('allow_literals:', allow_literals)
# print('_exec:', _exec)
# print('sys.argv:', sys.argv)

# No Literals (call eval once and exit).
if allow_literals == 'False':
    invocation = ''
    # Include everything after allow_literals as invocation.
    i = 0
    for _ in sys.argv:
        if i > 3:
            invocation = invocation + _
        i += 1
    _eval(_exec, tag, invocation)


# Literals (keep calling eval until literals are exhausted).
elif allow_literals == 'True':
    invocation = str(sys.argv[4])
    _literal = ''
    # Include everything after invocation as _literal.
    i = 0
    for _ in sys.argv:
        if i > 4:
            _literal = _literal + _
        i += 1
    _literal = ast.literal_eval(_literal)
    for _literals in _literal:
        _eval(_exec, tag, invocation)
