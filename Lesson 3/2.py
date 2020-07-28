number = int(input('Enter your number:'))
a = number % 10
b = (number//10) % 10
c = (number//100) % 10
d = number//1000
print(a*b*c*d)