class Point():
    def __init__(self, input1, input2):
        self.x = input1+10
        self.y = input2+101


p = Point(2, 10)
print(p.x)
print(p.y)

print("**********************************")


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)


flight = Flight(3)

people = ["Hero", "John", "Smith", "Suwath", "Kamal"]

for person in people:
    success = flight.add_passenger(person)
    if success == True:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
