'''
strategy to be used here:
    - return rem of sums division by k

complexity:
    - O(1) time and space
'''

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k