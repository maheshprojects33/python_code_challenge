"""
The Sweetest Ice Cream
Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest ice cream. Note that there is a class provided for you in the Tests tab.
class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles

    Each sprinkle has a sweetness value of 1
    Check below for the sweetness values of the different flavors.
Flavors	Sweetness Value
Plain	0
Vanilla	5
ChocolateChip	5
Strawberry	10
Chocolate	10
Examples
ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8

sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
sweetest_icecream([ice3, ice1]) ➞ 23
sweetest_icecream([ice3, ice5]) ➞ 17
Notes
    Remember to only return the sweetness value.
    IceCream class is provided (check Tests tab).
"""


class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles

def sweetest_icecream(lst):
    sweet = 0
    for sweetness in lst:
        value = sweetness.num_sprinkles
        if sweetness.flavor == "Strawberry" or sweetness.flavor == "Chocolate":
            value += 10
        elif sweetness.flavor == "Vanilla" or sweetness.flavor == "ChocolateChip":
            value += 5

        if value > sweet:
            sweet = value
    return sweet


ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8
print(ice1.num_sprinkles, ice2.num_sprinkles, ice3.num_sprinkles, ice4.num_sprinkles, ice5.num_sprinkles)
print()
print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5])) #➞ 23
print(sweetest_icecream([ice3, ice1])) #➞ 23
print(sweetest_icecream([ice3, ice5])) #➞ 17