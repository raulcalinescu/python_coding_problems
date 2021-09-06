# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
# element always exists in the array.
#
# Example
# Input: nums = [3,2,3]
# Output: 3
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1

# if you just need a number that's bigger than all others, you can use
# float('inf')
# in similar fashion, a number smaller than all others:
# float('-inf')

from collections import defaultdict
from typing import List
import sys


class Solution(object):
    @staticmethod
    def majority_element(nums: List[int]) -> int:
        # max = -sys.maxsize or float('-inf')
        max = 0
        dict = defaultdict(int)
        for i in nums:
            dict[i] += 1
        for k in dict:
            if max < dict[k]:
                max = dict[k]
                result = k
        return result


# Driver code
nums = [-2, 1, 2, 0, 1, 1]
print(Solution.majority_element(nums))
