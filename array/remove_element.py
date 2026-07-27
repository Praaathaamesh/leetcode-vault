'''
strategy to be used here is: 
    - Two pointers: 
        - slow as a write pointer keeping the idx of next value to keep
        --> fast pointer checks entire array
            --> if not same as val, keep it and copy to slow, advance slow
            --> if val; then skip, fast moves
        --> return slow

complexity:
    - O(n) time; O(1) space complexity
'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow