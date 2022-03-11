dict = { 'horror': 'Sepperation',
        'comedy': 'Red Notice', 
        'thriller': 'The Guilty'}
###### method of the class dict #######
# # dict.get(key) - return the value for the given key, if the key is not in the dict return None
print(dict.get('horror'))
print(dict.get('thriller'))

# # dict.has_key(key) - return True if the key is in the dict if not return False
# dict.has_key('sd') #### only with Python2

# # dict.items() - return the list two-element tuples (key, value)
print(dict.items())

# # dict.keys() - return list all od the keys
print(dict.keys())

# # dict.values() - return the list all of the values
print(dict.values())

# # dict.clear() - removes all keys from the dict dictionary
#   dict.clear()
#   print(dict)


del dict['horror'] # remove they key 'horror' from the dictionary dict
print(dict)
keys = dict.keys()
print(keys) # the horror is not there because od the del

l = len(keys) # len return the value of length of keys right here
print(l)
print(len(dict))
