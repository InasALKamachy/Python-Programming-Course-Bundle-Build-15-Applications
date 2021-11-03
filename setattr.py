class Gree():
  def __init__(self,name):
    self.name = 'hyder'
  def show(self):
    print("Hello "+self.name)
R = Gree('enas')
print(R.name)

setattr(R,'name','enas')
print(R.name)
