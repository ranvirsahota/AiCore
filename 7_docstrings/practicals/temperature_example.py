class Temperature:
    """
    Converts tempreature betwen Fahrenheit and Celsius
    
    """
    def __init__(self, temp_celsius):
        self.temp_celsius = temp_celsius

    
    '''converts from celsius to fahrenheit'''
    def convert_temp_to_fahrenheit(self):
        return (self.temp_celsius * 1.8) + 32

    '''converts fahrenheit to celsius'''
    @staticmethod
    def convert_fahrenheit_to_cel(temp_fah):
        return (temp_fah - 32) * 1.8
    
    '''enuses teprature value provided is valid'''
    @staticmethod
    def check_valid_temp(temp):
        if -273 <= temp <= 3000:
            print("This is a valid temperature")
    
    '''create temperature with fahrenheit'''
    @classmethod
    def create_with_fahrenheit(cls, temperature):
        return cls(Temperature.convert_fahrenheit_to_cel(temperature))
    
    '''standard'''
    @classmethod
    def standard(cls):
        return cls(0)

    def __repr__(self) -> str:
        temp = str(self.temp_celsius)
        return temp
