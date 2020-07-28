try:
    c = 5 / 0
except ZeroDivisionError :
    print("Ne dilumo na 0!")


try:
    x = int(input('Enter a nuumber: '))
    y = 1 / x
    print(y)
except ValueError:
    print('U need to enter a number!')
except:
    print('Somethig was wrong!')