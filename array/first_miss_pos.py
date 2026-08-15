'''
strategy to be used here:
    - Place the numbers in their correct position

complexity:
    - O (n) time and O(1) space
'''
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # place ints in their correct position
        for i in range(n):
            while 1 <= nums[i] <= n  and nums[i] != nums[nums[i] - 1]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]


        # find the first idx of int not in a correct position
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        #if all goes well n+1 is missing
        return n+1