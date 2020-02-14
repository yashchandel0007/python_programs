print("linklist")


class Node:
    def __init__(self, data):
        self._data = data
        self._next_ = None


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
                temp = temp._next_
    def addNodeBeginning(self,data):
         if self.head == None:
             self.head = Node(data)
         else:
             temp = self.head
             while(temp._next_ !=None):
                 temp = temp._next_
             temp._next_ = Node(data)
             
list1 = Linkedlist()

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# list1.head = n1
# list1.head._next_ = n2
# n2._next_ = n3
# n3._next_ = n4

for i in range(10, 0, -1):
    list1.addNodeBeginning(i)

list1.traversal()