"""
A list is a collection of consecutive items
objects in another language are referred to as arrays
"""

int_list = [2, 5, 9]

len_int_list = len(int_list)
print('List length = {}'.format(len_int_list))
print('List values are: ')
for i in range(len(int_list)):
    print('int_list[{}] = {}'.format(i, int_list[i]))

# pierwszy sposób
suma = 0
print('The sum of the list values')
for i in range(len(int_list)):
    suma = suma+ int_list[i] 
    print('Sum in {} iteration is = {}'.format(i, suma))

# drugi sposób
# lista_suma = sum(int_list)
# print(lista_suma)

print('\n###################\n')

wszystkie_wartosci_list = ["string", 0.1, True]
len_wszystkie_wartosci_list = len(wszystkie_wartosci_list)
print('List length= {}'.format(len_wszystkie_wartosci_list))
for i in range(len(wszystkie_wartosci_list)):
    print('wszystkie_wartosci_list[{}] = {}'.format(i, wszystkie_wartosci_list[i]))

print('\n###################\n')

lista_listy = [ int_list, wszystkie_wartosci_list, []]
len_lista_listy = len(lista_listy)
print('List length = {}'.format(len_lista_listy))
# print(len(lista_listy))
for i in range(len(lista_listy)):
    print('lista_listy[{}] = {}'.format(i, lista_listy[i]))

print('\n###################\n')
print('List_list sublist: ')
for i in range(len(lista_listy)):
    for j in range(len(lista_listy[i])):
        print('lista_listy[{}][{}] = {}'.format(i, j , lista_listy[i][j]))

print('\n###################\n')

x = range(15) # values [0, 1, ...., 14]
lista = []
lista[: 5] = [2, -3, 6, 9, 2] # first 5 values
lista[5:9] = [-80, 23, 55, 2] # values from 5 to 8
lista[-1:] = [-5, -9, 112] # last 5 values

for i in range(len(lista)):
    lista[:5] = [2, -3, 6, 9, 2] # pierwsze 5 wartosci
    lista[5:9] = [-80, 23, 55, 2] # wartości od 6 do 9
    lista[-3:] = [-5, -9, 112] 
    print('lista[{}] = {}'.format(i, lista[i]))