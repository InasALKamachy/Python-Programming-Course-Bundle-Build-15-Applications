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
  

##Q3

try:
   # do something


   print(isinstance(x, (int, float, str)))
   pass

except ValueError:
   # handle ValueError exception
   print("ValueError")
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   print("typeError, zeroo")
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   print("not int not str not float")
   pass
  
 #Q4

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#Q5 
def lst(x):
   y = set(x)
   print(list(y))
   
L = [1,1,1,3,4,5,6]
lst(L)


Object Oriented Program
#Q1
class Bird():
   def __init__(self, name, color, weight):
      self.name = name
      self.color = color
      self.weight = weight
   def fly(self):
      print("fly")
   def flap_wings(self):
      print("flap_wing")
   def chirp(self):
      print("chirp")
      
  #Q2
  


