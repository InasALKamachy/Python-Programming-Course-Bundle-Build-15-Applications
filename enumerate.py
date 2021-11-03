#enumerate print the index to print as tuple
L = ['E','b','c','d']
x = enumerate(L)
print(list(x))
# to print as index and value
for ind,lan in enumerate(L, start=1): # make the index begin with i as value
    print(ind, ':', lan)
