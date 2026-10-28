'''
strategy to be used here:
    - ords and abs simple math for loop and res int

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            res += abs(ord(s[i]) - ord(s[i+1]))

        return res
        
