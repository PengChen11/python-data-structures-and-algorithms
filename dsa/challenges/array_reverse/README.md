# Reverse an Array

## Challenge
<!-- Description of the challenge -->
write a function to take an array as input, output an array with elements in reversed order

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
two approches:
1st: Big O is length of input array's Floor division to 2
 use the for loop to loop  length of input array's Floor division to 2 times
 each time swamp the left array element with the one from right side.
 return input array.

2nd: Big O is the lenght of input array.
  create an empty array;
  use for loop to loop the length of input array times.
  each time, push the element in reversed order from input array to new array.
  return new array.


## Solution
<!-- Embedded whiteboard image -->
![img1](array_reverse.PNG)
