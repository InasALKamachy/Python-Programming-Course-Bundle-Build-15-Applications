class ZeroCuError(Exception):
    '''zero can\'t be zero'''


class Cube():
    def __init__(self, num):
        num = int(num)
        if (num!= 0):
            self.qud = num**3
        else:
           raise ZeroCuError



try:
    num1 = Cube(input("Number_"))
    num2 = Cube(input("Number_"))

except:
    ZeroCuError
    print(ZeroCuError.__doc__)

else:
    print("The number1 : "+str(num1.qud))
    print("The number2 : " + str(num2.qud))

