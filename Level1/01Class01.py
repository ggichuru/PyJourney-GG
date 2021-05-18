# Declaring an object

class Car:
    # class attributes
    car_consumption = 2400
    car_class = 'fuel'

    def __init__(self, name, millage):
        self.name = name
        self.millage = millage

    def carModel(self):
        print(f'This is a {self.name}')
        print(f'It has {self.millage} km millage')
        print(f'It runs on {self.car_class}')
        print(f'It consumes {self.car_consumption}cc of fuel')

m6 = Car(input('Enter you car brand: '), input('Enter Millage: '))
# m6 = Car('BMW M6')

print(m6.name)
m6.carModel()


# class myCar():
#     def __init__(self, car):
#         self.car = car

#     def carMod(self):
#         print(f'This is a {self.car}')

# car = myCar('BMW M6')
# car.carMod()        
