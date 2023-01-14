""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
Summary: PySubPlexed.
"""
import sys
import ast


def eval_expression(input_string):
    """ Create a dictionary containing the names that you want to use with eval().
    May need further restricting. check: id, isinstance, iter """
    allowed_names = {"abs": abs,
                     "all": all,
                     "any": any,
                     "ascii": ascii,
                     "bin": bin,
                     "chr": chr,
                     "dir": dir,
                     "divmod": divmod,
                     "hash": hash,
                     "hex": hex,
                     "id": id,
                     "isinstance": isinstance,
                     "iter": iter,
                     "len": len,
                     "max": max,
                     "min": min,
                     "oct": oct,
                     "ord": ord,
                     "pow": pow,
                     "repr": repr,
                     "round": round,
                     "sorted": sorted,
                     "sum": sum
                     }
    # Compile the input string to bytecode using compile() in mode 'eval'.
    code = compile(input_string, "<string>", "eval")
    # Check .co_names on the bytecode object to make sure it contains only allowed names.
    for name in code.co_names:
        if name not in allowed_names.keys():
            # Raise a NameError if the user tries to enter a name that’s not allowed.
            raise NameError(f"Use of {name} not allowed")

    return eval(code, {"__builtins__": {}}, allowed_names)


def _call_eval(_tag, _invocation):
    try:
        ev = eval_expression(_invocation)
        # Output for STDOUT reader (results --> PySubPlexed)
        print(str(_tag) + ' ' + str(ev))
    except Exception as e:
        # Output for STDOUT reader (errors --> PySubPlexed)
        print(str(_tag + ' ' + str(e)))


""" Parse sys.argv for input arguments """
tag = str(sys.argv[1])
allow_literals = str(sys.argv[2])

# No Literals (call eval once and exit).
if allow_literals == 'False':
    invocation = ''
    i = 0
    for _ in sys.argv:
        if i > 2:
            invocation = invocation + _
        i += 1
    _call_eval(tag, invocation)
