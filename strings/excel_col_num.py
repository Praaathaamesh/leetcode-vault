'''
strategy to be used here:
    - formula for convert the title to num, no use list

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result = result * 26
            result += ord(char) - ord('A') + 1

        return result