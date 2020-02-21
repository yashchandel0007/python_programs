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