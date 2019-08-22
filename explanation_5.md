# Question Title

Autocomplete with Tries

The notebook was exported as a .py file from Udacity's website.

Time complexity of suffixes method:
The worst case time complexity is O(n) where n is the number of leaves on the subtrie from the prefix. This is because the recursion searches every branch and leaf from the prefix onwards.

Space complexity of suffixes method:
The space complexity is O(n) where n is the number of branches and leaves in the trie beneath the prefix. This is because the recursion call stack grows to a length of n.
