from datetime import *
Time = datetime.now()
# print(Time.day)
# print(Time.year)
# print(Time.month)
print(Time.today())
To = date.today()
print(To) # print without hours
birth = datetime(year = 1982, month = 8, day=9,hour =12,minute=15,second=12)
full_birth = Time - birth
print(full_birth/360)
