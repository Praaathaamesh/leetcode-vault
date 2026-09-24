'''
strategy to be used here:
    -  sliding window

complexity:
    - O(n) time and O(m) space; m = num of unique chars of string
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. set char hashmap, left boundary of window and result int var
        char_map = {}
        l = 0
        result = 0

        # 3. iterate over the string 
        for r in range(len(s)): # r is right bound of the window
            if s[r] in char_map: # if that ele of s in map
                l = max(char_map[s[r]]+1, l) # move l to map[s[r]]+1 and update map[s[r]] with r
            char_map[s[r]] = r
            result = max(result, r-l+1) # return the longest path
        # 2. return only the result var!
        return result