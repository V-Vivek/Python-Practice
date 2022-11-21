# Map is used to apply some logic(function) to each item of an input iterable
# As a result it produces the map object.
# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
# Syntax: map(fun, iter)
  # fun : It is a function to which map passes each element of given iterable.
  # iter : It is a iterable which is to be mapped.

# ==================================================================================================
# Problem 1: Write a program to get the square of each item in a list

#Method 1: Without using map()
lst = [1, 2, 3, 4, 5]
result =[]
for i in lst:
  result.append(i*i)
print(result)
  
#Method 2: Using map()
lst = [1, 2, 3, 4, 5]
result = map(lambda x : x*x, lst) # map() is used to iterate through each item of list
print(list(result))
# ==================================================================================================

# map() can take any number of iterables as inputs.

# ==================================================================================================
# Problem 2: Write a function to add sequential elements of two lists
#Method 1: Without using map()
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
result =[]
for i in range(len(lst1)):
  result.append(lst1[i]+lst2[i])
print(result)
  
#Method 2: Using map()
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
result = map(lambda x,y : x+y, lst1, lst2) # map() is used to iterate through each item of list
print(list(result))
# ==================================================================================================
