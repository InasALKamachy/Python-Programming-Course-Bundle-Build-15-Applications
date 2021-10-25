class SumPair():
  def __init__(self, lst):
    self.List = lst
    self.List_len = len(lst)
    self.i1 = 0
    self.i2 = 0
  def __iter__(self):
    return self
  def __next__(self):
    if self.i2 ==self.List_len:
      raise StopIteration
    else:
      self.sum_pair = self.List[self.i1]+ self.List[self.i2]
      self.i1 += 1
      self.i2 += 1
      return self.sum_pair

l = SumPair([1,2,3,4,55])
for ele in l:
  print(ele)
print(l.List_len)
