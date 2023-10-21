#Create a list of 10 strings then create the following lambda functions:
games = [
    'Elden Ring', 'Mass Effect Legendary', 'Survival', 'Little Nightmare', 'Inside',
    'Alan Wake', 'DS', 'Alien', 'XCOM', 'CIV'
    ]
# 1. A lambda function that takes in a string and returns True if the string is longer than 5 characters, and False if it is not. 
is_longer_five_char = lambda x: True if len(x) > 5 else False
# Then use filter and the lambda function to filter out all strings that are longer than 5 characters.
print('All strings from list \'games\' longer than five characters: ', list(filter(is_longer_five_char, games)))

# 2. A lambda function that takes in a string and returns True if the string is longer than 5 characters and starts with a vowel, and False if it is not.
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
is_longer_five_char_and_vowel = lambda x: True if is_longer_five_char(x) and x[0].lower() in vowels else False

# Then use filter and the lambda function to filter out all strings that are longer than 5 characters and start with a vowel.
print('All strings from list \'games\' longer than five characters and start with a vowel', list(filter(is_longer_five_char_and_vowel, games)))