'''
strategy to be used here:
    - hash set

complexity:
    - O(n) time and O(n) space
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 1. define hashset and streak count variable
        numset = set(nums)
        count = 0

        # 3. check the occurance
        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                count = max(length, count) 

        # 2. return longest streak count
        return count