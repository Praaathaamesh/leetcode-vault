'''
strategy to be used here:
    - first and last char swipe

complexity:
    - O(n) time and O(1) space
'''

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
    
        while left < right:
            # swap characters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1