"""
Book Shelf
Create a Book class that has two attributes:
    .title
    .author
and two methods:
    A method named .get_title() that returns: "Title: " + the instance title.
    A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:
    Pride and Prejudice - Jane Austen (PP)
    Hamlet - William Shakespeare (H)
    War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.
For instance, if I instantiated the following book using this Book class:
    Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:
Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
Notes
    Read more about Python classes in Resources.
    Remember, after you've finished writing the class and its methods, you must instantiate it through the creation of new objects.
"""

class Book:
    def __init__(self, book):
        self.book = book
        self.title = self.book.split("-")[0]
        self.author = self.book.split("-")[1].strip().split("(")[0]

    def get_title(self):
        return f"Title: {self.title}"

    def get_author(self):
        return f"Author: {self.author}"


PP = Book("Pride and Prejudice - Jane Austen (PP)")
H = Book("Hamlet - William Shakespeare (H)")
WP = Book("War and Peace - Leo Tolstoy (WP)")
HP = Book("Harry Potter - J.K. Rowling (HP)")

print(HP.title)
print(HP.author)
print(HP.get_title())
print(HP.get_author())