'''
strategy to be used here:
    - Two pointers

complexity:
    - O(n logm) time and O(logm) space
'''

from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        # 1. set up the return variable
        total_sum = 0

        # 3. set the end pointers
        l = 0
        r = len(nums) - 1

        # 4. process eles from both ends
        while l < r:
            # 5. concat the nums using simple typecasting
            concat_val = int(str(nums[l]) + str(nums[r]))
            # 6. add it to total sum
            total_sum += concat_val

            # 7. move pointers to center
            l += 1
            r -= 1
        
        # 8. if nums is odd, middle isnt present so add the l again to total sum
        if l == r:
            total_sum += nums[l]

        # 2. return it!
        return total_sum