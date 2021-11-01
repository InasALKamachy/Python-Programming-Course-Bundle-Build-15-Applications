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
