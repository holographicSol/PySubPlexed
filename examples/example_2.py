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

data = ['10*1', '10*2', '10*3', '10*4',
        '10*5', '10*6', '10*7', '10*8']

""" PySubPlexed can chunk data for you """
chunks = pysubplexed.chunk_data(data, 4)

""" Now we have two chunks of data we can pass one at a time into PySubPlexed daemon.
Four items is the chunk size and we have eight items in data so this will mean two calls
to PySubPlexed each call spawning 4 processes to run simultaniously.
"""
print('Chunks:', chunks)

""" Lets pass each chunk into PySubPlexed """
results = []
for chunk in chunks:
    results.append(PySubPlexed(chunk))
print('Results:', results)
print('Items in results:', sum(len(chunk) for result in results))
