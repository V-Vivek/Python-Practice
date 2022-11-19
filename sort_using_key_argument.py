# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison

# Sort with custom function using key
# If you want your own implementation for sorting, the sort() method also accepts a key function as an optional parameter.
# Based on the results of the key function, you can sort the given list.

# =======================================================================================
# Problem statement:
# To sort a list of tuples using 2nd item of tuple

lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)]

# Custom function used by key argument
def second_item(tup):
    return tup[1]

lst.sort(key=second_item)
print(lst)
# Output -> [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# =======================================================================================
