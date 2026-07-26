'''
strategy to be used here is: 
    - binary search: 
        - left as leftmost idx and right as rightmost idx
        --> while left is smaller right
            --> calculate the middle index
            --> if nums at mid is target; return mid, less than target add 1 to left, else minus 1 by right
        --> return left

complexity:
    - O(log n) time
'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left 