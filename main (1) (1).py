#Leap year

"""
Year\4==0
year\100

"""
def isLeapyear(year):
 if (year%4==0 and year%100!=0)or year%400==0:
    return True
 else:
    return False
  
year=int(input("enter the year:"))

if isLeapyear(year):
  print('{}is a leapyear.'.format(year)) 
else:
  print('{}is not a leapyear.'.format(year))
  


