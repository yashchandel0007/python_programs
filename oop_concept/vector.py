class Vector:
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return repr(self.data)
    def __add__(self, other):
        data = []
        for i in range(len(self.data)):
            data.append(self.data[i]+other.data[i])
        return Vector(data)
    
    def __sub__(self, other):
        data = []
        for i in range(len(self.data)):
            data.append(self.data[i]-other.data[i])
        return Vector(data)

x = Vector([1,2,3])
y = Vector([1,2,3])

print(x+y)
print(x-y)
