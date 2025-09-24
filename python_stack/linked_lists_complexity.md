Time and Space Complexity
Traversal

Time Complexity: O(n) – Since you have to traverse through all the nodes in the list to reach the end.

Space Complexity: O(1) – Only a constant amount of extra space is required for a temporary variable to traverse the list.
Insertion at the Beginning

Time Complexity: O(1) – Insertion at the beginning simply involves updating the references at the head.

Space Complexity: O(1) – No additional space is required.
Insertion at the End

Time Complexity: O(n) – It may require traversing the entire list to reach the end where insertion needs to take place.

Space Complexity: O(1) – No additional space is required.
Deletion at the Beginning

Time complexity O(1), it involves updating references at the head.

Space complexity O(1), constant.
Deletion at the End

Time complexity O(n), it may require traversing the entire list to reach the end.

Space complexity O(1), constant.
Summary of Operations for the Time Complexity
Operation Singly Linked List Doubly Linked List Circular Linked List
Traversal O(n) O(n) O(n)
Insertion at Beginning O(1) O(1) O(1)
Insertion at End O(n) O(1) O(n)
Deletion at Beginning O(1) O(1) O(1)
Deletion at End O(n) O(1) O(n)
Summary of Operations for the Space Complexity
Operation Singly Linked List Doubly Linked List Circular Linked List
Traversal O(1) O(1) O(1)
Insertion at Beginning O(1) O(1) O(1)
Insertion at End O(1) O(1) O(1)
Deletion at Beginning O(1) O(1) O(1)
Deletion at End O(1) O(1) O(1)
Differences Between Array and Linked list

A linked list is a dynamic way to represent a list, where adding and removing items from the beginning of the list typically involves changing only a few pointers. This operation can be performed in constant time, denoted as O(1), regardless of the list's size.

On the other hand, arrays are a sequential representation of a list. Adding or removing items from the beginning of the list requires shifting all subsequent elements to accommodate the change. This operation has a time complexity of O(n), where n is the number of elements in the array. Therefore, for large arrays, adding or removing items from the beginning can be relatively slow compared to linked lists.
How to Solve the Remove Duplicates from Sorted List Problem

Explanation of the problem: Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
