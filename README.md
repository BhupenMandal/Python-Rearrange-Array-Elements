# Python-Rearrange-Array-Elements

## Task Description
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Explanation
I've used Merge Sort to sort the array in a descending order. 
In the sorted list, the evenly distributed elements in the list are the first max sum of the given list and the rest of the digits forms second max sum of the given list for e.g [5, 4, 3, 2, 1] then 5,3,1 are evenly distributed which forms the first max sum and the remaining digits 4,2 forms the second max sum. 

Time Complexity: O(nlogn) for sorting the array and O(n) is for traversing the sorted list to find first max sum and second max sum. Total complexity = O(nlogn) + O(n) = O(nlogn)

Space Complexity: O(n) to store the sorted elements