import time 

class Timer(object):
    """
    Performance debugging class. Usage:
       with Timer(<optional label/tag>):
    """
    def __init__(self, label=None):
        self.label = label

    def __enter__(self):
        self.tic = time.perf_counter()
        return(self)

    def __exit__(self, type, value, traceback):
        elapsed = time.perf_counter() - self.tic
        print("Finished %s after %.5fs"%(self.label, elapsed))
        self.elapsed = elapsed

