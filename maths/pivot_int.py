'''
strategy to be used here:
    - x is perfect sqrt of int from 1 to n

complexity:
    - O(1) time and O(1) space
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n*(n+1))//2
        x = math.isqrt(total)

        return x if x*x == total else -1
