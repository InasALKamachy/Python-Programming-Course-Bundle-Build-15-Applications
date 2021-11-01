from random import *

def cho(l):
    '''This fucntion is used to choice N values form the list
    coding: sample(l)'''
    print(sample(l,2))

print(help(cho))
L = [1,2,3,4]
N = ['a','b','c']
seed = 7 # '''The seed() method is used to initialize the random number generator.The random number generator needs a number to start with (a seed value), to be able to generate a random number. '''
cho(L)
cho(N)
