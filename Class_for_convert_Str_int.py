class Convert():
  def __init__(self, Str =''):
    self.Str = Str
  def con(self):
    return int(self.Str)

convert = Convert('1023')
print(convert.con()*2)
print(convert.Str*2)
