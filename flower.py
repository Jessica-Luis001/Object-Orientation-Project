 #my class
class Vehicles:
    """Class for Vehicles"""

    def __init__(self, name):
        #attributes
        self.carname = name
        self.wheels = 0
        self.doors = 0
        self.seats = 0
        self.passengers = []
        self.passengers1 =[]

    def num_wheels(self, wheels):
        self.wheels = wheels

    def num_doors(self, doors):
        self.doors = doors

    def num_seats(self, seats):
        self.seats = seats

    def add_pass(self, passengers):
        self.passengers = passengers
        self.passengers1.append(passengers)

#objects
v1 = Vehicles("Car")
print(v1.carname)
v1.wheels = "4 wheels"
print(v1.wheels)
v1.doors = "4 doors"
print(v1.doors)
v1.seats = "7 seats"
print(v1.seats)

my_list = ["Mily", "Kirtsen", "Juliana", "Jessica"]
v1.add_pass(my_list)
print(v1.passengers)

v1.add_pass("Joseph")
print(v1.passengers1)

v2 = Vehicles("Truck")
print(v2.carname)
