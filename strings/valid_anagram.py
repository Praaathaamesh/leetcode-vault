'''
strategy to be used here:
    - check if sorted s is same as sorted t

complexity:
    - O(nlogn) time and O(1) space
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)