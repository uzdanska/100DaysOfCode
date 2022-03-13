print("Enter numbers to set a: ")
numbersA = []
for i in range(5):
  number = input("Enter a number: ")
  try: 
    int(number)
  except:
    print("Try to add a number!")
    number = input("Enter a number: ")
  numbersA.append(int(number))
print('Set a: {}'.format(numbersA))

setA = set(numbersA)

print('Enter numbers to set b: ')
numbersB = []
for i in range(5):
  number = input("Enter a number: ")
  try: 
    int(number)
  except:
    print("Try to add a number!")
    number = input("Enter a number: ")
  numbersB.append(int(number))
  
print('Set b: {}'.format(numbersB))

setB = set(numbersB)
def Menu():
  print('\n########################')
  print('Menu: ')
  print('1: Common part of both sets')
  print('2: Values of the set a and set b')
  print('3: Items from set a with exclusion set b')
  print('4: Items from set b with exclusion set a')
  print('5: Items belonging to one set a or b')
  print('########################\n')
i = 0
while i < 5:
  choice = input('Choose a number from the interval [1, 5]: ')
  
  if int(choice) == 1:
    print(setA & setB)
    i = i + 1
    if i != 5:
      Menu()
  elif int(choice) == 2:
    print(setA | setB)
    i = i + 1
    if i != 5:
      Menu()
  elif int(choice) == 3:
    print(setA - setB)
    i = i + 1
    if i != 5:
      Menu()
  elif int(choice) == 4:
    print(setB - setA)
    i = i + 1
    if i != 5:
      Menu()
  elif int(choice) == 5:
    print(setA ^ setB)
    i = i + 1
    if i != 5:
      Menu()
  else:
    if i != 5:
      print("Wrong number")
