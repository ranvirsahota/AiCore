class Phone():
    def __init__(self, number, balance = 20):
        self.number = number
        self.balance = balance

    def make_call(self, number, duration = 1):
        if self.balance >= duration:
            print(f'Calling {number} for {duration}')
            self.balance -= duration
        else:
            print('Insufficent balance')

    def info(self):
        print('Phone Number: ', self.number)
        print('Balance: ', self.balance)


my_phone = Phone(number = '0666666664', balance = 60)
my_phone.info()
my_phone.make_call('3333333333', 33)
