"""
Digits Battle!
Starting from the left side of an integer, adjacent digits pair up in "battle" and the larger digit wins. If two digits are the same, they both lose. A lone digit automatically wins.
Create a function that returns the victorious digits.
To illustrate:
battle_outcome(578921445) ➞ 7925
# [57]: 7 wins; [89] 9 wins; [21] 2 wins;
# [44] neither wins; 5 (automatically) wins
"""


def battle_outcome(num):
    winner = []
    try:
        for i in range(0, len(str(num)), 2):
            if str(num)[i] != str(num)[i + 1]:
                winner.append(max(str(num)[i], str(num)[i+1]))
            else:
                continue
    except:
        winner.append(str(num)[-1])

    return int("".join(winner))


print(battle_outcome(111))