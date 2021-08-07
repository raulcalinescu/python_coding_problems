# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
from typing import List


# [0, 2, 5, 0]
class Solution:
    @staticmethod
    def move_zeroes_easy(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)

    @staticmethod
    def move_zeroes_fast(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer approach
        nonzeros = 0  # slow
        zeros = 0  # fast
        while zeros < len(nums):
            if nums[zeros] == 0:
                zeros += 1
            else:
                nums[zeros], nums[nonzeros] = nums[nonzeros], nums[zeros]  # swaps values between the two
                zeros += 1
                nonzeros += 1


# Driver code
nums = [0, 2, 5, 0]
print(nums)
moves = Solution()  # have to instantiate the class instance in the driver code
moves.move_zeroes_fast(nums)
print(nums)
