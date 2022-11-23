# Permutation using List comprehension

# Use space separated multiple list comprehensions
permutation = [[i,j,k] for k in range(3) for i in range(3) for j in range(3)]
print(permutation)
