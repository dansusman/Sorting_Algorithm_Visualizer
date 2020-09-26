import random

# Sorts the given array in ascending order using the Quicksort algorithm


def quicksort(arr, start, end):

    # optimize further the speed of this algorithm by using selection sort on arrays of small size
    #if (end - start < 20) and (end > start):
    #    selection_sort(arr, start, end)

    if (end > start):

        # find the pseudo-random pivot
        pivot = find_pivot(start, end)

        # partition the array around the pseudo-random pivot
        pivot = partition(arr, start, end, pivot)

        # sort the two sides of the array
        quicksort(arr, start, pivot)
        quicksort(arr, pivot + 1, end)


def find_pivot(start, end):
    return random.randrange(start, end)


def partition(arr, start, end, pivot):

    value_at_pivot = arr[pivot]

    # swap pivot with first element in the list
    arr[pivot], arr[start] = arr[start], arr[pivot]

    border = start

    # iterate through the list, swap current element with border element if the former is smaller than pivot value
    for i in range(start, end):
        if arr[i] < value_at_pivot:
            # each time we swap an element to the left, we increment the index of the border (move it to the right)
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    # swap pivot value with border value
    arr[start], arr[border] = arr[border], arr[start]

    return border