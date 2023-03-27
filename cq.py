# -- coding: utf-8 --
"""
Created on Tue Mar 14 15:42:53 2023

@author: Jorge Roa & Carmen Garro
"""

class Empty(Exception):
    pass

class CircularQueue:
    """Queue implementation"""

    # Define the Node class for the circularly linked list
    class _Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, nxt):
            self.element = element
            self.next = nxt

    # Initialize the CircularQueue object
    def __init__(self):
        self._tail = None
        self._size = 0

    # Return the length (size) of the queue
    def __len__(self):
        return self._size

    # Check if the queue is empty
    @property
    def is_empty(self):
        return self._size == 0

    # Get the first element in the queue
    @property
    def first(self):
       if self.is_empty:
           raise Empty("The queue is empty")
       head = self._tail.next
       return head.element

    # Remove and return the first element from the queue
    def dequeue(self):
        if self.is_empty:
            raise Empty("The queue is empty")
        former_head = self._tail.next
        dequeued_element = former_head.element
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = former_head.next
        self._size -= 1
        return dequeued_element

    # Add a new element to the end of the queue
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty:
            newest.next = newest
        else:
            newest.next = self._tail.next
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    # Move the first element to the end of the queue
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail.next

    # Provide a formal string representation of the CircularQueue object
    def __repr__(self):
        return f"CircularQueue(size={self._size})"

    # Provide a readable string representation of the CircularQueue object
    def __str__(self):
        if self.is_empty:
            return "Empty Queue"
        result = []
        current = self._tail.next
        for _ in range(self._size):
            result.append(str(current.element))
            current = current.next
        return " -> ".join(result)

    # Check if a value is present in the queue using the 'in' keyword
    def __contains__(self, value):
        if self.is_empty:
            return False
        current = self._tail.next
        for _ in range(self._size):
            if current.element == value:
                return True
            current = current.next
        return False

    # Look at the next element to be dequeued without removing it
    def peek(self):
        if self.is_empty:
            raise Empty("The queue is empty")
        return self._tail.next.element


