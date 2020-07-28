m = int(input('Enter meters: '))
sm = m*100
mm = m*1000
km = m/1000

r = int(input('sm(0)  or  mm(1)  or  km(2)?: '))

if r == 0:
    print(sm)
elif r == 1:
    print(mm)
else:
    print(km)