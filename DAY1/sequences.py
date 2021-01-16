name = "Harry"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Python List -mutable values(list)
list_name = ["Harry", "Ron", "Hermione", "Ginny"]
print(list_name[0])
list_name.append("Draco")  # appending

list_name.sort()  # sorting

print(list_name)


# Tuples -immutable values(tuple)
coordinateX = 10.0
coordinateY = 20.0

coordinate = (10.0, 20.0)

# Sets -collection of unique value(set)
s = set()
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(6)
print(s)

s.remove(2)
print(s)
print(f"The set has {len(s)} elements")  # calculate the length


# Dictionary -collection of keyvalue pairs(dict)
houses = {0: "Gryffindor", 1: "Slytherin"}
print(houses[0])
print(houses[1])
houses[1] = "SirageHouse"
print(houses[1])
