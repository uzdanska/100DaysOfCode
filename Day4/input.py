###### Communication with the user, loading data from the console
name = input('Enter your name: ')
age = input('Enter your age: ')

print("Hi, I'm {}. I'm {} years old.".format(name, age))


##### 2:
# input from user is always is a string
side1triangle = input('Enter first side of triangle: ')
side2triangle = input('Enter second side of the triangle: ')
side3triangle = input('Enter third side of the triangle: ')

try:
  # The try block lets you test a block of code for errors.
  float(side1triangle) # check if it possible to convert to float 
  float(side2triangle)
  float(side3triangle)
except:
  # The except block lets you handle the error.
  print('Enter value again: ')
  side1triangle = input('Enter first side of triangle: ')
  side2triangle = input('Enter second side of the triangle: ')
  side3triangle = input('Enter third side of the triangle: ')

# the condition for the existence of a triangle
  
if float(side1triangle) + float(side2triangle) > float(side3triangle):
  if float(side1triangle) + float(side3triangle) > float(side2triangle):
    if float(side2triangle) + float(side3triangle) > float(side1triangle):
      print('The condition for the existence of a triangle has been met')
else:
  print('the condition for the existence of a triangle has not been met')