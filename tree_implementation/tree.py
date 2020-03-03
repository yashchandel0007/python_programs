class Node:
    def __init__(self):
        self.__data = None
        self.__left = None
        self.__right = None

    def get__data(self):
        return self.__data

    def get__left(self):
        return self.__left

    def get__right(self):
        return self.__right

    def set__data(self, data):
        self.__data = data

    def set__left(self, left):
        self.__left = left

    def set__right(self, right):
        self.__right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def convention_inorder(self, root):
        if root is not None:
            self.convention_inorder(root.get__left())
            print(root.get__data(), end=" -> ")
            self.convention_inorder(root.get__right())

    def convention_preorder(self, root):
        if root is not None:
            print(root.get__data(), end=" -> ")
            self.convention_preorder(root.get__left())
            self.convention_preorder(root.get__right())

    def convention_postorder(self, root):
        if root is not None:
            self.convention_postorder(root.get__left())
            self.convention_postorder(root.get__right())
            print(root.get__data(), end=" -> ")

    def converse_inorder(self, root):
        if root is not None:
            self.converse_inorder(root.get__right())
            print(root.get__data(), end=" -> ")
            self.converse_inorder(root.get__left())

    def converse_preorder(self, root):
        if root is not None:
            print(root.get__data(), end=" -> ")
            self.converse_preorder(root.get__right())
            self.converse_preorder(root.get__left())

    def converse_postorder(self, root):
        if root is not None:
            self.converse_postorder(root.get__right())
            self.converse_postorder(root.get__left())
            print(root.get__data(), end=" -> ")

n1 = Node()
n1.set__data(4)

n2 = Node()
n2.set__data(1)

n3 = Node()
n3.set__data(7)

n4 = Node()
n4.set__data(3)

n5 = Node()
n5.set__data(5)

n6 = Node()
n6.set__data(2)

n7 = Node()
n7.set__data(6)

tree = Tree(n1)
n1.set__left(n2)
n1.set__right(n3)
n2.set__right(n4)
n3.set__left(n5)
n4.set__left(n6)
n5.set__right(n7)

print("Conventional Inorder")
tree.convention_inorder(tree.root)
print("\nConventional Preorder")
tree.convention_preorder(tree.root)
print("\nConventional Postorder")
tree.convention_postorder(tree.root)
print("\nConverse Inorder")
tree.converse_inorder(tree.root)
print("\nConverse Preorder")
tree.converse_preorder(tree.root)
print("\nConverse Postorder")
tree.converse_postorder(tree.root)
