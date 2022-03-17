############ break - stop loop for and while
############ continue - can skip the statement block lower and back to the lock
import random

#### Example 1:
## print the variables 0 1 2 3 4

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
meter = 0
while meter in list:
    print('list[{}] = {}'.format(meter, list[meter]))
    meter += 1 # meter = meter + 1
    if meter >= 5:
        break

print('\n############\n')

#### Example 2:
## print only odd number
x = random.sample(range(100), 10)
# print(type(x))

for i in range(len(x)):
    if x[i] % 2 == 0:
        continue
    print('x[{}] = {}'.format(i, x[i]))


