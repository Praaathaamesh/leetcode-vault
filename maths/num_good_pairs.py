'''
strategy to be used here:
    - brute force

complexity:
    - O(n) time and O(1) space

'''

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        ans = 0
        for num in nums:
          ans += count.get(num, 0)
          count[num] = count.get(num, 0) + 1
        return ans