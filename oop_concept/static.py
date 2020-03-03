class Example:
    staticVariable = 5

    def __init__(self):
        self.exampleVariable = 0


    @staticmethod   #decorators
    def staticmethod():
        print("this is a static method.")


instance = Example()
print(Example.staticVariable)
print(instance.staticVariable)

print(dir(Example))


instance.staticVariable = 6
print(Example.staticVariable)
print(instance.staticVariable)   #still don't know where this variable is added
print(instance.exampleVariable)

print(dir(instance))  #don't know why the new variable staticVariable is not displayed twice by this function once for the static variable and one for the explicitly added variable







