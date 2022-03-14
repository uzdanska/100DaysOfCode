# function
from email import message


def double(x):
    # this function multiplies the passed value (x) by 2
    return x * 2

# python allows you to assign functions to variables and pass to other functions as arguments
def apply_to_one(f):
    # calls functions with the argument 1
    return f(1)

my_double = double # reference to an earlier function
x = apply_to_one(my_double)
print(x)

# creating short anonymous functions with lambda
y = apply_to_one(lambda x : x + 4) # adding to the given value 4
print(y)

# function parameters can be given default values. Such values ​​are passed to the function only if they have a value other than the default:
def my_print(message= 'default message'):
    return message

print(my_print())
print(my_print('Hello'))

# definiowanie argumentów funkcji
def subtract(a = 0, b = 0):
    return a - b

print(subtract(35, 5))
print(subtract()) 
print(subtract(b = 10))