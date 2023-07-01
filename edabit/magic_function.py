"""
Magic Function
Create a class with a few functions like these examples.
    magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
    magic.str_length("string") is a function that returns the length of the string.
    magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
    magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of the new list is 0, return -1.
Examples
magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"
magic.str_length("hello world") ➞ 11
magic.trim("      python is awesome      ") ➞ "python is awesome"
magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]
Notes
N/A
"""
class Magic:
    def replace(self, word, find, replace):
        fixed = word.replace(find, replace)
        return fixed

    def str_length(self, word):
        return len(word)

    def trim(self, word):
        return word.strip()

    def list_slice(self, lst, tpl):
        start_index, end_index = tpl
        new_list = lst[start_index:end_index]

        return new_list

magic = Magic()
print(magic.list_slice([1, 2, 3, 4, 5,6,7,8], (2, 6)))
print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world")) # ➞ 11
print(magic.trim("      python is awesome      ")) # ➞ "python is awesome"

