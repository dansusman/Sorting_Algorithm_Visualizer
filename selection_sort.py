"""

Created by Daniel Susman (dansusman)
Date: 10/03/2020

This module holds the implementation for the Selection Sort algorithm. It enables
sorting of a random array and display of step-by-step actions taken to do so.

"""
from algorithms import Algo

class SelectionSort(Algo):
    """ Represents a Selection Sort algorithm which has an O(n^2) best case, worst case, 
    and average case running time"""
    def __init__(self):
        super().__init__("Selection Sort")
    def sort_by_algo(self):
        """Sorts the array using Selection Sort sorting algorithm."""
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            # swap minimum element with first element
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            # update the view each swap, highlighting the two elements being swapped
            self.update_view(self.arr[i], self.arr[min_index])
