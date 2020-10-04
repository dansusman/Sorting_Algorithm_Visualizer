"""

Created by Daniel Susman (dansusman)
Date: 10/04/2020

This module holds the MergeSort class, an extension of the Algo class that represents
the sorting of a random array using the merge sort algorithm. Merge sort operates
in O(n log n) time for best case, worst case, and average case. It is probably my
favorite sorting algorithm.

"""
from algorithms import Algo

def mergesort(arr):
    """ Sorts the given array using the divide and conquer algorithm, Mergesort Running
     time complexity: O(n log n) average, best, and worst cases."""
    
    # if the list is greater than 1, we will do in-place sorting in ascending order
    # (otherwise, the list is trivially sorted)
    if (len(arr) > 1):
        # compute middle of array with integer division
        mid = len(arr) // 2

        # using mid at middle point, break arr into two halves
        left = arr[:mid]
        right = arr[mid:]

        # sort each half
        mergesort(left)
        mergesort(right)

        # merge the two halves
        # i will traverse the left half, j the right half, and k the whole list
        i = 0
        j = 0
        k = 0

        while (i < len(left)) and (j < len(right)):
            if (left[i] < right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # copy over leftovers of left half (if they exist)
        while (i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1
        
        #copy over leftovers of right half (if they exist)
        while (j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1
