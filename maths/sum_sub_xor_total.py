'''
strategy to be used:
    - calc OR for each n and left shift 

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res |= n

        return res << (len(nums)-1)  