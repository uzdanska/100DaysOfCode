###### dictionary #####

# empty dictionary:
dict_empty = dict()
print(dict_empty) # {}
print(type(dict_empty)) # type(x) - type of element x, here is <class 'dict'>

# dict = { key1: valueKey1, key2: valueKey2}

# # # create a dictionary
dict = { 'horror': 'Sepperation',
        'comedy': 'Red Notice', 
        'thriller': 'The Guilty'}

print(dict)

programmingLan = {
  'front end': ['HTML', 'CSS', 'JavaScript'],
  'back end': ['Ruby', 'Python', 'PHP']
}
print(programmingLan)

##### element references #####
print(programmingLan['front end'])
print(programmingLan['front end'][2])
print(programmingLan['back end'])
print(programmingLan['back end'][1])