'''
strategy to be used here:
    - prefix and suffix sums

complexity:
    - O(n) time and space
'''

from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # 1. set length var, res var, total_sum and prefix_sum
        n = len(nums)
        res = [0] * n
        total_sum = sum(nums)
        prefix_sum = 0

        # 2. enumerate idx and ele
        for i, num in enumerate(nums):
            total_sum -= nums[i]
            left_sum = i * nums[i] - prefix_sum
            right_sum = total_sum - (n - i - 1) * nums[i]
            res[i] = right_sum + left_sum
            prefix_sum += nums[i]

        # 3. return the res
        return res