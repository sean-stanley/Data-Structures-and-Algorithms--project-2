# HTTPRouter using a Trie


Setup a Trie for http route matching. I went for all the bonus objectives.

## Time complexity of methods:

### Router.add_handler:
The worst case time complexity is O(n) where n is the length of the path and the number of nodes to travel through to insert a new route and handler.

### Router.lookup:
The worst case time complexity is O(n) where n is the length of the path and the number of nodes to travel through to find a route's handler.

## Space complexity:
In general the space complexity of both the Router.add_handler and Router.lookup methods is O(1) as only 1 node is held in memory at a time during iterations.
