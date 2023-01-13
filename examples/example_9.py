""" Written by Benjamin Jack Cullen
Intention: Testing."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.

    In the two previous examples we turned off tagging and then even turned off sorting, however one must be
    certain that tagging is no longer required and also have no need to sort. Like simply using sum() or max() with
    results no matter the original order.

    In this example let's turn tagging and sorting back on and look at the results. Each chunk has daemon ID as
    index(zero) in the list. This is because one daemon could finnish before another and list alignment may be
    desired. PySubPlexed handles all of this when requested.

    Tags are reset each chunk for tag efficiency, otherwise a tag could theoretically keep growing across every chunk
    resulting in a huge tag. Undesirable as the tag in each chunk is already unique due to the chunk number
    containing the tag.

    In this example we will not un-chunk because tag=True.
    """

    return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=True, sort=True)


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
print(results)
