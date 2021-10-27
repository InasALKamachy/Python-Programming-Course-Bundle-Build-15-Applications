class Number():
    def __init__(self):
        self.num = 0
    def increase(self):
        self.num += 1
    def decrease(self):
        self.num -=1
class newNumber(Number):
    def __init__(self):
        super().__init__()
    def show_nu(self):
        print("the nimber is : "+str(self.num))

num = newNumber()
new_number = 100 #public variable can be access in all program
_newNumber = 50 # privet variable can be access inside the class (parent, child)
__newNumber = 10 #privet variable can be access isnside the child class onley

num.show_nu()
num.increase()
num.show_nu()
