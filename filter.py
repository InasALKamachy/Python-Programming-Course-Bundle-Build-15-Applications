# functions.py
def even(num):
    if num % 2 ==0:
        return True
    else:
        return False
#main.py
# use filter with (function, list)
L1 = [11,232,4,55,66,3,2,654,77]
filter_list = filter(fucntions.even, L1)
even_list = []
for i in filter_list:
    even_list.append(i)
print(even_list)
