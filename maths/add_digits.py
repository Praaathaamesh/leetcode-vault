'''
strategy to be used here:
    - mathematical formula 1 + (number - 1) % 9

complexity:
    - O (1) time and space
'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9