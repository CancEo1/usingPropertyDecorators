# Purpose: a python program to illustrate the use of @property decorators
# raises a valueError so code is incomplete. Technically speaking
# just meant to illustrate the use of @property decorators

# creating class
class Celsius:
    # define init method with its parameter
    def __init__(self, temp = 0):
        self._temperature = temp

    # @property decorator
    @property
    # getter method for temperature
    def temp(self):
        print("The value of the temperature is: ")
        return self._temperature

    # setter method
    @temp.setter
    def temp(self, val):
        # if temperature is less than -273, then raises a value error
        if val < -273:
            raise ValueError("It is a value error.")

        # print this if the value of the temperature is set
        print("The values of the temperature is set.")
        self._temperature = val

# creating an object of the class
cel = Celsius();

# setting the temperature
cel.temp = -270

# prints the temperature that is set
print(cel.temp)

# setting the temperature to a value less than -273
# this will raise a ValueError
cel.temp = -300
print(cel.temp)