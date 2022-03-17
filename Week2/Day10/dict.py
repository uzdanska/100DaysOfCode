""" dictionary is another basic data structure. 
This structure assigns values to the keys 
and allows you to quickly read the value 
based on the key. """

empty_dict = () # frist way to create a dictionary
empty_dict2 = dict() # second way to create a dictionary 

booksInTheLibrary = {'Ada' : 3, 'Kasia': 2, 'Ula': 4}

#### to read the value assigned to the key 
AdaBooksInTheLibrary = booksInTheLibrary['Ada']
print(AdaBooksInTheLibrary)

print('\n############\n')

## if you ask about key, which is not is the dict, it will generate a error key
try:
    annaBooksInTheLibrary = booksInTheLibrary['Anna']
except KeyError:
    print('Anna is not in the dictionary')

print('\n############\n')

## you check if the key exist
adaBooks = 'Ada' in booksInTheLibrary
print(adaBooks)

print('\n############\n')

annaBooks = 'Anna' in booksInTheLibrary
print(annaBooks)

print('\n############\n')

## the dict has a method get, which return a default value
adaBooks = booksInTheLibrary.get('Ada', 0)
print(adaBooks) # return 3

print('\n############\n')

annaBooks = booksInTheLibrary.get('Anna', 1)
print(annaBooks) # return 1

print('\n############\n')

noOnesBook = booksInTheLibrary.get('No One')
print(noOnesBook) # return None

print('\n############\n')

booksInTheLibrary['Ada'] = 10 # now Ada has 10 book in the library
booksInTheLibrary['Marta'] = 1 # adding new element to booksInTheLibary

print(booksInTheLibrary)

num_person = len(booksInTheLibrary)

print('\n############\n')

print('Person in Library = {}'.format(num_person))

# print('\n############\n')

instagram = {
    'name': 'anna_male',
    'followers': '1257',
    'hastags': ['#travel', '#ootd', '#photo']
}

### the dict allow you to have a look at all the keys
insta_keys = instagram.keys() ## list of 
insta_values = instagram.values() ## list of values
insta_items = instagram.items() ## list tuples (keys, values)

print(insta_keys)

print('\n############\n')

print(insta_values)

print('\n############\n')


# 'name' in instagram ## check if 'name' is in the dict insta
if 'anna_male' in insta_values:
    print('The user {} is in the instagram.'.format(instagram['name']))
    print('{} has a {} followers and using this person using hashtags like {}'.format(instagram['name'], instagram['followers'], instagram['hastags']))