from math import pi, sin

print(sin(pi/2))

def sin(x):
    return 1
    
print(sin(pi/2))

# або імпортуємо мінус і переназиваємо його

from math import sin as sinus, pi
print(sinus(pi/2))