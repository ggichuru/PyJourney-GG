class Car():
    car_brand = 'BMW'

    def __init__(self, car_model, car_color):
        self.car_model = car_model
        self.car_color = car_color

Alex = Car('740i', 'mate black')
John = Car('x6', 'white')


print(f'Alex has a {Alex.car_color} {Alex.car_brand} {Alex.car_model}')
print(f'John has a {John.car_color} {John.car_brand} {John.car_model}')


# Defining instance variable using the normal method
class aCar():
    car_brand = 'BMW'
    # init constructor
    def __init__(self, car_model):
        self.car_model = car_model

    # Add an instance of a variable
    def setCarColor(self, color):
        self.color = color

    # Retrieve instance variable
    def getCarColor(self):
        return self.color

name = input('Enter you name: ')
car = aCar(input('What type of BMW do you drive: '))
car.setCarColor(input('What is the color of your car: '))
print(f'{name} drives a {car.getCarColor()} {car.car_brand} {car.car_model}')

