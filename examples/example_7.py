""" Written by Benjamin Jack Cullen
Intention: Example program using PySubPlexed. Summary. Use potentially all CPU cores easily
with PySubPlexed in one line.
"""
import pysubplexed

print('Starting Program X: Using PySubPlexed to compute...')

print('Results:', len(pysubplexed.spawn(int(8), _data=['1024**100000', '1024**100000', '1024**100000', '1024**100000',
                                                       '1024**100000', '1024**100000', '1024**100000', '1024**100000'])))
