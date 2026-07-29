'''
strategy to be used here is
    - One pas,  track minimum so far

complexity
    - O(n) time, O(1) space
'''

class Solution:
    def maxProfit(self, prices) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit