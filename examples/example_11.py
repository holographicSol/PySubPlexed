""" Written by Benjamin Jack Cullen
Intention: Testing."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    Data Structure again. Observe data structure when passing many chunks
    to PySubPlexed.
    """
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=True, sort=True)


print('Starting Program X: Using PySubPlexed to compute...')

""" Create some data (n items of data in a list) """
data = []
for i in range(0, 1024):
    _str = str(i) + '+1'
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
print('Results:')
print(results)
print('Items in results:', i_results)
