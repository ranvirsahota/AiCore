print('hello world')

print('__name__ in original file: ', __name__ )

# the if statement will prevent the execution of this code inside unless it is ran directly, i.e from terminal
# '__name__' is bultin keyword from python 
if __name__ == '__main__':
    print('Inside the if __name__ == __main__ block')