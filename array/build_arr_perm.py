'''
strategy to be used here:
    - brute force list comp

complexity:
    - O(n) time and space
'''
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]     
