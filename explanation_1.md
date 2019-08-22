# Finding the Square Root of an Integer

In my research there seemed to be many ways of calculating square roots. Some very old and some only possible with computers. Since only a rough estimate was needed for the problem though I chose the Babylonian method. This method requires an initial estimation and then converges in accuracy with every additional calculation made.

Time complexity:
The worst-case time complexity can be described as O(n) where n is the count of the number of digits in the input number. As the algorithm uses this length to set an arbitrary limit on the number of iterations.

Space complexity:
The space complexity is effectively O(n) where n is the number of iterations on the recursive function. As the call stack keeps increasing for every recursion. The max number of recursions is controlled by the number of digits in the input number.
