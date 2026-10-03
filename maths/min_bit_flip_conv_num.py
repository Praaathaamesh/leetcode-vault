'''
strategy to be used here:
    - Brian Kernighans algorithm (rightmost bit of n clears when n&(n-1))

complexity:
    - O(1) time and space
'''

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 1. xor result between start and end; set count var
        xor_res = start ^ goal
        count = 0

        # 3. while xor_res is nonzero --> do the algo
        while xor_res:
            xor_res &= (xor_res - 1)
            count += 1

        # 2. return count
        return count
