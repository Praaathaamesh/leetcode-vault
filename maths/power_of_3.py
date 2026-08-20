'''
strategy to be used here:
    - keep floor diving till three and check if the num has updated to 1

complexity:
    - O(log n) and O(1) space
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1