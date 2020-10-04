"""

Created by Daniel Susman (dansusman)
Date: 10/04/2020

This module holds the MergeSort class, an extension of the Algo class that represents
the sorting of a random array using the merge sort algorithm. Merge sort operates
in O(n log n) time for best case, worst case, and average case. It is probably my
favorite sorting algorithm.

"""
from algorithms import Algo
class MergeSort(Algo):
    """ Represents the Merge Sort algorithm and contains all of its functionality
    and data."""
    # initialize by assigning merge sort a name in Algo class
    def __init__(self):
        super().__init__("Merge Sort")

    def sort_by_algo(self, array=[]):
        """ Sorts the given array using the divide and conquer algorithm, Mergesort Running time
        complexity: O(n log n) average, best, and worst cases."""
        if array == []:
            array = self.arr
        if len(array) < 2:
            return array
        # if the list is greater than 1, we will do in-place sorting in ascending order
        # (otherwise, the list is trivially sorted)
        if len(array) > 1:
            # compute middle of array with integer division
            mid = len(array) // 2

            # using mid at middle point, break arr into two halves
            left = array[:mid]
            right = array[mid:]

            sort_left = self.sort_by_algo(left)
            sort_right = self.sort_by_algo(right)
            # sort each half and merge
            return self.merge(sort_left, sort_right)

    def merge(self, left, right):
        """ Merge the two halves."""
        result = []
        # i will traverse the left half, and j the right half
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # copy over leftovers of left half (if they exist)
        result += left[i:]
        #copy over leftovers of right half (if they exist)
        result += right[j:]
        self.update_view()
        return result
