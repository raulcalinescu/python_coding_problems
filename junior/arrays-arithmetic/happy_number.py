# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
# not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Note: you also usually want to initialize your objects. For that, you place an __init__ method in your class.

# The reason we use a HashSet and not a Vector, List, or Array is because we're repeatedly checking whether or
# not numbers are in it. Checking if a number is in a HashSet takes O(1) time,
# whereas for the other data structures it takes O(n) time.
# Choosing the correct data structures is an essential part of solving these problems.

# LC's HashSet solution - 48 ms:
class Solution(object):
    @staticmethod
    def is_happy(self, n: int) -> bool:
        def get_next(num, sum=0):
            while num > 0:
                sum += (num % 10) ** 2
                num //= 10
            return sum

        seen = set()  # looking in a set takes O(1)
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# Floyd's Cycle-Finding Algorithm - slow and fast runner pointers
# https://leetcode.com/problems/happy-number/solution/
class Solution2(object):
    @staticmethod
    def is_happy2(self, n: int) -> bool:
        def get_next(num, sum=0):
            while num > 0:
                sum += (num % 10) ** 2
                num //= 10
            return sum
        slow = n
        fast = get_next(n)
        while fast != 1 and fast != slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1

# My Solution - Slow - 88 ms, only faster than 5%
def happy_number(n):
    first_sum = add_square_digits(n)
    if first_sum == 1:
        return True
    temp_sum = 0
    seen = set()
    seen.add(first_sum)
    while temp_sum not in seen:
        seen.add(temp_sum)
        if temp_sum == 1:
            return True
        if temp_sum == 0:
            temp_sum = add_square_digits(first_sum)
        else:
            temp_sum = add_square_digits(temp_sum)
    return False


def add_square_digits(num):
    if num == 0:
        return 0
    return ((num % 10) ** 2) + add_square_digits(num // 10)


# Driver code
number = 19
result = Solution()

print(result.is_happy(None, number))
print(happy_number(number))
