import all module
import re
my_regex = re.compile("[0-9] + ", re.I)
print(my_regex)

# if in your code there is a class re you can add alias
import re as regex
myregex1 = regex.compile("[0-9] + ", regex.I)


# importing explicitly when methods are needed
from collections import defaultdict, Counter
lookup = defaultdict(int) # dict subclass that calls a factory function to supply missing values
my_counter = Counter() #dict subclass for counting hashable objects

print(-5 / 2) # -2.5
print(-5 // 2) # -3

# function
def double(x):
    """
    Define a function operation
    """
    return x * 2

""" Python allow assign function to the variables, 
and passing them to other functions as arguments """

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)
print(x)

# short anonymous function
y = apply_to_one(lambda x : x + 4) # equals 5

# lambda can assign to variables:
# another_double = lambda x : 2 * x  # don't to that
def another_double(x):  return 2 * x # do like that
