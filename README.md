# Grokking-Algorithms
Code practice and brief notes from the book Grokking Algorithms by Aditya Y. Bhargava

**Reminders**  
All references to log mean log base 2. Example: log base 2 of 1024 = 10 or in terms of exponentials, 2 to the power of 10 equals 1024. 


## Chapter 1
**Topics: Binary Search**  
It only works when your list is sorted.

It finds an item in a sorted list by repeatedly dividing the search interval in half. If the target value is less than the middle element, it narrows the search to the lower half; otherwise, it searches the upper half until the item is found or the list is exhausted.

Worst and average case performance = O(log n)  
Space = O(1)


## Chapter 2
**Topics: Arrays and Linked Lists, and Selection Sort**  
Linked Lists can only do sequential access, meaning starting at the first element and accessing in order until the end is reached.  
Arrays can be accessed randomly, meaning any index can be accessed without requiring a prior index to be accessed.  

| Action | Arrays | Linked Lists |  
| :---: | :---: | :---: |  
| Reading | O(1) | O(n) |  
| Insertion | O(n) | O(1) |  
| Deletion | O(n) | O(1) |  

Arrays allow fast reads. All elements are stored next to each other, and should be the same type.  

Linked lists allow fast inserts and deletes. Elements are strewn all over memory space with each element storing the address of the next one.  
 
