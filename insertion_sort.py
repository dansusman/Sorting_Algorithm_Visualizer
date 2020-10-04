"""
Created by Daniel Susman (dansusman)
Date: 10/03/2020

This module holds the InsertionSort class, which holds all of the functionality required
to display the sorting of a given array using the Insertion Sort algorithm.

"""

from algorithms import Algo
class InsertionSort(Algo):
    """ Represents the Insertion Sort algorithm, which is an 
    O(n^2) best case, worst case, and average case algorithm."""
    # initialize by assigning insertion sort a name in Algo class
    def __init__(self):
        super().__init__("Insertion Sort")
        
    def sort_by_algo(self):
        """ Sorts the given array using the insertion sort algorithm."""
        for i in range (1, len(self.arr)):
            value_at_marker = self.arr[i]
            j = i - 1
            # until we find an item whose value is larger than the value at marker, swap
            # elements to the right and decrement j to examine leftward (compare with
            # everything to the left until find one that is smaller than marker value)
            while (j >= 0) and value_at_marker < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = value_at_marker
            self.update_view(self.arr[j], self.arr[i])
