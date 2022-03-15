from Week2.Day8.list import lista
# # check if the number belongs to the list
print(1 in lista)
print(2 in lista)
print(3 in [3, 2, 5, 1])
print(2 in [1, 5, 7, -2])
# in operator check every number in sequence so , if the list is short is okay to use it, 
# but when the list is long, time the working time may be extended

print('\n###################\n')

### connecting 2 list
x = [2, 5, 1]
x.extend([3, 6, 8])
for i in range(len(x)):
    print('x[{}] = {}'.format(i, x[i]))

print('\n###################\n')

# unzip a list
print(type(lista)) # lista is list
print(type(x)) # x is a list
lista, x = [lista[0], x[2]] # lista = lista[0] and x = x[2]
print(lista)

print(type(lista)) # now lista is a int
print(type(x)) # now x is a int

print('\n###################\n')

# If you don't need a value, you can replace it with an underscore (_):
x1 = [2, 3, 4, 1]
_, x1 = [1, 'HIII']
print(type(x1)) # now x1 is a string
print(x1)