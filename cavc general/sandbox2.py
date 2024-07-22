class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print('Vehicle created')
    
    def description(self):
        print('This is a vehicle.')
    
    def moving(self):
        print('Vehicle is moving')

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, engine_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.engine_type = engine_type
        print('Car is created')
    
    def description(self):
        print(f'This is a {self.num_doors}-door car with a {self.engine_type} engine.')
    
    def honk(self):
        print('Honk!')

# Creating an instance of Vehicle
v = Vehicle("Honda", "Civic", 2017)

# Creating an instance of Car with extra attributes
c = Car("Toyota", "Corolla", 2020, 4, "V6")

# Calling methods on the Vehicle instance
v.description()  # Output: This is a vehicle.
v.moving()       # Output: Vehicle is moving

# Calling methods on the Car instance
c.description()  # Output: This is a 4-door car with a V6 engine.
c.moving()       # Output: Vehicle is moving (inherited from Vehicle)
c.honk()         # Output: Honk!
