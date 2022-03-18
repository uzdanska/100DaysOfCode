import random
numberI = 0
numberR = random.randint(1, 50)
# print(numberR)

while numberI != numberR:
    numberI = int(input('Guess the number: '))
    if numberI == numberR:
        print('You guess the number.')
        break
    elif numberI >= numberR:
        print('Try to guess the small number.')
        continue
    else:
        print('Try to guess the large number.')
        continue