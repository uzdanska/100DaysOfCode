##### DEFINE LIST #####
list = ['John', 'Peter', 'Adam', 'Anna']
##### methods for the list ##### 
# # # append(x) - add element to the end of list
list.append('Mary')
print('Now list look like: ',list)

# # # extend(x) - expands the list by including all elements of the given x-list,
list.extend('Gary')
print('Now list look like: ',list)
print('Elements of the list belonging to a compartment [5; 9]: ', list[5:9])

# # # insert(i , x) - add element x on i position list
list.insert(2, 'Madison')
print('The secend element of the list is now: ',list[2])
print(list)

# # # remove(x) - remove the first element from list, which is equal to x
list.remove('Peter')
print('List after remove the "Peter": ',list)

# # # pop([i]) - remove the element from a given item in the list i and return their element
list.pop(1)
print(list)

# # # index(x) - return index first element of list, which value is x
print('Index "Adam": ', list.index('Adam'))
print('Index "Mary": ',list.index('Mary'))

# # # count(x) - return the numbers element x instances 
print('"Anna" count is: ',list.count('Anna'))

# # # sort() - sorts the items in the list itself
numbers = [1, -2, 3, 20, 1 , 100, -10]
# ascending
numbers.sort()
print(numbers)

# # # reverse() - reverses the order of the list items
# descending
numbers.sort(reverse = True)
print(numbers)

####### merge list ####
list2 = ['Linda', 'Emily', 'Lily']

merge_list = list + list2
print(merge_list)
