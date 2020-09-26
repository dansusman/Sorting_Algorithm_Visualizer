# Sorts the given array using the selection sort algorithm
def selection_sort(arr):
    
    for i in range (len(arr)):
        min_index = i
        
        for j in range (i + 1, len(arr)):
            if (arr[j] < arr[min_index]):
                min_index = j
            
        # swap minimum element with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    
                
