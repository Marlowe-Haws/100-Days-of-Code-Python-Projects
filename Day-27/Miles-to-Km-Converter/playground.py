# def add(*args):
#     return sum(args)
# print(add(1, 2, 3, 8, 22))

# Keyword arguments (**kwargs) returns dictionary with keyword:value pairs.
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=4)

# You can use .get() method to create a class with optional kwargs.
# It will return None if left undefined.
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Ford")
print(my_car.model)
