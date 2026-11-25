class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_nums = sum(1 for i in nums if i % 2 == 0)
        return [0] * even_nums + [1]*(len(nums) - even_nums)
        
