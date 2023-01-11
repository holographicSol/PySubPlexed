""" Written by Benjamin Jack Cullen
Intention: This program runs as n subprocess(s) to do work for a program.
           This subprocess should return values back to a program like a thread would but over ports.
Summary: Multiplex via ports.
"""
import sys
import time
import socket

retry_max = 10

""" Parse sys.argv for input arguments """
port = int(sys.argv[1])
port_1 = int(sys.argv[2])
buffer_size = int(sys.argv[3])


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


def _call_eval(_invocation):
    return eval_expression(_invocation)


def _send(_port, _port_1, _ev):
    """ Send reties n times if send should not succeed """
    global retry_max
    try:
        """ Send the result back to the main program (note: final operation is as client) """
        _s = socket.socket()
        _host = socket.gethostname()
        _s.connect((_host, _port_1))

        """ Tag result with port and send it home """
        _s.send(bytes(str(_port) + ' ' + str(_ev), encoding='utf-8'))
    except:
        if retry_max > int(0):
            retry_max -= int(1)
            time.sleep(1)
            _send(_port, _ev)


""" Startup layer protection against running arbitrarily """
if str(port).isdigit():
    if str(port_1).isdigit():
        if str(buffer_size).isdigit():

            """ Setup socket according to input arguments """
            s = socket.socket()
            host = socket.gethostname()
            s.bind((host, port))
            s.listen()

            """ Create a reusable I/O device in software that communicates over ports """
            c = None
            con_rcv = ''
            while con_rcv != 'terminate':
                con_rcv = ''
                if c is None:

                    """ Accept incoming connection """
                    c, addr = s.accept()
                else:
                    host_ip = s.getsockname()[0]

                    """ Allow receive if incoming addr[0] (IP) == socket.getsockname()[0] """
                    if host_ip == addr[0]:

                        """ Decode the incoming message """
                        invocation = bytes(c.recv(buffer_size)).decode('utf8')

                        """ Self destruct """
                        if invocation != '':
                            if invocation == 'terminate':
                                break

                            else:
                                """ Do some work, in this example eval() is used statically (test purposes only) CAUTION.
                                Restrict eval()s access to namespaces.
                                """
                                ev = ''
                                try:
                                    ev = _call_eval(invocation)
                                except Exception as e:
                                    ev = str(e)

                                _send(port, port_1, ev)
            s.close()
