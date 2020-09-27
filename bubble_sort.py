import random
import time

# enables the visualization of Bubble Sort to occur; can be extended later when other algorithms are
# ready to be visualized
class Algo:
    def __init__(self, name):
        self.arr = random.sample(range(512), 512)
        self.name = name

    def update_view(self):
        import sorting_algo_view
        sorting_algo_view.update(self)

    def run(self):
        self.start_time = time.time()
        self.sortByAlgo()
        time_elapsed = time.time() - self.start_time
        return self.arr, time_elapsed
    
# to represent bubble sort visualizer
class BubbleSort(Algo):
    
    # initialize by assigning bubble sort a name in Algo class
    def __init__(self):
        super().__init__("BubbleSort")
    
    # actual implementation of bubble sort
    def sortByAlgo(self):
        
        # go through whole list, making 1 to 1 comparisons
        # each pass guarantees that largest item is placed in correct place in array
        for _ in range(len(self.arr) - 1):
            for j in range(len(self.arr) - 1):

                # if the element one ahead is less than the one being examined, swap the two
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j+1] = self.arr[j + 1], self.arr[j]
                    
            # visualize each step by reporting which two elements are being swapped
            self.update_view()        


