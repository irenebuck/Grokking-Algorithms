# Grokking-Algorithms
Code practice and brief notes from the book Grokking Algorithms by Aditya Y. Bhargava

**Reminders**
All references to log mean log base 2. Example: log base 2 of 1024 = 10 or in terms of exponentials, 2 to the power of 10 equals 1024. 

## Chapter 1
**Topics: Binary Search**
It only works when your list is sorted in ascending order.

It finds an item in a sorted list by repeatedly dividing the search interval in half. If the target value is less than the middle element, it narrows the search to the lower half; otherwise, it searches the upper half until the item is found or the list is exhausted.

Performance Complexity = O(log n)  
Space Complexity = O(1)
