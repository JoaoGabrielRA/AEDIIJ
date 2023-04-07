from linkedlist import *

class Stack(LinkedList):
    """
    This class represents a stack data structure that inherits from a linked list.
    
    Methods:
    push(data) -- adds a new node to the top of the stack with the given data.
    peek() -- returns the data at the top of the stack without removing it.
    pop() -- removes and returns the node at the top of the stack.
    """
    
    def push(self, data):
        """
        Adds a new node to the top of the stack with the given data.
        
        Arguments:
        data -- the data to be stored in the new node.
        """
        self.append(data)

    def peek(self):
        """
        Returns the data at the top of the stack without removing it.
        """
        return self.tail.data

    def pop(self):
        """
        Removes and returns the node at the top of the stack.
        
        Returns:
        The data stored in the node at the top of the stack.
        """
        ret = self.tail.data
        if self.length == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret
