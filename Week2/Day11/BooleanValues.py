######### Bolean values
OneIsLessThanTwo = 1 < 2
TrueEqualsFalse = True == False

print(OneIsLessThanTwo)
print(TrueEqualsFalse)

# None - non-existent value
a = None
print(a == None)
print(a is None)
print(a is not None)

##### This is a few elements that Python treat as "false":
### * False,
### * None,
### * [] (empthy list)
### * {} (empthy dict)
### * "",
### * set()
### 0,
### 0.0

#### check if a string is empty return "" or is not empty return first_char
string = input('Enter a string: ')
# if string:
#     first_char = string[0]
#     print(first_char)
# else:
#     first_char = ""
#     print(first_char)

#### second way on one line
## and return second value if the first is "true"
first_char = string and string[0]
print(first_char)