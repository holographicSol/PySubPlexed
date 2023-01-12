""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed.
"""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.

    Note: In this example, the number process(s) is specified by our
          list length which in this case is fine and is something to
          keep in mind when PySubPlexing.
          You may decide to loop through a list divided by say eight,
          like in this example. This depends on the capabilities of
          your CPU.
          For example: With a CPU with four cores with 8 threads a
                       program would greatly benefit from using 8
                       daemons, so chunks of eight to PySubPlexed
                       would be perfect.
    """

    return pysubplexed.spawn(int(len(_data)), _data)


print('Starting Program X: Using PySubPlexed to compute...')
data = ['10**100', '10**200', '10**300', '10**400',
        '10**400', '10**300', '10**200', '10**100']
results = PySubPlexed(data)
print('Items in results:', len(results))
