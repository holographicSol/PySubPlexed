""" Written by Benjamin Jack Cullen
Intention: Testing."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    Data Structure again. Observe data structure when passing many chunks
    to PySubPlexed.
    Observe I/O with small sample sizes when providing PySubPlexed with expressions
    and data combinations to test if your required expression and data will always
    provide the correct results and data structure.
    Sampling is even more important if your expression(s) are variable and or with
    truly variable data.
    You can say, okay I will always have these kinds of expression(s) so lets sample
    so many cycles and test with a program to ensure everything will always be correct
    using your particular expressions.
    """
    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=True, sort=True)


print('Starting Program X: Using PySubPlexed to compute...')

""" Create some data (n items of data in a list) """
data = []
for i in range(0, 2048):
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
