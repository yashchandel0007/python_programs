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
    def addNodeEnd(self,data):
         if self.head == None:
             self.head = Node(data)
         else:
             temp = self.head
             while(temp.next_ !=None):
                 temp = temp.next_
             temp.next_ = Node(data)
    def addNodeBeginning(self, data):
        new_node = Node(data)
        new_node.next_ = self.head
        self.head = new_node


             
list1 = Linkedlist()
list2 = Linkedlist()

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# list1.head = n1
# list1.head.next_ = n2
# n2.next_ = n3
# n3.next_ = n4

for i in range(10, 0, -1):
    list1.addNodeBeginning(i)
for i in range(1, 11):
    list2.addNodeEnd(i)

list1.traversal()
list2.traversal()