'''
strategy to be used here:
    - brute force loop

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 1. res variable
        res = 0

        # 2. loop through nums and iterative operate
        for i in range(n):
            res ^= (start + 2 * i)
        
        # 3. return the res
        return res