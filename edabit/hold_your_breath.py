"""
Hold Your Breath!
You will be given a list of numbers which represent your character's altitude above sea level at regular intervals:
    Positive numbers represent height above the water.
    0 is sea level.
    Negative numbers represent depth below the water's surface.
Create a function which returns whether your character survives their unsupervised diving experience, given a list of integers.
    Your character starts with a breath meter of 10, which is the maximum. When diving underwater, your breath meter decreases by 2 per item in the array. Watch out! If your breath diminishes to 0, your character dies!
    To prevent this, you can replenish your breath by 4 (up to the maximum of 10) for each item in the array where you are at or above sea level.
    Your function should return True if your character survives, and False if not.
Worked Example
diving_minigame([-5, -15, -4, 0, 5]) ➞ True
# Breath meter starts at 10.
# -5 is below water, so breath meter decreases to 8.
# -15 is below water, so breath meter decreases to 6.
# -4 is below water, so breath meter decreases to 4.
# 0 is at sea level, so breath meter increases to 8.
# 5 is above sea level and breath meter is capped at 10 (would've been 12 otherwise).
# Character survives!
"""


def diving_minigame(lst):
    breath_meter = 10
    breath_decrease = 2
    breath_regain = 4
    for i in lst:
        if i < 0:
            breath_meter -= breath_decrease
            if breath_meter <= 0:
                return False
        elif i >= 0:
            breath_meter += breath_regain
            if breath_meter > 10:
                breath_meter = 10
    return True


print(diving_minigame([-5, -15, -4, 0, 5]))
print(diving_minigame([-5, -5, -5, -5, -5, 2, 2, 2, 2, 2, 2, 2, 2]))
print(diving_minigame([-3, -6, -2, -6, -2]))

