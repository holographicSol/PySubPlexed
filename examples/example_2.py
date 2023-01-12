""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed.
"""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.

    Same as example 1 but let's demonstrate how very little code we need
    to PySubPlex things.
    """

    return pysubplexed.spawn(int(len(_data)), _data)


print('Starting Program X: Using PySubPlexed to compute...')
data = []
for i in range(0, 64):
    data.append('1024**' + str(i))
chunks = [data[x:x+8] for x in range(0, len(data), 8)]
results = []
for chunk in chunks:
    results.append(PySubPlexed(chunk))
print('Items in results:', sum(len(chunk) for chunk in chunks))
