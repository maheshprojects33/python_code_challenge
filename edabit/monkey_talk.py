"""
Let's Talk Like a Monkey 🐵
Mubashir can talk with monkeys. You can also learn their simple language.
Create a function that takes a string txt and returns the string in monkeys language. You have to figure out their language from test cases.
Examples
monkey_talk("Mubashir Hassan") ➞ "Ook ook."
monkey_talk("Hello") ➞ "Ook."
monkey_talk("Matt") ➞ "Ook."
monkey_talk("Everyone") ➞ "Eek."
monkey_talk("Edabit is Amazing") ➞ "Eek eek eek."
"""

def monkey_talk(txt):
    vowel = "AEIOUaeiou"
    a = txt.split(" ")
    b = []
    for x in range(len(a)):
        if a[x][0] in vowel:
            b.append("Eek")
        else:
            b.append("Ook")
    return " ".join(b).capitalize()+"."

print(monkey_talk("Edabit is Amazing"))
print(monkey_talk("you are so beautiful"))
print(monkey_talk("Mubashir Hassan"))