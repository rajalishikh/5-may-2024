# find the leap year 
year=int(input('Enter your year:  '))
if(year%400 == 0):
    print('It is a leap year ')

elif(year%4==0 and year%100 != 0):
    print('it is leap year ')
else:
    print('it is a not leap year ')