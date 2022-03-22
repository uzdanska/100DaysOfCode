"""A generator is something you can iterate over (in our case it usually will
that's about the for loop. Generator values ​​are only created when needed """

# # # Generator create using a function,and  an operator yield

def lazy_range(n):
    """ Simples way of range function """
    i = 0
    while i < n:
        yield i
        i += i

# for i in lazy_range(10):
#     ## function name (i)

lazy_events_below_15 = {i for i in lazy_range(15) if i % 2 == 0}
print(lazy_events_below_15)
