'''
strategy to be used here:
    - two pointers

complexity:
    - O(n^2) time and O(1) space
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. first set the locations of the resulting substr
        residx = 0 # start idx of resulting substr 
        reslen = 0 # len of resulting substr

        # 2. set the for loop for iter over each idx i over s
        for i in range(len(s)):

            # 4. for odd len palindrome do this
            l, r = i, i # set i as l and r as i (treat i as center)
            # while l is after first idx and r is behind last index and if both char at those idx are same
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                 # expand code
                if (r - l + 1) > reslen:
                    residx = l
                    reslen = (r - l + 1)
                l -= 1
                r += 1
            
            # 5. for even len palindrome do this
            l, r = i, i + 1 # set i and i + 1  (treat i as center since both are same)
            # while l is after first idx and r is behind last index and if both char at those idx are same
            while l >= 0 and r < len(s) and s[l] == s[r]:
                 # expand code
                if (r - l + 1) > reslen:
                    residx = l
                    reslen = (r - l + 1)
                l -= 1
                r += 1
                
        # 3. return the result substr
        return s[residx: (residx + reslen) ]