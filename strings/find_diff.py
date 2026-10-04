'''
strategy to be used here:
    - two hash maps

complexity:
    - O(n) time and O(1) space
'''

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str):
        # 1. set double hashmap
        set_t, set_s = Counter(t), Counter(s)

        # 2. if c in set t, is not in set s or its freq in s is less than freq in t, return c
        for c in set_t:
            if c not in set_s or set_s[c] < set_t[c]:
                return c