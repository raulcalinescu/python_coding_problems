# Given an integer x, return true if x is a palindrome, and false otherwise.
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


# Driver Code
n = -12321
print(is_palindrome(n))
