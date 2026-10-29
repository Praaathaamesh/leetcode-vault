'''
strategy to be used here:
    - brute force

complexity:
    - O(n) time and space
'''

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]
