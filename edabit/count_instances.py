"""
Count Number of Instances
Create a class named User and create a way to check the number of users (number of instances) that were created, so that the value can be accessed as a class attribute.
Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3

Make sure that the usernames are accessible via the instance attribute username.
u1.username ➞ "johnsmith10"
u2.username ➞ "marysue1989"
u3.username ➞ "milan_rodrick"
Notes
Feel free to check out the resources provided in the Resources tab for some helpful information on Python classes!
"""

class User:
    user_count = 0
    def __init__(self, username):
        self.username = username
        User.user_count += 1

u1= User("johnsmith10")
u2 = User("marysue1989")
u3 = User("milan_rodrick")
print(u1.username)
print(u2.username)
print(u3.username)
print(User.user_count)


class Composer:
    count = 0
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.count = Composer.count
        Composer.count += 1
print(f"\nOther Similar Challege Solution in same file")
print(Composer.count) # ➞ 0

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count) # ➞ 1

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.count) # ➞ 3