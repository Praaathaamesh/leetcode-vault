'''
strategy to be used here:
    - go for the k increments

complexity:
    - O(nm) time; O(n) space
'''

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        while word * k in sequence:
            k += 1
        return k - 1 