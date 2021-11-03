L=[1,2,3,4]
M = ['enas','E','R','C']
print(list(zip(L,M)))

#compain two list as dic

L=[1,2,3,4]
M = ['enas','E','R','C']
for i,n in zip(L,M):
  print(str(i)+"is"+str(n)+"ok")
