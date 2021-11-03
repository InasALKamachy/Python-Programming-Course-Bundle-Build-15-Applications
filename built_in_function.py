code = 'print(sum([1,2,3,4]))' # single operation

compile_code =compile(code, '', 'eval')
print(compile_code)
eval(compile_code)

code1 = 'l=[1,2,4,54] print(sum(l))' # more than one operation

compile_code1 =compile(code1, '', 'exec')
print(compile_code1)
exec(compile_code1)

abs() # return absulute value of number
shuffle(l) # rearragnge the list 
bin() # to convert number to binary
ascii() # to return the value of special character 
callback() # to cheack wheather the function could be call or not
all() # return False if one of elemenet is false of list = [1,2,0]
any() # return True if any of list is true


=================
class Number():
    def __init__(self,value, str):
        self.va = value
        self.st = str

    def show(self):
        print(self.va, self.st)
    def p(self):
        print("This the p attribute"+str(self.va))

c = Number(2,"t")
# use del(c.value) to delete the attribute
# use delattr(object , attribute)  ==> delattr(c,value)

c.show()
c.p()
==========================================================

import fucntions
import inspect
fucntions.grting('x')
print(dir(fucntions))
print(dir(inspect))

# use dir(file_name) ==> to know all the function that file have
# use dir(module)==> to know all the methode that modeul have. 
