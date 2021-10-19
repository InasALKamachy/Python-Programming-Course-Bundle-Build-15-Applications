class Coder():
  def __init__(self,name,address,color):
    self.Name = name
    self.Address = address
    self.Color = color
x = Coder('enas','Iraq','red')
print(x.Name)
print(x.Color)
print(x.Address)


*************************
class Colder():
  def __init__(self,name, age):
    self.Name = name
    self.Age = age
  def Employ(self,address,color):
    self.Address = address
    self.Color = color
  def is_python(self):
    if 'Python' in self.language:
      print("True")
    else:
      print("False")


cd = Colder('enas','45')
cd.language=['Python','C++','JavaScript']
cd.Employ('Iraq','red')
print(cd.Address)
print(cd.Age)
print(cd.Name)
print(cd.is_python())


**********************
class Item():
  def __init__(self,name,price=0,total=0):
    assert price >=0, f"price {price} is not equal or more than zero!"
    assert total >=0, f"total {total} is not equal or more than zero!"
    self.name = name
    self.price = price
    self.total = total

  def calculate_total_price(self):
    return self.price*self.total
  def compare(self):
    if self.name =='Laptop':
      print(self.name.upper())


item = Item('Laptop', -250, -3)
item_1 = Item('LG', 500, -5)
print(item.calculate_total_price())
print('the price is :',item_1.calculate_total_price())
print(item.compare())


******************

class Item():
  def __init__(self,name,price=0,total=0):
    self.name = name
    self.price = price
    self.total = total

  def calculate_total_price(self):
    return self.price*self.total
  def compare(self):
    if self.name =='Laptop':
      print(self.name.upper())


item = Item('Laptop', 250, 3)
item_1 = Item('LG', 500, 5)
print(item.calculate_total_price())
print('the price is :',item_1.calculate_total_price())
print(item.compare())
