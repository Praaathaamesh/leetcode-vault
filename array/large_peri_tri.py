'''
strategy to be used here:
    - brute force (sort it, iterate from behind and leave the last two, chcek prevprev + prev > curr and return their sum, return 0)

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # 1. sort the arr
        nums.sort()
        
        # 2. check side ineq theorem for pre, curr and next ele idx
        for i in range(len(nums)-1, 1, -1): # iterate from back, keep last two intact
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i] # return the sum
        
        # 3. if not return 0
        return 0