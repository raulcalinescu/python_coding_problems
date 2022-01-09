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
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Note: you also usually want to initialize your objects. For that, you place an __init__ method in your class.

def happy_number(self, n: int) -> bool:
    return True


def add_square_digits(num):
    if num == 0:
        return 0
    return ((num % 10) ** 2) + add_square_digits(num // 10)


# Driver code
n = 123
print(add_square_digits(n))
