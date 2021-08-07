# Given a non-empty array of non-negative integers nums, the degree of this array is defined
# as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.
from typing import List


# [2, 1, 2, 0, 3, 3]  so shortest same degree subarray is
class Solution:
    @staticmethod
    def find_shortest_array(nums : List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1   # look this up soon

        ans = len(nums)   # chose the maximum value so we can then get minimum
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans


# Driver code
nums = [2, 1, 2, 0, 3, 3]
ans = Solution.find_shortest_array(nums)
print(ans)
