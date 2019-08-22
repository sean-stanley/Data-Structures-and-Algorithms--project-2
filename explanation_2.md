# Search in a Rotated Sorted Array

A divide and conquer algorithm similar to a binary search is done to find the number.

However extra logic and checks happen to test if we are searching a pre-sorted chunk or not.

Time complexity:
The worst case time complexity is O(log(n)) where n is the size of the array to be search. This is because this algorithm is still similar enough to a binary search algorithm the worst case time complexity does not change.

Space complexity:
The space complexity is O(1) as the only data being created are the start, end and middle pointers.
