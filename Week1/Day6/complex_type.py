##### complex type (set) #####

list = [1, 6, 3, 9, 10, 23]
a = set(list)
b = set([2, 5, 1, 6, 8, 2])

##### new set containing common items from set a and b
print(a & b) # 1 way
print(a.intersection(b)) # 2 way

###### new set containing items from set a and b
print(a | b) # 1 way
print(a.union(b))

###### new set containing items from set a with exclusion set b
print(a - b) # 1 way
print(a.difference(b)) # 2 way

####### new set containing items belonging to one set a or b
print(a ^ b) # 1 way
print(a.symmetric_difference(b)) # 2 way

#### new set, a copy from set a
print(a.copy())
#### new set, a copy from set b
print(b.copy())

##### return set a after remove items, which do not apear in set b
print(a.intersection_update(b))

#### return set s after remove items which apear in set a
print(a.difference_update(b))

##### return set a after filling it with elements belonging to exactly one of the sets a or b
print(a.symmetric_difference_update(b))

##### add item x to set a
a.add(4)
print(a)

##### remove item x from the set s
a.remove(2)
print(a)

######remove item x from the set s, if it appears in it
a.discard(4)
print(a)

###### remove and return chosen items from set a
print(a.pop())
print(a)

###### add to set a item from set b
a.update(b)
print(a)

##### remove from set a all item
a.clear()
print(a)