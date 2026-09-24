'''
strategy to be used here:
    - iteration

complexity:
    - O(2 * n^2) time and O(n) extra space and O(2^n) output
'''


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 1. set result nested numeric list
        result = [[]]

        # 3. for every number in nums
        for num in nums:    
            result += [subset + [num] for subset in result]

        # 2. return it!
        return result