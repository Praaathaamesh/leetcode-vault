'''
strategy to be used here is: 
    - horizontal scanning: 
        - if strs empty return "" 
        --> declare prefix and take first word as answer 
        --> while check if every other one starts with it 
        --> if not chop the last char 
        --> if empty return "" 
        --> return prefix
complexity:
    - O(n.m). where n is number of strings, m is length of the shortest string
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix