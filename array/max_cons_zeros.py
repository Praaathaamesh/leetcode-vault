'''
strategy to be used here:
    - iterate and increment count and return max

complexity:
    - O(n) time and O(1) space
'''

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0 # set both to 0
        for num in nums: # iterate over the binary list
            count = count + 1 if num else 0 # increment count by 1 if num is not zero
            result = max(result, count) # update result as max between res and count
        return result # return the result variable