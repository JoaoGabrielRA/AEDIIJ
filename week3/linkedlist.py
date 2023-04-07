
class Node:
    """A class representing a node in a doubly linked list."""

    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    """A class representing a doubly linked list."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, data):
        """Add a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
    def __iter__(self):
        """Return an iterator for the linked list."""
        self._iter_node = self.head
        return self 
    
    def __next__(self):
        """Return the next value in the linked list."""
        if self._iter_node is None:
            raise StopIteration
        ret = self._iter_node.data
        self._iter_node = self._iter_node.next
        return ret
    
    def prepend(self, data):
        """Add a new node with the given data to the beginning of the linked list."""
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def __len__(self):
        """Return the length of the linked list."""
        return self.length
    
    def __str__(self):
        """Return a string representation of the linked list."""
        return str([value for value in self])

    def __eq__(self, other):
        """Check if two linked lists are equal.

        Traverse both linked lists and compare the data of each node. 
        If the data of all nodes in both linked lists match, return True. 
        Otherwise, return False.

        Args:
            other (LinkedList): The linked list to compare with self.

        Returns:
            bool: True if the linked lists are equal, False otherwise.
        """
        # Check if the lengths of the linked lists are the same
        if len(self) != len(other):
            print(self,other)
            return False
        
        # Iterate over both linked lists and compare the data of each node
        for node1, node2 in zip(self, other):
            if node1 != node2:
                print(node1.data,node2.data)
                return False
        
        # If we made it this far, the linked lists are equal
        return True
