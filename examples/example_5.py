""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False)


print('Starting Program X: Using PySubPlexed to compute...')

data = []
for i in range(1, 65):
    _str = '10**' + str(i)
    data.append(_str)
print('Data:  ', data)

chunks = pysubplexed.chunk_data(data, 2)
print('Chunks:', chunks)

print('')
results = []
i_results = 0
for chunk in chunks:
    print('processing chunk:', chunk)
    result = PySubPlexed(chunk)
    results.append(result)
    i_results += int(len(result))
    print('chunk result:    ', result)

print('Items in results:', i_results)
