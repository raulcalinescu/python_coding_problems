# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# https://leetcode.com/problems/single-number/solution/


from collections import defaultdict
from typing import List

# [1,2,5,1,2,3,3] -> return 5
class Solution:
    @staticmethod
    # List operation approach
    def remove_single_element(nums: List[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

    # HashTable approach
    def rem_single_element(nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i
# Driver code
list = [1,2,5,1,2,3,3]
print(Solution.remove_single_element(list))


