#print the attribute values as dic 

class Gree():
  def __init__(self,name,age,address):

    self.name = name
    self.age = age
    self.address = address

dd = Gree('enas',15,'iraq')
print(vars(dd))
    
