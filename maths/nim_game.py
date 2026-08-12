'''
strategy to be used here:
    -  check complete division by 4

complexity:
    - O(1) time and space
'''

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0