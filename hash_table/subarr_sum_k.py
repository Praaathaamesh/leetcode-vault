'''
strategy to be used here:
    - hash map 

complexity: 
    - O(n) time and O(n) space
'''

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 1. set result int var
        result = 0
        # 2. set cursum var
        cursum = 0
        # 3. set hashmap prefix_sum
        prefix_sum = {0 : 1}

        # 4. iterate over the nums
        for num in nums:
            cursum += num
            diff = cursum - k
            result += prefix_sum.get(diff, 0)
            prefix_sum[cursum] = 1 + prefix_sum.get(cursum, 0)
        

        # 4. and we are returning it
        return result