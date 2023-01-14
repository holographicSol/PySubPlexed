Module Name: PySubPlexed.

Author: Written by Benjamin Jack Cullen.

Intention: Run multiple subprocesses simultaniously, all with handling and all slam-dunking results back into one
variable, all in one line, keeping any given program that imports PySubPlexed clean.

Summary: Use potentially all CPU cores easily with PySubPlexed in one line to get things done faster.

Description: A less powerful version of my PyPortPlexed module, but faster and designed for running on a single machine.


Things to remember:

    1. Setting daemon count can be dangerous so stay within the logical limits of your hardware.
       4 Cores, <=8 threads = Set a max of 8 for n_thread (like below).
    2. Restrain the daemons. Use only the daemon you need by setting restrained=True/False accordingly.
    3. Consider eval() when passing lists/chunks of data to PySubPlexed because eval() is extremely powerful.
    4. PySubPlexed may not always be faster depending on the application of PySubPlexed. Apply appropriately.


Simple Example:

    import pysubplexed

    print('Starting Program X: Using PySubPlexed to compute...')

    print('Results:', len(pysubplexed.spawn(int(8), _data=['1024**1', '1024**2', '1024**3', '1024**4',
                                                           '1024**5', '1024**6', '1024**7', '1024**8'],
                                            allow_literals=False)))


Chunks Example:

    import pysubplexed

    def PySubPlexed(_data):
        return pysubplexed.spawn(int(len(_data)), _data, allow_literals=False)


    print('Starting Program X: Using PySubPlexed to compute...')
    
    data = ['10*1', '10*2', '10*3', '10*4',
            '10*5', '10*6', '10*7', '10*8']
    
    """ PySubPlexed can turn a list into chunks of sub-lists for you """
    chunks = pysubplexed.chunk_data(data, 4)
    
    """ Now we have two chunks of data we can pass one at a time into PySubPlexed daemon.
    Four items is the chunk size and we have eight items in data so this will mean two calls
    to PySubPlexed each call spawning 4 processes to run simultaniously.
    """
    print('Chunks:', chunks)
    
    """ Lets pass each chunk into PySubPlexed """
    results = []
    for chunk in chunks:
        results.append(PySubPlexed(chunk))
    print('Results:', pysubplexed.unchunk_data(data=results, depth=1))
    print('Items in results:', sum(len(chunk) for result in results))


Let's try something different, 2 default pings in half the time. This kind of thing is what PySubPlexed is great at.

In this case 8 is the number of daemons that can run at a time and our chunk is a length of two (two commands).
So this will spawn 2 daemons and ping in the time of one, with all the handling taken care of and all
results slam-dunked back into a single variable and ready to use:

    import pysubplexed
    
    
    def PySubPlexed(_data):
        return pysubplexed.spawn(8, _data=_data, allow_literals=False)
    

    results = PySubPlexed(['"subprocess.getoutput(\'powershell ping 8.8.8.8\')"',
                           '"subprocess.getoutput(\'powershell ping 9.9.9.9\')"'])
    print('Results:', results)


Data Structures. Create some imaginary data, chunk the data and then feed each chunk into PySubPlexed.
This example demonstrates how one could perform some expression sampling and ensure everything will go as hypothesized
when leveraging PySubPlexed:

    import pysubplexed
    
    
    def PySubPlexed(_data):
        """ Provide something for PySubPlexed to compute... In one line.
        """
    
        return pysubplexed.spawn(int(len(_data)), _data, allow_literals=False)
    
    
    print('Starting Program X: Using PySubPlexed to compute...')
    
    """ This example demonstrates data structures and correct PySubPlexed usage """
    
    """ Create some data (1024 items of data in a list) """
    data = []
    for i in range(1, 1024):
        _str = '10*' + str(i)
        data.append(_str)
    print('Data Structure:  ', data)
    
    """ Chunk the data """
    chunks = pysubplexed.chunk_data(data, 4)
    print('Chunks Data Structure:', chunks)
    
    """ Feed the chunks into PySubPlexed one by one and familiarize with the data structures """
    results = []
    i_results = 0
    for chunk in chunks:
        print('Processing Chunk:', chunk)
        result = PySubPlexed(chunk)
        results.append(result)
        i_results += int(len(result))
        print('Chunk Result:    ', result)
    
    print('Items in results:', i_results)


Tagging. Tagging occurs internally in case one daemon finishes before another and enables PySubPlexed to keep
everything in order the same way as everything came in:

    import pysubplexed


    def PySubPlexed(_data):
        return pysubplexed.spawn(int(len(_data)), _data, tag=True, sort=True)
    
    
    print(PySubPlexed(['1024**1', '1024**2', '1024**3', '1024**4']))


Disabling Tagging. Tags can be optionally removed on the way out of PySubPlexed and will still be used internally
to maintain results order. This means untagged data can be returned while order being maintained:

    import pysubplexed
    
    
    def PySubPlexed(_data):
        return pysubplexed.spawn(int(len(_data)), _data, tag=False, sort=True)
    
    
    print(PySubPlexed(['1024**1', '1024**2', '1024**3', '1024**4']))


Sorting. Sorting also occurs for results on the way out of PySubPlexed and is optional.

    import pysubplexed
    
    
    def PySubPlexed(_data):
        return pysubplexed.spawn(int(len(_data)), _data, tag=False, sort=False)
    
    
    print(PySubPlexed(['1024**1', '1024**2', '1024**3', '1024**4']))


UnChunking. One to one data structures with expressions in and results out may be desirable.
UnChunking with a specified depth allows PySubPlexed to return provide one to one list alignment between expressions
in and results out.

The UnChunking depth can be increased/decreased as needed for a one to one, if indeed a one to one is required at all:

    import pysubplexed
    
    
    def PySubPlexed(_data):
        """ Provide something for PySubPlexed to compute... In one line.
    
        In this example let's return sorted un-tagged data and then un-chunk for a clean one to one list alignment
        between expressions in and results out.
        """
    
        return pysubplexed.spawn(int(len(_data)), _data, restrained=False, tag=False, sort=True)
    
    
    print('Starting Program X: Using PySubPlexed to compute...')
    
    data = ['1+1', '2+1', '3+1', '4+1']
    chunks = pysubplexed.chunk_data(data, 2)
    
    """ Feed the chunks into PySubPlexed one by one """
    results = []
    for chunk in chunks:
        result = PySubPlexed(chunk)
        results.append(result)
    
    """ The data can then be un-chunked if desired """
    print(pysubplexed.unchunk_data(data=results, depth=1))

Literals. Literals can be passed through PySubPlexed, this can make many things even faster because the daemons can
keep evaluating instead of restarting for each new evaluation:

    import pysubplexed
    
    
    def PySubPlexed(_data):
        return pysubplexed.spawn(int(len(_data)), _data, restrained=False, allow_literals=True, tag=True, sort=True)
    
    
    def LiteralsPySubPlexed():
        """ In this example pss a bag of literals in to PySubPlexed.
        """
    
        x = [1, 2, 3]
        y = [4, 5, 6]
        z = [7, 8, 9]
    
        data = ['1024**_literals ' + str(x), '1024**_literals ' + str(y), '1024**_literals ' + str(z)]
    
        chunks = pysubplexed.chunk_data(data, 8)
        results = []
        t0 = time.perf_counter()
        for chunk in chunks:
            result = PySubPlexed(chunk)
            results.append(result)
        print('Results:', results)
        print('Time taken (PySubPlexed):  ', time.perf_counter() - t0)
    
    
    LiteralsPySubPlexed()


Using the restrained daemon. There are two daemons, one with unrestricted access to namespace and the other has
tried to be contained which should have restricted/limited access to namespaces. Make no assumptions, this is the
intention. Here is an example of using the restricted daemon:

    import pysubplexed
    pysubplexed.spawn(4, sum[1,2,3], restrained=True)


Notes:

PySubPlexed makes many things faster in one line while keeping a program clean that imports PySubPlexed however pure
math operations is not what PySubPlexed is great at despite efforts. Proper application of PySubPlexed can and will
yield infinitely faster results in one line.
