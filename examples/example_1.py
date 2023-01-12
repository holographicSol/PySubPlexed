""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed.
"""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.

    This time for looping through a larger data set.
    """

    return pysubplexed.spawn(int(len(_data)), _data)


print('Starting Program X: Using PySubPlexed to compute...')

""" First lets create some variable imaginary data """
data = []
for i in range(0, 64):
    data.append('1024**' + str(i))

""" It is important to break the data up into chunks that can be managed
 by the CPU. Chunks of eight items means eight processes simultaniously which
 is perfect for my CPU in this example.
 """
chunks = [data[x:x+8] for x in range(0, len(data), 8)]

""" Now we have prepared our data for looping through PySubPlexed, we can
 start PySubPlexing.
 """
results = []
for chunk in chunks:
    results.append(PySubPlexed(chunk))
print('Items in results:', sum(len(chunk) for chunk in chunks))
