'''
strategy to be used here:
    - iteration

complexity:
    - O(k * (n!/(n-k)! * k!)) time and space
'''

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # 1. define result nested intlist
        result = []
        # 3. set pointer i for while loop and combination binary arr of len k
        i = 0
        combine = [0] * k

        # 4. till i is or more than 0
        while i >= 0:
            combine[i] += 1 # stepup the value at next postion
            if combine[i] > n: # if exceeds n stepdown
                i -= 1
                continue
            if i == k-1: # check to have complete combination
                result.append(combine.copy())
            else:
                i += 1
                combine[i] = combine[i-1]

        # 2. and we are returning it
        return result