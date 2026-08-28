'''
strategy to be used here:
    - make list of 26 zeros, add counts as per alphabetical index, if one return the index or -1 if not

complexity:
    - O(n) time and space
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # make a list with 26 zeros
        count = [0] * 26

        for c in s: # loop in str, add 1 to alphabetical index in countlist
            count[ord(c) - ord('a')] += 1
        for i in range(len(s)): # iterate over str
            if count[ord(s[i]) - ord('a')] == 1: # if alphabetical index count in countluist is 1, returnt that num
                return i
        return -1 # else return -1