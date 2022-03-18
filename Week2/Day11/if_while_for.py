############  if
"""
age = input('How old are you? \n')

if int(age) >= 18:
    print('You are adult')
elif int(age) < 18 and int(age) > 10:
    print('You are teenager')
elif int(age) <= 10:
    print('You are child')

# one line statements:

print('You are adult') if int(age) >= 18 else print('You are child') 

"""

########### while

x = 113
p = 7
while x % p != 0:
    print('{} mod ({}) = {}'.format(x, p, x % p))
    x += 1

print('\n################\n')
######### for
for i in range(p):
    print(i, 'mniejsze od ', p)

print('\n################\n')
for i in range(2, 10):
    if i % p != 0:
        print('{} mod({}) = {}'.format(i, p , i % p))
        continue
    if i % p == 0:
        break


