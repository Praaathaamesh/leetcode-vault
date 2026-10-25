'''
strategies to be used here:
    - div math, return n if even else n by 2

complexity:
    - O(1) time and O(1) space
'''

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2