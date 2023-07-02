"""
Wait... Who Am I?
Hello there, I... seem to not remember who I am, my memories is all... cloudy, although maybe if I could piece it together...
Oh! Maybe you could help me make a class that helps me remember things. Maybe a method called add that would add to my memory if I would recall things and a remember method that would let me recall a specific memory.
But you have to make add more flexible, I might recall many things in an instant or only one that I would forget again.
Examples :D
# add method doesn't return anything.
memories.add(name="Shane", gender="M", catch_phrase="bazinga")
memories.add(work="None", love_life=0)
memories.add(adress="car")
memories.remember("work") ➞ "None"
memories.remember("gender") ➞ "M"

# If memory was not added, return False
memories.remember("lover") ➞ False
Notes
The add method should be able to handle any number of arguments
"""


class Memories:
    def __init__(self):
        self.data = {}

    def add(self, **kwargs):
        self.data.update(kwargs)
        return self.data

    def remember(self, recall):
        if recall in self.data:
            result = self.data.get(recall)
            return result
        else:
            return False




memories = Memories()
memories.add(name="Shane", gender="M", catch_phrase="bazinga")
memories.add(work="None", love_life=0)
memories.add(adress="car")
memories.add(purpose="lol idk", social_life="What's that?", dream="money")
memories.add(fears="code", languages=["english", "filipino", "python", "Java"])
memories.add(favorite_number=404, is_gamer=True, race="Filipino", gender="M", name="Shane",
             embarassing_moments="dance with her.. oh god", omai_wa_mo_shindeiru="NANI?!")
memories.add(strength_level="Over 9000!!!")

print(memories.remember("work")) #➞ "None"
print(memories.remember("gender")) #➞ "M"
# If memory was not added, return False
print(memories.remember("lover")) #➞ False
print(memories.remember("languages"))
