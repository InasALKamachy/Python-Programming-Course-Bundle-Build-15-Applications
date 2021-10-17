Str1 = 'Desserts'
Str2 = "Live" 
Str3 = 'Pals'
Str4 = 'God'
Str5 = 'Raw'
#word:reverse
dic = [Str1,Str2,Str3,Str4,Str5]

# for i in dic:
#   i.lower()
#   print(i,':',i[::-1].capitalize())
def str_rev(l):
  for i in dic:
    i.lower()
    print(i, ':', i[::-1].capitalize())

print(str_rev(dic))


******************************************************
Str1 = 'Desserts'
Str2 = "Live" 
Str3 = 'Pals'
Str4 = 'God'
Str5 = 'Raw'

lst = [Str1, Str2, Str3, Str4, Str5]
 
# the function
def str_rev(stm):
    # reversing the passed string
    rev_str = stm.lower()[::-1]
    # returning the string with the original
    return f"{stm} : {rev_str.capitalize()}"
    
# using for loop to pass the string literals to the function
for l in lst:
    Str = str_rev(l)
    print(Str)

