'''
strategy to be used here:
    - bin func count method

complexity:
    - O(1) time and space
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. return binary of n and str count 1 in it
        return bin(n).count('1')