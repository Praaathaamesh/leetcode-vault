'''
strategy to be used here:
    - track range start to end

classification:
    - O(n) time and O(1) space
'''

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            # extend range as long as consecutive numbers continue
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            end = nums[i]
            
            # format the range
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            
            i += 1
        
        return result