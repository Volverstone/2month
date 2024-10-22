class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # constructor matching
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class attribute
    counter = 0

    # constructor           #parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # fields / attributes
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city, speed):
        print(f'Car {self.model} is driving to {city} with {speed} km/h')

    # method
    def signal(self, number_of_times, sound):
        while number_of_times > 0:
            print(f'Car {self.model} is signalling: {sound}')
            number_of_times -= 1


class Truck(Car):
    counter = 0

    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1