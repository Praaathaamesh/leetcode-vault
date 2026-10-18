'''
strategy to be used here:
    - brute force digit extraction

complexity:
    - O(1) time and O(n) space
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        # 1. set res arr
        res = []

        # 2. iterate over the ranges
        for i in range(left, right+1):
            temp = i # preserve i
            while temp > 0: 
                digit = temp % 10
                if digit == 0 or i % digit != 0: # use i not temp
                    break
                temp //= 10 # reduce the num by last place
            else:
                res.append(i) 

        # 3. return the res
        return res 