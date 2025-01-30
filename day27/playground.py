def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'{k}: {v}')
    n += kwargs['add']
    n *= kwargs['multiply']
    print(f'{n}')

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Ford", model="Mustang")
print(my_car.make, my_car.model)