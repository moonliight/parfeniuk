# number = int(input('Enter tour number: '))
# a = number % 10
# b = (number//10) % 10
# c = (number//100) % 10
# d = number//1000
# print(a,b,c,d)

number = int(input('Enter tour number: '))
a = number % 10
b = (number//10) % 10
c = (number//100) % 10
d = number//1000
r = str(a) + str(b) + str(c) + str(d)
print('Result = ', r)