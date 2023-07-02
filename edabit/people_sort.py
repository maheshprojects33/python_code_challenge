"""
People Sort
Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.
The Person class will only include these attributes in the following order:
    firstname
    lastname
    age
Examples
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey
people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters
people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40
Notes
    Sort the list in ASCENDING order.
    All objects will be valid.
"""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


def people_sort(lst, attr):
    if attr == "firstname":
        return [item.firstname for item in sorted(lst, key=lambda item: item.firstname)] # To Get value
        # return sorted(lst, key=lambda item: item.firstname) # To Get Address
    elif attr == "lastname":
        return [item.lastname for item in sorted(lst, key=lambda item: item.lastname)] # To Get value
        # return sorted(lst, key=lambda item: item.lastname) # To Get Address
    else:
        return [item.age for item in sorted(lst, key=lambda item: item.age)] # To Get value
        # return sorted(lst, key=lambda item: item.age) # To Get Address


p1 = Person('Michael', 'Smith', 40)
p2 = Person('Alice', 'Waters', 21)
p3 = Person('Zoey', 'Jones', 29)
p4 = Person('Susan', 'Heffley', 43)
p5 = Person('Bob', 'Fredericson', 70)
p6 = Person('Braxton', 'Leighsonley', 2)
p7 = Person('Joshua', 'Senoron', 99999999999999)

people = [p1, p2, p3, p4, p5, p6, p7]

print(people_sort(people, "firstname"))
print(people_sort(people, "lastname"))
print(people_sort(people, "age"))
print(people_sort([p1, p2, p3], "firstname"))
print(people_sort([p1, p2, p3], "age"))