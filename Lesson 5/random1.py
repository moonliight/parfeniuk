# import random
# print(dir(random))


# from random import random
# for i in range(10):
#     print(str(i) + ". " + str(random()))


# from random import randrange, randint
# print(randrange(0, 12, 2), end=' ')
# print(randint(0, 13))


from random import choice, sample
lst = [1,2,3,4,5,6]
print(choice(lst))
print(sample(lst, 3))





