'''
strategy to be used here:
    - two-pointers

complexity:
    - O(n+m) time and space
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0 # initialise two pointers
        results = [] # empty list for storing chars
        while i < len(word1) and j < len(word2):
            results.append(word1[i])
            results.append(word2[j])
            i += 1
            j += 1

        # append remaining chars
        results.append(word1[i:])
        results.append(word2[j:])

        # retrun joined chars as a string
        return ''.join(results)