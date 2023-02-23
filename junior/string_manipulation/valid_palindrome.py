# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
from is_palindrome import Palindrome
import re


class Solution:
    # beats 73% time submissions and 20% in memory
    def valid_palindrome(s: str) -> bool:
        tmp_lst = []
        for c in list(s):
            if c in '123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ':
                tmp_lst.append(c)
        final = ''.join(tmp_lst).lower()
        return str(final) == str(final)[::-1]

    # 37ms , beats 95% time, 20% mem
    def optimal_palindrome(s: str) -> bool:
        data = re.sub(r'[^0-9a-zA-Z]', '', s.lower())
        return data == data[::-1]


# Main Driver
my_string = " ta.;'co -=Cat"
print(Solution.valid_palindrome(my_string))
print(Solution.optimal_palindrome(my_string))

