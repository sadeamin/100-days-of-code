# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(3, 5, 6))
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for k, v in kwargs.items():
#     #     print(k)
#     #     print(v)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="GT-R202")
print(my_car.make)
print(my_car.model)