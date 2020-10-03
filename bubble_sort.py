"""

Created by Daniel Susman (dansusman)
Date: 10/03/2020

This module holds the BubbleSort class, which holds all of the functionality required
to display the sorting of a given array using the Bubble Sort algorithm.

"""
from algorithms import Algo
class BubbleSort(Algo):
    """Represents the Bubble Sort algorithm, which is an O(n^2) best case, worst case, 
    and average case algorithm."""

    # initialize by assigning bubble sort a name in Algo class
    def __init__(self):
        super().__init__("BubbleSort")
    def sort_by_algo(self):
        """Implementation of bubble sort"""

        # go through whole list, making 1 to 1 comparisons
        # each pass guarantees that largest item is placed in correct place in array
        for _ in range(len(self.arr) - 1):
            left_swap = 0
            right_swap = 1
            for j in range(len(self.arr) - 1):

                # if the element one ahead is less than the one being examined, swap the two
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j+1] = self.arr[j + 1], self.arr[j]
                    left_swap = self.arr[j]
                    right_swap = self.arr[j+1]

            # update the view each swap, highlighting the two elements being swapped
            self.update_view(left_swap, right_swap)
            