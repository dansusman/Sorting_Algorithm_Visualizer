# Sorts the given array using the insertion sort algorithm
def insertion_sort(arr):
    
    for i in range (1, len(arr)):
        
        value_at_marker = arr[i]
        
        j = i - 1
        
        # until we find an item whose value is larger than the value at marker, swap elements to the right and 
        # decrement j to examine leftward (compare with everything to the left until find one that is smaller than marker value)
        while (j >= 0) and value_at_marker < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value_at_marker
    

            
        