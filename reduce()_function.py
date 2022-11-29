# reduce() is used to apply a logic/function to each element of list
# It returns single aggregated data as a result(It doesn't return list)
# NOTE : reduce() function is defined in “functools” module. It should be imported before the use of reduce.

# Syntax: reduce(fun, iter, initializer->optional)
  # fun : It is a function to which reduce passes each element of given iterable.
  # iter : It is a iterable which is to be reduced.
  # initializer : It is an optional argument used to provide the default value to reduce()
  
# Working :
# At first step, first two elements of iterable argument are picked & intermediate result is calculated.
# In next step it operates on next element of the iterable argument & intermediate result.
# This process continues till no more elements are left in the container.
# The final result is returned to caller object.

# ==================================================================================================
# Problem 1: Write a program to get the sum of list elements

#Method 1: Without using reduce()
lst = [1, 2, 3, 4, 5]
result = 0
for i in lst:
  result += i
print(result)
  
#Method 2: Using reduce()
import functools
lst = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x,y : x+y, lst)
print(result)
# Output -> 15
# ==================================================================================================

# ==================================================================================================
# Using 3rd argument of reduce()
import functools
lst = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x,y : x+y, lst, 6)
print(result)
# Output -> 21
# ==================================================================================================
