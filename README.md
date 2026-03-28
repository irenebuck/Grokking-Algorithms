# Grokking Algorithms
Code practice and brief notes from the book Grokking Algorithms by Aditya Y. Bhargava

**Reminders**  
All references to log mean log base 2.  
Example: log base 2 of 1024 = 10 or in terms of exponentials, 2 to the power of 10 equals 1024. 


## Chapter 1
**Topic: Binary Search**  
It only works when your list is sorted.

It finds an item in a sorted list by repeatedly dividing the search interval in half. If the target value is less than the middle element, it narrows the search to the lower half; otherwise, it searches the upper half until the item is found or the list is exhausted.

Time = O(log n)  
Space = O(1)


## Chapter 2
**Topic: Arrays and Linked Lists**  

| Action | Arrays | Linked Lists |  
| :---: | :---: | :---: |  
| Reading | O(1) | O(n) |  
| Insertion | O(n) | O(1) |  
| Deletion | O(n) | O(1) |  

Arrays allow fast reads. All elements are stored next to each other, and should be the same type. Arrays can be accessed randomly, meaning any index can be accessed without requiring a prior index to be accessed.    

Linked lists allow fast inserts and deletes. Elements are strewn all over memory space with each element storing the address of the next one. Linked Lists can only do sequential access, meaning starting at the first element and accessing in order until the end is reached.  

**Topic: Selection Sort**  
The book's version offers a helper function to find the index of the smallest value element, pops the element from the original array, and appends the smallest value to a new array. The new array is returned.  

Time = O(n^2)  
Space = O(n)  

My version does not create a new array, it swaps elements with it's neighbor when element at the next index is smaller. No helper function is needed as the loops are nested.  

Time = O(n^2)  
Space = O(1)  


## Chapter 3
**Topic: Recursion**  
Recursion is where a function calls itself and has two parts:  
1- the recursive case where it calls itself  
2- the base case that stops the calling of the function.  

The book's example is a simple factorial function, decrementing one for each call until the base case of one is reached.  

Time: O(n)  
Space: O(n)

A recusive version of binary search is included for comparison to the "binary search.py" file. 

Time: O(log n)  
Space: O(log n)  


## Chapter 4
**Topic: Divide and Conquer**  
This is a recusive technique for dividing your problem into smaller ones until you reach a base case. There are two steps:  
1- Figure out the base case, typically the simplest case.  
2- Divide or decrease your problem until it becomes the base case. When an array is involved, the base case is often an empty array or an array with one element in it.  

The quicksort code sample demonstrates D&C.  

**Topic: Quicksort**  
This algorithm picks a pivot and partitions the rest of the elements into two subarrays. The first subarray includes elements less than or euqal to the pivot and the second has elements greater than the pivot. Each subarray gets the same treatment until there are 0 or 1 elements in the subarrays. Then, each side is recursively sorted and the results are concatenated.  

Time: worst O(n^2), average O(n log n)  
Space: O(n)