# Grokking-Algorithms
Code practice and brief notes from the book Grokking Algorithms by Aditya Y. Bhargava

**Reminders**  
All references to log mean log base 2. Example: log base 2 of 1024 = 10 or in terms of exponentials, 2 to the power of 10 equals 1024. 
<img width="1042" height="336" alt="image" src="https://github.com/user-attachments/assets/2450bcc2-b45f-4d8f-b347-41bdf490d024" />


## Chapter 1
**Topics: Binary Search**  
It only works when your list is sorted in ascending order.

It finds an item in a sorted list by repeatedly dividing the search interval in half. If the target value is less than the middle element, it narrows the search to the lower half; otherwise, it searches the upper half until the item is found or the list is exhausted.

Worst and average case performance = O(log n)  
Space = O(1)
