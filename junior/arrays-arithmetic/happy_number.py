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

# Slow - 88 ms, only faster than 5%

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
number = 116
print(happy_number(number))
