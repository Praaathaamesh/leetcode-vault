'''
straategy to be used here:
    - Reverse half the number

compplexity:
    - O(log_10 n) time; O(1) space
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0  and (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        return x == reverted or x == reverted // 10