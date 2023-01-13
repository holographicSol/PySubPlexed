""" Written by Benjamin Jack Cullen
Intention: Testing."""
import time

import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


print('Starting Program X: Using PySubPlexed to compute...')

""" TESTING """

""" Create some data (n items of data in a list) """
data = ['1024**1', '1024**1', '1024**1', '1024**1',
        '1024**1', '1024**1', '1024**1', '1024**1']
print('Data Structure:  ', data)

""" Chunk the data """
chunks = pysubplexed.chunk_data(data, 8)
print('Chunks Data Structure:', chunks)

""" Feed the chunks into PySubPlexed one by one """
results = []
i_results = 0
t0 = time.perf_counter()
for chunk in chunks:
    print('Processing Chunk:', chunk)
    result = PySubPlexed(chunk)
    results.append(result)
    i_results += int(len(result))
    print('Chunk Result:    ', result)

print('Items in results:', i_results)
print('Time taken:', time.perf_counter() - t0)
print(pysubplexed.unchunk_data(data=results))
