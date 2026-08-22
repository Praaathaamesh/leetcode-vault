'''
strategy to be used here:
    - check if zero for false if not till reminder is zero keep dividing the num and return comparison of n with 1

complexity:
    - O(log n) time and O(1) space
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1