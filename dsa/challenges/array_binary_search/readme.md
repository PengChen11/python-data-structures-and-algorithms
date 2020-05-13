# Binary search in a sorted 1D array

## Challenge
<!-- Description of the challenge -->
WWrite a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
without using any build-in list method, it is:
1. since we are searching from a sorted array, if the key is greater than the last element inside of the array, don't even do the search. just return -1.
2. then will always compair the key with element that has the middle index first, if key is smaller than that element, get rid or the greater half of the array, do the search again; vice versa.


## Solution
<!-- Embedded whiteboard image -->
![img](array_shift.PNG)
