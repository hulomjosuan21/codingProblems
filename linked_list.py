class Node:
    def __init__(self,data,_next):
        self.data = data
        self._next = _next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = Node

    def print(self):
        ...