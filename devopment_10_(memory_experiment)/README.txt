Written by Benjamin Jack Cullen.

In this iteration of PyPortPlexed, there is an experiment.

Optimization Experiment: Intead of reading stdout would it be faster to pull
results directly out of memory by handing an address back instead of results themselves.

Yes. However for many expressions it is still tough to beat single threaded
procedural performance.
