""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed."""
import pysubplexed


def PySubPlexed(_data):
    """ Provide something for PySubPlexed to compute... In one line.
    """

    return pysubplexed.spawn(int(len(_data)), _data)


print('Starting Program X: Using PySubPlexed to compute...')

""" In this example let's PyPortPlexed something different """
data = []
for i in range(0, 1):
    _str = '"subprocess.getoutput(\'powershell notepad\')"'
    data.append(_str)

chunks = pysubplexed.chunk_data(data, 4)
results = []
for chunk in chunks:
    results.append(PySubPlexed(chunk))
print('Items in results:', sum(len(chunk) for result in results))
print(results[0])
