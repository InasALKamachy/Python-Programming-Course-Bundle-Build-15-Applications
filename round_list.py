l = (2.3343,4.664,1.5353)

def ro_l(l):
  s =0
  if type(l)!='list':
    n = list(l)
    x = [round(num, 1) for num in n]
    for i in x:
      s+=i
  return s
print(ro_l(l))
