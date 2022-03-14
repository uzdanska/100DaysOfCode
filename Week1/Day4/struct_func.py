####### structural vs functional
### calculate sqrt of 8
# 1 way:
p1 = 8**(1/2) # structured programming paradigm
print('sqrt of 8 = ' , round(p1, 4))

#  2 way:
from math import sqrt
p2 = sqrt(8) # functional programming paradigm
print('sqrt of 8 = ' ,round(p2, 4))

