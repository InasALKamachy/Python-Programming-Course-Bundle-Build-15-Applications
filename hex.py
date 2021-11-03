
def he(num):
  if type(num)== int:
    print(hex(num))
  elif type(num)==float:
    print(num.hex())

he(222)
