# A lambda function is a small anonymous(unnamed) function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax : lambda arguments : expression

# ==================================================================================================
# Problem 1: Write a program to add 10 to input number
x = lambda a : a + 10
print(x(5))
# ==================================================================================================

# ==================================================================================================
# Problem 2: Write a program to get max between 2 numbers
max = lambda x,y : x if x>y else y
print(max(5, 10))
# ==================================================================================================
