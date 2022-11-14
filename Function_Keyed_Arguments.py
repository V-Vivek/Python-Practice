# This is a keyed argument function
def func1(**vivek): # ** is used for keyed argument
    '''User can enter any no. of arguments in any sequence in the form of key-value pair'''
    for k,v in vivek.items():
        print(f'Key : {k} Value : {v}')

func1(name = 'Vivek', age = 23, city = 'Pune') # Note that no need to write key name in string format. Seperate key & value using = operator
