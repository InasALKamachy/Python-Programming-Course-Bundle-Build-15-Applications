##Q1 -
lst = [10,30,55]
if sum(lst)!=100:
  for i in lst:
    print(lst.append(i))
    print(lst)
    break
else:
  print(lst)
  
  
##Q2 
degree_ = [65,80,33]
student_ = ['S1_marks', 'S2_marks', 'S3_marks']


for i, j in list(zip(degree_, student_)):
  print(j + '=' +str(i))
for i in degree_:
  if i >=80:
    print('Ist division')
  elif i>=60:
    print('IIst division')
  elif i>=33:
    print('III division')
  else:
    print('Failed')

 ## Q3
c= True
d = False

a = 5
b = 5.0
if a==b:
  print(c)
else:
  print(d)
  
 ##Q4
nothing wrong

##Q5
$$ and if tru && tur ===> true, True && False ==> False
|| or  if True || True ==> True, True || False ==> True

##Q1
While Looop
l = [11,12,13,14,15]

i=True
while i ==True:
  for j in l:
    print(pow(j,2))
 
  break


##Q2
j = []
for i in range(11):

  if i!=3 & i!=7:
    
    j.append(i)
print(j)

##For Loop
#Q1
L = [12,22,56]
Max = 0
for i in L:
  
  if i > Max:
    Max = i
print(Max)

#Q2

from random import *
def shu(l):
    '''This function is used to shuffle the value
    Coding: shuffle(l)'''
    shuffle(l)
    print(l)
N = ['a','b','c']
shu(N)

#Q3
lst = [1,2,44,55,6]
sum = 0
for i in lst:
  sum+=i
print(sum)

#Q4
lst = ['C#','C==', 'Python','Java']
ex = False
num_ex = 0
for i in lst:
  if i =='C#':

    ex = True
    print(ex)
    num_ex +=1
  else:
   ex = False
   print(ex)
    
Function
#Q1

def greeting():
  x = input("Enter your name: ")
  print("Hello "+x)

greeting()
  

##Q7


