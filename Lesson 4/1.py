a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
d = int(input('Enter number 3: '))
s = a+b+d
c = a*b*d

r = int(input('Sum(1) or Composition?(0) : '))

if r == 1:
    print(s)
elif r == 0:
    print(c)
