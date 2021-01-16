people = [
    {"name": "name1", "house": "house3"},
    {"name": "name2", "house": "house2"},
    {"name": "name3", "house": "house1"}
]


def f(person):
    return person["house"]


people.sort(key=f)
print(people)

people.sort(key=lambda person: person["name"])
print(people)
