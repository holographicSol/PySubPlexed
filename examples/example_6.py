""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False)


def process_some_data(data, chunk_size):
    """ A concise version of example 5 """

    chunks = pysubplexed.chunk_data(data, chunk_size)
    results = []
    i_results = 0
    for chunk in chunks:
        result = PySubPlexed(chunk)
        results.append(result)
        i_results += int(len(result))
    print('Items in results:', i_results)


""" PySubPlex some imaginary data """
print('Starting Program X: Using PySubPlexed to compute...')
data = []
for i in range(1, 65):
    _str = '10**' + str(i)
    data.append(_str)
process_some_data(data=data, chunk_size=8)
