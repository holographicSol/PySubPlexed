""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed.
"""
import time
import pysubplexed
from threading import Thread


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute and then destroy the daemons """

    n_threads = int(len(_data))
    print(pysubplexed.spawn(n_threads, _data))


data = ['10**10000', '10**10000', '10**10000', '10**10000']
PySubPlexed(data)
