""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed.
Summary: Use potentially all CPU cores easily with PySubPlexed in one line.

Things to remember:
    1. Setting Daemon Count can be dangerous so stay within the logical limits of your hardware.
       4 Cores, 8 threads = Set a max of 8 for n_thread (like below).
    2. Restrain the daemons. Use only the daemon you need by setting restrained=True/False accordingly.
    3. Consider eval() when passing lists/chunks of data to PyPortPlexed because eval() is extremely powerful.

"""
import pysubplexed

print('Starting Program X: Using PySubPlexed to compute...')

print('Results:', len(pysubplexed.spawn(int(8), _data=['1024**100000', '1024**100000', '1024**100000', '1024**100000',
                                                       '1024**100000', '1024**100000', '1024**100000', '1024**100000'])))
