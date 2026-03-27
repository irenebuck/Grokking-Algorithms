# Book version
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

my_arr = [2,5,2,6,7,8,1,34]
print(selectionSort(my_arr))


# In-place version, no new array needed
def selectionSort2(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

my_arr2 = [3,5,3,5,2,5,2,6,7,8,1,34]

print(selectionSort2(my_arr2))