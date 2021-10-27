#object class
class Obj():
    def __init__(self):
        self.name = input("Enter your name: ")
        self.lange = input("Enter your alnguage")
    def show(self):
        print("Hello "+ str(self.name))
        print("hello "+ str(self.lange))

class ChildObj(Obj):
    def __init__(self):
        super().__init__()
    def showmore(self):
        print("hello my is childObj"+ str(self.name))
    def language(self):
        self.lange = input("Enter name ;"+ str(self.lange))

class Child_Child(ChildObj):
    def __init__(self):
        super().__init__()
    def rep(self):
        print("your are in third class")


l = Child_Child()
l.showmore()
l.name
l.rep()
l.language()
