def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        middle = int((low + high)/2)
        guess = sorted_list[middle]
        if guess == item:
            print(f'The index of {item} is {middle}.')
            return
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    print(f'The number was not found in the list.')

my_list = [1,3,5,81,256,500,760,999]

binary_search(my_list, 67)
binary_search(my_list, 500)