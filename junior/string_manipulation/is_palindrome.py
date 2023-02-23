# Given an integer x, return true if x is a palindrome, and false otherwise.

class Palindrome:
    @staticmethod
    def is_palindrome(num):
        """
        :type num: int
        :rtype: bool
        """
        if str(num) == reverse(str(num)):
            return True
        else:
            return False


def reverse(string):  # reversed () returns the reversed iterator of the given string and then its elements
    string = "".join(reversed(string))  # are joined empty string separated using join()
    return string


# with reversing it is possible to write in one line
# '[::]' this means print all, and this '[::-1]' reverses, it is mostly used with list in python
def is_palindrome2(self, x: int) -> bool:
    return str(x) == str(x)[::-1]

