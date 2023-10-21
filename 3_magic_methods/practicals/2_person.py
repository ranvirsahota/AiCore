# 1. Create a class called Person

# 2. Define its initialiser
    # It must take in a name, a date_of_birth in ISO format (YYYY-MM-DD) and a list of friends
    # It should initialise attributes for each of those. Be careful, don't use a default value for 'freinds!'
    # This will cause problems whenever you initialise a new instance of the class. To know more about, take a look at this:
    # https://stackoverflow.com/questions/19497879/using-a-empty-list-as-default-parameter-in-init-why-the-list-in-all-instanc

# 3. Instantiate your class and test that it works before continuing - do this for every section going forward

# 4. Define the __str__ magic method which returns a string representation of the person, detailing their name, DOB and number of freinds

# 5. Define the __gt__ magic method that defines how to use the greater than sign to compare the age of two people
#   (hint: compare the DOB of the two people)

# 6. Create a method called add_freind which take in another instance of the person class and adds it to this instance's freinds attribute.
# Assume that every relationship goes both ways: this mehotd should append each freinds to the other's list in just one call

import datetime

class Person:
    def __init__(self, name, date_of_birth, friends) -> None:
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends

    def __str__(self) -> str:
        friends_list_formatted = ', '.join(self.friends)
        return f'Name: {self.name}\nDOB(YYYY-MM-DD): {self.date_of_birth}\nFriends: {friends_list_formatted}'
    
    def __gt__(self, other_persons_date_of_birth):
        print('gt')
        return other_persons_date_of_birth > self.date_of_birth

person_1 = Person('Geralt', datetime.date(1160, 12, 12), ['Dandelion', 'Vesemir', 'Keria', 'Roach', 'Eskel'])
print(person_1.name)
print(person_1)

person_2 = Person('Vesemir', datetime.date(1120, 12, 12), ['Students'])
print(person_2)
print('Vesemir is older than Geralt:', person_1 > person_2)
