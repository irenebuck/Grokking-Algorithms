# Book example
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
factorial_value = factorial(5)
print(factorial_value)


# Recursive binary search - returns index of target in array
def binary_search(arr, target):
    def helper(low, high):
        if low > high:
            return -1
        
        mid = (low + high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid +1, high)
        else:
            return helper(low, mid - 1)
        
    return helper(0, len(arr)-1)

my_list = [1,3,5,81,256,500,760,999]

print(binary_search(my_list, 500))
