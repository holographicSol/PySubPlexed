""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed.
"""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line. """

    return pysubplexed.spawn(int(len(_data)), _data)


print('Starting Program X: Using PySubPlexed to compute...')
data = ['10**1', '10**2', '10**3', '10**4']
results = PySubPlexed(data)
print(results)
