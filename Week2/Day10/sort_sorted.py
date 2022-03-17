###### method vs function
""" If having the original order of the list is unimportant, 
    then you can call the sort() function on the list. """
a = [2, 4, 7, 9, 10]
a.sort()
print(a)
print('\n############\n')

####### descending
a.sort(reverse=True)
print(a)
print('\n############\n')

""" The sorted() function will not modify the list passed as a parameter.
    If you want to sort a list but still have the original unsorted version, 
    then you would use the sorted() function. """

b = [4, 6, 10, 23, 2]
newB = sorted(b) # overwrite variables
print(newB)

print('\n############\n')

######## descending
newB2 = sorted(b, reverse=True)
print(newB2)

