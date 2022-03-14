#  Python generates exceptions, if they are not handled, they will crash the program.
a  = int(input("Enter the first value: "))
b =  int(input("Enter the second value: "))
try:
    print(a / b)
except ZeroDivisionError:
    print("You cannot divide by zero")