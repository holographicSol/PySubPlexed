""" Written by Benjamin Jack Cullen
Intention: Testing."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.

    Example return un-tagged results while still using internal tagging for order.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)


print('Starting Program X: Using PySubPlexed to compute...')

data = ['1+1', '2+1', '3+1', '4+1']
chunks = pysubplexed.chunk_data(data, 2)

""" Feed the chunks into PySubPlexed one by one """
results = []
i_results = 0
for chunk in chunks:
    result = PySubPlexed(chunk)
    results.append(result)
    i_results += int(len(result))

print('Items in results:', i_results)

""" The data can then be un-chunked if desired """
print(pysubplexed.unchunk_data(data=results))
