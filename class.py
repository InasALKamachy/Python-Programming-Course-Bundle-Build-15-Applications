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
