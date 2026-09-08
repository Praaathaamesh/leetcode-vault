'''
strategy to be used here:
    - extra space as int

complexity:
    - O(n) time and space
'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [0] * n # temp binary array of len(nums)
        for i in range(n):
            tmp[(i + k) % n] = nums[i] # at tmp index (handle k > n cases) is nums idx will be

        nums[:] = tmp # make nums as tmp