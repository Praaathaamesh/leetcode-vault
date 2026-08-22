'''
strategy to be used here:
    - same as power of 3/4; use for loop over [2, 3, 5]

complexity:
    - O(logn) time and O(1) space
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime

        return n == 1