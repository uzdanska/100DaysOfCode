##### assigning many new variables on one line
a, b, c = 1, 'Dog', 1 +20

##### print variables

print(a, b, c)
print('a = ', a, '; b = ', b, '; c = ', c)

# str convert number to a string
print('a = ' + str(a) + ', b = ' + ', c = ' + str(c))

print('a = {}; b = {}; c = {}'.format(a, b, c))

###### Importing packages / libraries in Python
# 1 way:

import math # import all functions and methods available in the math library
x = 60 * math.pi / 180
print('60 * math.pi /180) = ', round(math.sin(x), 3)) # round a number to only 3 decimals

# 2 way:
from math import pi, sin
x = 60 * pi / 180
print('60 * math.pi /180) = ', round(sin(x), 5)) # round a number to only 5 decimals
