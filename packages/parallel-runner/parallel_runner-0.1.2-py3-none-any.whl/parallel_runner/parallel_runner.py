from multiprocessing import Process, Manager, Semaphore
from tqdm import tqdm

class ParallelRunner:
    """
    A class for running functions in parallel using multiprocessing.
    Supports indexed execution, normal and array arguments, and progress tracking.
    
    Example usage:
    
    def sample_task(ix, x, y):
        return x + y + ix  # Example function that takes indexed arguments
    
    runner = ParallelRunner(
        procedure=sample_task,
        debug=False,
        concurrency=4,
        ix_needed=True,
        use_tqdm=True,
        array_args={"x": [1, 2, 3, 4], "y": [10, 20, 30, 40]},
    )
    
    results = runner.run()
    print(results)  # Outputs results as a dictionary
    """
    def __init__(self, procedure, debug=False, concurrency=8, ix_needed=False, use_tqdm=False, no_iteration=None, normal_args=None, array_args=None):
        """
        Initializes the ParallelRunner.
        
        :param procedure: Function to be executed in parallel.
        :param debug: If True, runs sequentially for debugging.
        :param concurrency: Number of parallel processes.
        :param ix_needed: If True, passes index to function. Function should have an input argument called 'ix'.
        :param use_tqdm: If True, uses tqdm for progress tracking.
        :param no_iteration: Number of iterations (required if array_args is empty).
        :param normal_args: Dictionary of normal arguments (same for all processes).
        :param array_args: Dictionary of list-based arguments (different for each process).
        """
        self.procedure = procedure
        self.debug = debug
        self.concurrency = concurrency
        self.ix_needed = ix_needed
        self.use_tqdm = use_tqdm
        self.normal_args = normal_args or {}
        self.array_args = array_args or {}
        
        # Ensure all array_args have the same length
        array_lengths = [len(v) for v in self.array_args.values()]
        if len(set(array_lengths)) > 1:
            raise ValueError("Error: All array arguments must have the same length!")
        
        self.no_times = array_lengths[0] if array_lengths else no_iteration
        if self.no_times is None:
            raise ValueError("Error: You must specify no_iteration if array_args is empty.")
    
    def _mittle_runner(self, ix):
        """
        Internal function to execute a single instance of the procedure.
        
        :param ix: Index of the execution instance.
        """
        try:
            all_args = {**self.normal_args}
            if self.ix_needed:
                all_args["ix"] = ix
            for key, values in self.array_args.items():
                all_args[key] = values[ix]
            
            self.results[ix] = self.procedure(**all_args)
        except Exception as e:
            print(f"Error in ParallelRunner at index {ix}: {e}")
        finally:
            self.semaphore.release()
            if self.use_tqdm:
                self.progress.value += 1


    def update_progressbar(self):
        self.pbar.n = self.progress.value
        self.pbar.last_print_n = self.progress.value
        self.pbar.update(0)                 


    def run(self):
        """
        Runs the procedure in parallel using multiprocessing.
        
        :return: Dictionary containing results from each process.
        """
        try:
            manager = Manager()
            self.results = manager.dict()
            self.progress = manager.Value("i",0)
            self.semaphore = Semaphore(self.concurrency)

            if self.debug:
                # Run sequentially for debugging
                iterator = tqdm(range(self.no_times)) if self.use_tqdm else range(self.no_times)
                for i in iterator:
                    self._mittle_runner(i)
            else:
                # Run in parallel
                jobs = []
                if self.use_tqdm:
                    self.pbar = tqdm(total=self.no_times)

                for i in range(self.no_times):
                    self.semaphore.acquire()
                    if self.use_tqdm:
                        self.update_progressbar()
                    p = Process(target=self._mittle_runner, args=(i,))
                    jobs.append(p)
                    p.start()

                if self.use_tqdm:
                    while any(p.is_alive() for p in jobs):
                        self.update_progressbar()
               
                for job in jobs:
                    job.join()

                if self.use_tqdm:
                    self.pbar.close()  
            
            return dict(self.results)
        except Exception as e:
            print(f"Error in ParallelRunner(run): {e}")
            return {}
