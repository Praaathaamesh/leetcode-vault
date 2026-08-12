'''
strategy to be used:
    - idk i just memorised it

complexity:
    - O(1) time and space
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]