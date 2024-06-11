# here we can find which is rectangle or square 
a=int(input('Give me First  length of a: '))
b=int(input('Give me second length of b: '))
c=int(input('Give me Third  length of c: '))
d=int(input('Give me Fourth length of d: '))

if(a==b and a==c and a ==d  and b == c and b ==d and c==d ):
    print('It is a square ')
elif( a== c and b== d):
    print('Its a rectangle ')
else:
    print('This is nothing ')