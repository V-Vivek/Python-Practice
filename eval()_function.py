# eval() takes string as input and evaluates it as a Python expression
expr = "x**2 + 2*x + 3"
x = 4
print(eval(expr))

# We can use eval along with input() function to directly typecast the input data in required datatype

# Get List from user
lst = eval(input('Enter list elements along with [] : '))
print(lst)

# Get Tuple from user
tup = eval(input('Enter , separated Tuple elements : '))
print(tup)

# Get Set from user
s = eval(input('Enter set elements along with {} : '))
print(s)
