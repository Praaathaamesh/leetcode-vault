'''
strategy to be used here:
    - DP bottom up

complexity:
    - O(n * t) time and O(t) space
'''

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 1. create the dp array
        dp = [amount + 1] * (amount + 1)  
        dp[0] = 0 # min cost needed to make respected cost

        # 2. iterate over amount in coins arr
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0: # step minus cost is >= 0
                    dp[a] = min(dp[a], 1 + dp[a - c]) # select the min
        return dp[amount] if dp[amount] != amount + 1 else -1 # wrong amount be -1