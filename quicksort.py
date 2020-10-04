"""

Created by Daniel Susman (dansusman)
Date: 10/03/2020

This module contains a modified Quick Sort implementation that utilizes 
Insertion Sort for small arrays, thus improving average running time. It
contains the QuickSort class that extends the Algo class, thus inheriting
the ability to display the step-by-step process it takes to sort an array.

"""
import random
from insertion_sort import InsertionSort
from algorithms import Algo
class QuickSort(Algo):
    """ Represents the Bubble Sort algorithm, which is an O(n) best
    case, O(n^2) average case, and O(n^2) worst case algorithm."""

    # initialize by assigning bubble sort a name in Algo class
    def __init__(self):
        super().__init__("Quick Sort")

    def sort_by_algo(self, array=[], start=0, end=0):
        """ Sorts the given array in ascending order using the Quicksort algorithm."""
        if array == []:
            array = self.arr
            end = len(array) - 1
        if end > start:
            # find the pseudo-random pivot
            pivot = self.find_pivot(start, end)
            # partition the array around the pseudo-random pivot
            pivot = self.partition(array, start, end, pivot)
            # sort the two sides of the array
            self.sort_by_algo(array, start, pivot)
            self.sort_by_algo(array, pivot + 1, end)
    def find_pivot(self, start, end):
        """ Finds a random pivot index in the array, to be used when partitioning."""
        return random.randrange(start, end)
    def partition(self, arr, start, end, pivot):
        """ Partitions the list around the pivot so that all values smaller than the value 
        at the pivot are on the left side of the partition and all larger values on the right."""

        value_at_pivot = arr[pivot]

        # swap pivot with first element in the list
        arr[pivot], arr[start] = arr[start], arr[pivot]

        border = start

        # iterate through the list, swap current element with border element if the former is 
        # smaller than pivot value
        for i in range(start, end):
            if arr[i] < value_at_pivot:
                # each time we swap an element to the left, we increment the index of the
                # border (move it to the right)
                border += 1
                arr[i], arr[border] = arr[border], arr[i]
                self.update_view(arr[i], arr[border])
        # swap pivot value with border value
        arr[start], arr[border] = arr[border], arr[start]

        return border
