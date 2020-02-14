print("linklist")


class Node:
    def __init__(self, data):
        self._data = data
        self.next_ = None


class Linkedlist:
    def __init__(self):
        self.head = None
    def traversal(self):
        temp = self.head
        if temp == None:
            print("The list is empty")
        else:
            while temp != None:
                print(temp._data)
                temp = temp.next_

list1 = Linkedlist()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
list1.head = n1
list1.head.next_ = n2
n2.next_ = n3
n3.next_ = n4

list1.traversal()