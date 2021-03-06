import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # self.size = 0
        # Last in first out
        # Why is our DLL a good choice to store our elements?
        # Doubly Linkked Lists have a tail pointer, so we can push and pop easier from the end / top of stack.
        self.storage = DoublyLinkedList()
w
    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
