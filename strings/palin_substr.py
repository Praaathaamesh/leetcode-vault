'''
strategy to be used here:
    - two pointers

complexity:
    - O(n^2) time and O(1) space
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1. define result variable
        result = 0

        # 3. iterate over s using indices
        for i in range(len(s)):
            # 4. increment result as you find odd string palindrome
            result += self.countPalin(s, i, i)
            # 4. increment result as you find even string palindrome
            result += self.countPalin(s, i, i+1)

        # 2. return the result
        return result

    # 5. use this function to find palindromes
    def countPalin(self, s, l, r):
        result = 0 # same as step 1
        # 6. while left and right pointers are within the string and at respective index, the ele are same
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 7. increment step result var
            result += 1
            # 8. approach the center
            l -= 1
            r += 1
        # 9. same as step 2
        return result
