a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
d = int(input('Enter number 3: '))
s = (a + b + d)/3
s = int(s)

r = int(input('The largest number(0)  or  The smallest number(1)  or  Arithmetic mean(2): '))

if r == 0:
    if a > b:
        if a > d:
            print(a)
        else:
            print(d)
    else:
        if b > d:
            print(b)
        else:
            print(d)

elif r == 1:
    if a < b:
        if a < d:
            print(a)
        else:
            print(d)
    else:
        if b < d:
            print(b)
        else:
            print(d)

else:
    print(s)
