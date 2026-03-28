def quicksort(arr):
    if len(arr) < 2:
        # base case - array has 0 or 1 elements in it
        return arr  
    else:
        pivot = arr[0]
        # sub array with all elements less than or equal to the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub array with all elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
my_array = [2,23,56,24,987,45,345,4]    
print(quicksort(my_array))