""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False)


print('Starting Program X: Using PySubPlexed to compute...')

""" This example demonstrates data structures and correct PySubPlexed usage """

""" Create some data (64 items of data in a list) """
data = []
for i in range(1, 65):
    _str = '10**' + str(i)
    data.append(_str)
print('Data Structure:  ', data)

""" Chunk the data """
chunks = pysubplexed.chunk_data(data, 8)
print('Chunks Data Structure:', chunks)

""" Feed the chunks into PySubPlexed one by one """
results = []
i_results = 0
for chunk in chunks:
    print('Processing Chunk:', chunk)
    result = PySubPlexed(chunk)
    results.append(result)
    i_results += int(len(result))
    print('Chunk Result:    ', result)

print('Items in results:', i_results)
