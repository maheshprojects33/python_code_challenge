"""
Python Classes Mini Challenge
In this challenge, you will learn about classes in Python.
Python classes are easy to understand. They are almost the same as JavaScript classes, with a different syntax and different constructor function names. Constructors define some variables in your class; in Python that is def __init__(self). Other functions are defined the same as normal.
I want you to create a class called programmer. It should have a salary value, work_hours value, and a __del__(self) function. __del__(self) should return "oof, " + str(salary) + ", " + str(work_hours) when the object is destroyed. salary and work_hours will be in the constructor. Variables in a class are defined with self.name = value.
Also, define a function that will compare two programmers (their salary and work_hours) and return the programmer with the lower salary. If their salary is equal, then compare their work_hours, which will always be different.
This is not really a challenge, just an introduction to Python classes.
Examples
prog = programmer(25000, 5)
prog.salary ➞ 25000
prog.work_hours ➞ 5

del prog ➞ "oof, 25000, 5"
# By the __del__ function.
Notes
    Only base functions are pre-written in the code tab. You need to complete them and possibly add a few arguments.
    Class variables are defined inside the __init__ function.
    In most cases __del__ isn't used to return values (but it's not possible to check print output in an Edabit test).
"""

class Programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def __del__(self):
        return "oof, " + str(self.salary) + ", " + str(self.work_hours)

    def compare(self, other):
        if self.salary == other.salary:
            if self.work_hours < other.work_hours:
                return self.work_hours
            return other.work_hours
        if self.salary < other.salary:
            return self.salary
        return other.salary


jack = Programmer(25000, 15)
john = Programmer(50000, 5)

print(jack.salary) #➞ 25000
print(jack.work_hours) #➞ 5

print(jack.compare(john))