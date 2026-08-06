'''
strategy to be used here:
    - Sum formula (expected - actual)

Complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum