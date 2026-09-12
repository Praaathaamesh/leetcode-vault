'''
strategy to be used here:
    - DP bottom up

complexty:
    - O(n) time and space
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. len of arr
        n = len(nums)

        # 2. defien dp table/ matrix of size n * 2
        dp = [[0]*2 for _ in range(n)]

        # 3. last two boxes must have last element of nums
        dp[n-1][0] = dp[n-1][1] = nums[n-1]

        # 4. we are settled with the last two boxes
        # 5. to fill the rest, rev iterate using for loop
        for i in range(n-2, -1, -1):
            # 6. fill right box max(nums at i or nums at i + next right box)
            dp[i][1] = max(nums[i], nums[i] + dp[i+1][1])
            # 7. fill left box as max(right box, next left box)
            dp[i][0] = max(dp[i+1][0],dp[i][1])
        
        return dp[0][0]
