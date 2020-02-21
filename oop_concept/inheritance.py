class base:
    def __init__(self):
        self.constant = 1
    def method(self):
        print("this is base class.")


class derrived(base):
    def __init__(self):
        base.__init__(self)
        self.calling()
        # base.__init__(self)

    def calling(self):
        self.method()
        base.method(self)
        print(self.constant)

    def method(self):
        print("this is derrived class")

object = derrived()