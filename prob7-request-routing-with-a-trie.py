# A RouteTrie will store our routes and their associated handlers

class RouteTrie:
    """Store, insert and find routes by arrays of address nodes."""

    def __init__(self, rootHandler):
        """
        Initialize the RouteTrie with a root node to represent '/'.

        rootHandler @String message returned for the root handler node.
        """
        self.root = RouteTrieNode(rootHandler)

    def insert(self, path, handler=None):
        """
        Insert a new path and handler into the RouteTrie.

        path @String<[]> List of paths to follow. Intermediate steps created
          have no handler.
        handler @String Message to return when our route is called.

        return void
        """
        current_node = self.root
        for node in path:
            if node not in current_node.children:
                current_node.insert(node)
            current_node = current_node.children[node]

        current_node.handler = handler


    def find(self, path):
        """
        Navigate the RouteTrie until arriving at the path. Return the handler.

        path @String<[]> List of paths to follow.

        return @String|None The handler message or None if it's undefined.
        """
        current_node = self.root

        for node in path:
            if node not in current_node.children:
                return None
            current_node = current_node.children[node]

        return current_node.handler


class RouteTrieNode:
    """RouteTrieNode is the branch and leaves of a RouteTrie."""

    def __init__(self, handler=None):
        """Initialize a route node with children and an optional handler."""
        self.handler = handler
        self.children = {}

    def insert(self, route, handler=None):
        """
        Insert the node into children.

        route @String: String of last portion of full path.
        handler @String: String to return from the new node.

        return voids
        """
        # Insert the node as before
        self.children[route] = RouteTrieNode(handler)

    def getHandler(self):
        """Getter for the handler's data."""
        return self.handler


# The Router class will wrap the Trie and handle


class Router:
    """Main router that stores the RouteTrie and returns handlers."""

    def __init__(self, rootHandler, routeNotFoundHandler=None):
        """Initialize the route trie. Initialize the notFoundHandler."""
        self.route_trie = RouteTrie(rootHandler)

        self.handle_404 = routeNotFoundHandler

    def add_handler(self, path, handler):
        """
        Add a handler to a path.

        path @String URL path ie. /about/founder
        handler @String message to return when route is requested.

        return void
        """
        path_list = split_path(path)
        self.route_trie.insert(path_list, handler)

    def lookup(self, path):
        """
        Add a handler to a path.

        path @String URL path ie. '/about/founder/'

        return route handler or self.handle_404
        """
        path_list = split_path(path)

        handler = self.route_trie.find(path_list)
        if not handler:
            return self.handle_404
        return handler


def split_path(path):
    """
    Split a path along '/' and trim any trailing '/'.

    path @String URL path ie. '/about/founder/'

    return @String<[]> a list of path nodes ie. ['about', 'founder']
    """
    path_list = path.split('/')

    if path_list[0] == '':
        path_list.pop(0)
    if path_list[-1] == '':
        path_list.pop(-1)

    return path_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
