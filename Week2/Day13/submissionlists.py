# submission of lists
even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)

squares = [x * x for x in range(6)]
print(squares)

even_squares = [ x * x for x in even_numbers]
print(even_squares)

# list to a dictionary
square_dict = { x : x * x * x for x in range(5)}
print(square_dict)
print(type(square_dict))

square_set = { x * x * x  for x in [1, -1]}
print(type(square_set))
print(square_set)

pairs = [(x, y)
            for x in range(4)
            for y in range(4)]

print(pairs)