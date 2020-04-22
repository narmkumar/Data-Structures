import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        #First in, first out
        # Why is our DLL a good choice to store our elements?
        # A queue inserts elements from the front and removes from the back,s
        # DLL is an efficient data structure to implement this bc RV traversal ability
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        self.storage.remove_from_tail()

    def len(self):
        return self.storage.length