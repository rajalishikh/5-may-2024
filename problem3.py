# find the which number is largest in 4 value 
a=int(input('Enter the value of a ')) 
b=int(input('Enter the value of b '))
c=int(input( 'Enter the value of c '))
d=int(input('Enter the value of d '))
if (a>b and a>c and a>d):
    print("a is a largest number ")
elif(b>a and b>c and b>d):
    print('b is largest number ')
elif(c>a and c>b and c>d):
    print('c is largest number ')
else:
    print('d is largest number ')
    