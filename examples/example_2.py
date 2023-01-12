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
datas = []
for i in range(0, 8):
    datas.append('1024**' + str(i))

chunks = [datas[x:x+4] for x in range(0, len(datas), 4)]
datas = []
for chunk in chunks:
    datas.append(chunk)

results = []
for data in datas:
    results.append(PySubPlexed(data))
print('Items in results:', sum(len(data) for result in results))
print('Results:', results)
