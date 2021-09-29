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
import collections
import random
from collections import defaultdict
from typing import List
import sys


class Solution(object):
    @staticmethod # O(n), O(n)
    def majority_element_mysol(nums: List[int]) -> int:
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

    # O(n), O(n)
    def maj_elem_hash_map(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)  # Counter holds data in an unordered collection just like hashtable obj
                                            # elements represent the keys and the count as values
        return max(counts.keys(), key=counts.get)

    # O(infinity) - no upper bound for worst case, but likely linear otherwise and O(1) space
    def maj_elem_randomization(self, nums: List[int]) -> int:
        maj_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > maj_count:
                return candidate

    # O(n^2) time and O(1) space, no additional space proportional to the input size
    def majority_element_brutef(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num


# Driver code
nums = [-2, 1, 2, 0, 1, 1]
print(Solution.majority_element(nums))
