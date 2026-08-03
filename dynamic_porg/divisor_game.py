'''
strategy to be used here:   
    - one-time parity check

complexity:
    - O(1) time and space
'''

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0