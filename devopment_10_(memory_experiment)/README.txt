Written by Benjamin Jack Cullen.

Optimization Experiment.

Hypothesis:
	Intead of reading stdout would it be faster to pull results directly out of memory
	by handing an address back from the daemon instead of the results?

Answer:
	Yes. However for many expressions it is still tough to beat procedural performance
	in python in this way.

Conclusion:
	PySubPlex some things, and not others for best performance.