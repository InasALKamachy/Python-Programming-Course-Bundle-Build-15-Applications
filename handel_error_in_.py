#error handling in python
try:
    x = int(input("number_"))
    y = int(input("number1_"))
    print(x/y)
except:ZeroDivisionError:
print("not zero ")
except:ValueError:
print("just type INterger value")
except:
   print("something error")

