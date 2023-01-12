""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False)


def process_some_data(_data, _chunk_size):
    """ A concise version of example 5 """

    chunks = pysubplexed.chunk_data(_data, _chunk_size)
    _results = []
    _i_results = 0
    for chunk in chunks:
        result = PySubPlexed(chunk)
        _results.append(result)
        _i_results += int(len(result))
    return _results, _i_results


""" PySubPlex some imaginary data """
print('Starting Program X: Using PySubPlexed to compute...')
data = []
for i in range(1, 65):
    _str = '10**' + str(i)
    data.append(_str)
results, i_results = process_some_data(_data=data, _chunk_size=8)
print('Items in Results:', i_results)
