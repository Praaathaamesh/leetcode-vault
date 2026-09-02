'''
strategy to be used here:
    - simulation

complexity:
    - O(n logn) time and O(1) space
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        empty = 0

        while numBottles > 0:
            # drink all full bottles
            drunk += numBottles
            empty += numBottles

            # exchange empty bottles for full bottles
            numBottles = empty // numExchange
            empty = empty % numExchange

        return drunk