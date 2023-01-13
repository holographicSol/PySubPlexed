""" Written by Benjamin Jack Cullen
Intention: Testing."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.

    In this example let's return sorted un-tagged data and then un-chunk for a clean one to one list alignment
    between expressions in and results out.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


print('Starting Program X: Using PySubPlexed to compute...')

data = ['1+1', '2+1', '3+1', '4+1']
chunks = pysubplexed.chunk_data(data, 2)

""" Feed the chunks into PySubPlexed one by one """
results = []
for chunk in chunks:
    result = PySubPlexed(chunk)
    results.append(result)

""" The data can then be un-chunked if desired """
print(pysubplexed.unchunk_data(data=results))
