"""

Created by Daniel Susman (dansusman)
Start Date: 09/2020

To generalize the implementation of sorting algorithms, this module contains the generic
Algo class, from which all specific algorithms will inherit functionality and data.

This is an OOP approach to this visualizer, as extension without heavy modification
will definitely be required as the project grows and more algorithms are included.

It is currently a work in progress.

"""

import random
import time

class Algo:
    """Enables the visualization of Bubble Sort to occur; can be extended later when other
    algorithms are ready to be visualized, as each sort will be an Algo thus inheriting
    the behaviors of this Algo class."""
    def __init__(self, name):
        """Initializes an Algo object given a string representing its name; 
        e.g. "Bubble Sort. Creates random array of length 800 with numbers from 0 to 800."""
        self.arr = random.sample(range(700), 700)
        self.name = name

    def update_view(self, left_swap=None, right_swap=None):
        """Updates the view at every iteration in order to display the sorting algorithms
        step-by-step."""
        import sorting_algo_view
        sorting_algo_view.update(self, left_swap, right_swap)
    def run(self):
        """Runs the sorting algorithm with visualization."""
        self.start_time = time.time()
        self.sort_by_algo()
        time_elapsed = time.time() - self.start_time
        return self.arr, time_elapsed
