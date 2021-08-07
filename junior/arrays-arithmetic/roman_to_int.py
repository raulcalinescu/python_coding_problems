# https://leetcode.com/problems/roman-to-integer/
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
# which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not III. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# 48 ms faster than 65% | 14.2 MB less than 84%
class Solution:
    @staticmethod
    def roman_to_int(s: str) -> int:
        Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        division = False
# keep a flag when division is needed to avoid counting second letter next iteration
        for char in range(0, len(s) - 1):
            if division:
                division = False
                continue
            if Dict[s[char]] < Dict[s[char + 1]]:
                res += Dict[s[char + 1]] - Dict[s[char]]
                division = True
            else:
                res += Dict[s[char]]
# consider case where len(s) is 1 or when no division was done last but need to include last letter
        if len(s) >= 1 and not division:
            res += Dict[s[len(s)-1]]
        return res


# driver code
num = Solution.roman_to_int("M")
print(num)
