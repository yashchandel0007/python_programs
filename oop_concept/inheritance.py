class base:
    def __init__(self):
        self.constant = 1
    def method(self):
        print("this is base class.")
    def getconstant(self):
        return self.constant

class derrived(base):
    def __init__(self):
        base.__init__(self)
        self.calling()
        # base.__init__(self)

    def calling(self):
        self.method()
        base.method(self)
        # print(self.constant)
        print(base.getconstant(self))

    def method(self):
        print("this is derrived class")

object = derrived()


class A:
    def function(self):
        print("this is function A")


class B(A):
    def function(self):
        print("this is function B")
        super(B, self).function()


class C(B):
    def function(self):
        print("this is function C")
        super(C, self).function()

newObject = C()
newObject.function()