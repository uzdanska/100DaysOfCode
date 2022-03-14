# how for works
for i in [1, 2, 3, 4, 5]:
    print("row: {}".format(i))
    for j in [1, 2, 3, 4, 5]:
        print("column: {}".format(j))
        print("sum: {}".format(i + j))
    print(i)
print("finish for")

# The python ignores whitespace in square () and square brackets {}

long_operation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)
print(long_operation)

list =  [   [1, 2, 3], 
            [2, 3, 4], 
            [5, 6, 7]   ]
    
# \ - the next instruction is on the next line,
two_plus_three = 2 + \
                 3

print(two_plus_three)
