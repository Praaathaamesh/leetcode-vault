'''
strategy to be used here:
    - Boyer-Moore Voting Algorithm

complexity:
    - O(n) time; O(1) space
'''

class Solution:
    def majorityElement(self, nums: list[int]):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate