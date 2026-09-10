'''
strategy to be used here:
    - count sorting

complexity:
    - O(n) time and O(1) space
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. count the occurances of numbers in separate list
        count = [0] * 3
        for num in nums:
            count[num] += 1

        # 2. sort them via idx (basically wtf is this)
        idx = 0 # increm by one as we done with all of them
        for i in range(3):
            while count[i]: # as long as the count at 0/1/2is nonzero
                count[i] -= 1
                nums[idx] = i
                idx += 1