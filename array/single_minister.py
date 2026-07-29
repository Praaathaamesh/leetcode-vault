'''
strategy to be used here:
    - XOR bitwise operator use

complexity:
    - O(n) time, O(1 space
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result