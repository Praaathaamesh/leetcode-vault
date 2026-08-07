'''
strategy to be used here:
    - Hash Set (make empty set, check if each num is in set, 
    then return True end the check/ add it to set and return False and end the check)

complexity:
    - O(n) time and space
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False