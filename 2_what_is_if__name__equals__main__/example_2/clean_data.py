def clean_data(data):
    #clean data
    return data

# if this file were to be imported WITHOUT the if statement AND clean_data is called in the file importing it
# 'clean_data' will be called twice, becuase import statement will execute everythiing inside global space of a file
if __name__ == '__main__':
    clean_data('my_data')