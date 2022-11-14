# This is a non-keyed argument
def func1(*vivek):
	'''You can pass any number of arguments to this function'''
	for v in vivek:
		print(v)

func1('Hi', 'This', 'is', 'Vivek', 1, 2, 3)
