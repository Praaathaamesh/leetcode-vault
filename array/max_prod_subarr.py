'''
strategy to be used here:
    - prefix/suffix

complexity:
    - O(n) time and O(1) space
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1. set up the length and first idx ele variable for nums
        n, res = len(nums), nums[0]
        # 2. set up prefix and suffix
        prefix = suffix = 0

        # 3. iterate over nums ele via idx using for loop
        for i in range(n):
            # 5. nums at i by 1 if prefix is 0 else multiply by prefix
            prefix = nums[i] * (prefix or 1)
            # 6. nums at n-1-i by 1 if suffix is 0 else multiply by suffix
            suffix = nums[n-1-i] * (suffix or 1)
            # 4. idea is to find max between current res or max of prefix or suffix and update res accordingly
            res = max(res, max(prefix, suffix))
        return res