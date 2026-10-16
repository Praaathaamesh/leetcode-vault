'''
strategy to be used here:
    - 0 arr of n ele, iterate over all except first, till num not 0, inc res[i] by 1, remove set bits, return res

complexity:
    - O(nlogn) time and O(1) extra space/O(n) output arr
'''

class Solution:
    def countBits(self, n: int) -> list[int]:
        # 1. res 0 arr
        res = [0] * (n + 1)

        # 2. iterate
        for i in range(1, n + 1):
            num = i
            while num != 0:
                res[i] += 1
                num = num & (num - 1)
        
        # 3. return res 
        return res