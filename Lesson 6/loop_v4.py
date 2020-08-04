# big_number = -999999999
# i = 0
# while True:
#     number = int(input('Enter a number: '))
#     if number == -1:
#             break
#     elif number > big_number:
#         big_number = number
        

big_number = -999999999
i = 0
number = int(input('Enter a number: '))
while number != -1:
    if number == -1:
        continue
    i += 1
    if number > big_number:
        big_number = number
    number = int(input('Enter a number: '))
print('Big number = ', big_number)