'''
strategy to be used here:
    - brute force

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # 1. max len and curr len var set
        max_len = 1
        curr_len = 1
        
        # 3. iterate from secound char
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1: # if curr is immediate successor of prev ascii diff
                curr_len += 1 # if consecutive, increment 
                max_len = max(max_len, curr_len) # update max_len between it and curr_len
            else:
                curr_len = 1 # reset curr

        # 2. return the max len var
        return max_len