'''
strategy to be used here is: 
    - two pointers: 
        - slow marks bound of unique so far; fast looks ahead
        --> bound slow at 0
        --> for fast in rest array
            --> if slow and fast aren't same; increment slow by 1
                --> at nums, value at index slow becomes index fast 
            --> return slow + 1 
            --> if empty return "" 
        --> return prefix
        --> if nums empty return 0

complexity:
    - O(n) time and O(1) space
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1