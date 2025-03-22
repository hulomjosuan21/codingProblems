class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
<<<<<<< HEAD
        self.head = Node

    def print(self):
        ...
=======
        self.head = node

    def insert_at_end(self,data):
        if not self.head:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def print(self):
        if not self.head:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

ll = LinkedList()
ll.insert_at_end(5)
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)

ll.print()
>>>>>>> 4fd67513875c4341b71639a2397c64e8a24533d7
