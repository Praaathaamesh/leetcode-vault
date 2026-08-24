'''
strategy to be used here:
    -  ascii mapping

complexity:
    - O(log n) time and O(n) space
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        results = []

        while columnNumber > 0:
            columnNumber = columnNumber - 1
            results.append(chr(ord('A') + columnNumber % 26))
            columnNumber = columnNumber // 26
        
        return ''.join(reversed(results))