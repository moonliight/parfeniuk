big_number = -999999999

number = int(input('Enter a number or -1 to close program: '))

while number != -1:
    if number > big_number:
        big_number = number
    number = int(input('Enter a number or -1 to close program: '))

print('The baggest num: ' , big_number)