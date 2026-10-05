'''
strategy to be used here:
    - brute force (track the max substr using prev and curr)

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 1. set result and prev var with curr as 1
        res = 0
        prev = 0
        curr = 1

        # 3. loop over 1 idx eles using for loop
        for i in range(1, len(s)):
            if s[i] == s[i-1]: 
                curr += 1
            else:
                res += min(prev, curr) # reset to the minimum
                prev = curr # change the curr
                curr = 1 # reset curr
        
        # 4. once out do the min reset final
        res += min(prev, curr)
        
        # 2. return the res
        return res