'''
strategy to be used here:
    - iteration with if nums[i]>nums[(i+1) % len(nums)] --> inc count --> if count > 1--> return false 
    - else true

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def check(self, nums: list[int]) -> bool:
        # 1. set count and len var
        N = len(nums)
        count = 0

        # 3. iterate and check over the idx
        for i in range(N):
            if nums[i] > nums[(i+1) % N]:
                count += 1
                if count > 1:
                    return False

        # 2. return true if all conditions true
        return True