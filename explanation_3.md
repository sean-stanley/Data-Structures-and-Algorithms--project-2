# Rearrange Array Elements

The solution to this problem was to sort the list from highest to lowest. Then split the digits up between the first and second output numbers. This was fastest using string concatenation.

Time complexity:
The worst case time complexity is O(nlog(n)) where n is the size of the initial list. This is because we do a merge sort on the input list. We finish with a linear loop of the input list but this does not change the time complexity.

Space complexity:
The space complexity is O(n) where n is the size of the input array because we construct a new array of equal size during the sorting process.
