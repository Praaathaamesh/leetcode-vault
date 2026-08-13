'''
strategy to be used here:
    - math pattern (divide by 3; reminder of 0, 1, or any other has a formula)

complexity:
    - O(1) time and space
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        else:
            return 3 ** (n // 3) * 2