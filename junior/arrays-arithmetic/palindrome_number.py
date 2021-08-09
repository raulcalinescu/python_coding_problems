# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        pal = 0
        temp = x
        while temp != 0:
            pal = 10 * pal + temp % 10
            temp = temp // 10
        if x == pal:
            return True
        else:
            return False


# Driver code
print(Solution.isPalindrome(-121))
