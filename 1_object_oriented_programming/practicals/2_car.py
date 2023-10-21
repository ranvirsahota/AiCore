class Car():
    def __init__(self, model, year = 2023):
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self):
        self.miles_driven += 1
        print('vroom')

    def info(self):
        print(f'Miles Driven: {self.miles_driven} miles')
        print('Model: ', self.model)
        print('Year: ', self.year)


no_name = Car(model = 'No Name', year = 1923)
for i in range(5):
    no_name.drive()

no_name.info()