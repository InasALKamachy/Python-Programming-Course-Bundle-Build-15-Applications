#object class
class Obj():
    def __init__(self):
        self.name = input("Enter your name: ")


class ChildObj():
    def __init__(self):
        self.lange = input("Enter your alnguage")


class Child_Child(Obj, ChildObj): # add classes
    def __init__(self):
        Obj.__init__(self)
        ChildObj.__init__(self) # initialize the class

    def sho(self):
        print("first is "+ self.name + "second is "+self.lange)



l = Child_Child()
l.sho()


