class Coder():
    def __init__(self):
        self.name = input("Enter your nam: ")
        self.lang = input("Enter your language")
    def sho_details(self):
        print("Name is "+str(self.name))
        print("The Language is "+str(self.lang))
    
class Pythoneer():
    def __init__(self):
        self.profile = Coder() # containership define father class inside children
    def show(self):
        self.profile.sho_details()

jack = Pythoneer()
jack.show()






