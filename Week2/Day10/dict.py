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

## if you ask about key, which is not is the dict, it will generate a error key
try:
    annaBooksInTheLibrary = booksInTheLibrary['Anna']
except KeyError:
    print('Anna is not in the dictionary')

## you check if the key exist
adaBooks = 'Ada' in booksInTheLibrary
print(adaBooks)
annaBooks = 'Anna' in booksInTheLibrary
print(annaBooks)

## the dict has a method get, which return a default value
adaBooks = booksInTheLibrary.get('Ada', 0)
print(adaBooks) # return 3
annaBooks = booksInTheLibrary.get('Anna', 1)
print(annaBooks) # return 1
noOnesBook = booksInTheLibrary.get('No One')
print(noOnesBook) # return None