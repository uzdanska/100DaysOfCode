##### Tuple is a non changing list
## Tuple define in () or without anything like in line 4
my_list = [0, 2]
my_tuple = (0, 2)
different_tuple = 3, 4

print('\n###################\n')

print('List:')
print('type(my_tuple) =  '.format(type(my_list)))

print('\n###################\n')

for i in range(len(my_list)):
    print(my_list[i])

print('\n###################\n')

print('Tuple:')
print(type(my_tuple))

print('\n###################\n')

for i in range(len(my_tuple)):
    print(my_tuple[i])

print('\n###################\n')

print('Different tuple:')
print('type(different_tuple) = {}'.format(type(different_tuple)))

print('\n###################\n')

for i in range(len(different_tuple)):
    print(different_tuple[i])

# trying to change a tuple
try: 
    my_tuple[1] = 3
except:
    print(' you can\'t change a tuple')

print('\n###################\n')

#### Tuples are easy return from function

def sum_and_product(x, y):
    return (x / y), (x ** y)
    
sp = sum_and_product(3, 2)
print(sp)


s, p = sum_and_product(3, 2)
print(s)
print(p)

