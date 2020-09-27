# Sorts the given array using Radix Sort, also known as bucket sort to some
def radix_sort(arr, max_digits):

    length = len(arr)    
    
    # initialize result array 
    result_array = [0] * length
    
    # initialize counting array 
    count_array = [0] * 10
    
    # add counts of occurrences into count_array
    for i in range(0, length):
        idx = (arr[i] / max_digits)
        count_array[idx % 10] += 1
        
    