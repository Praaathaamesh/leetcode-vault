'''
strategy to be used here:
    - scan from the end

complexity:
    - O(n) time; O(1) space
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length