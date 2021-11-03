def upp(x):
  return x.upper()
L1 = ['ens','hello']


x = map(upp,L1)

print([i for i in x])


#OR

print(
  [i for i in map(lambda up: up.upper(),L)]
)

