'''
strategy to be used here:
    - ord for alphaidxing and maths

complexity:
    - O(n) time and O(1) space

'''

class Solution:
    def reverseDegree(self, s: str) -> int:
        revdeg = 0
        for idx, char in enumerate(s):
            revdeg += (ord("z") - ord(char) + 1) * (idx+1)

        return revdeg