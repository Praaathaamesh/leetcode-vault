'''
strategy to be used here:
    - sorting using counter

complexity:
    - O(n log n) time and O(n) space
'''

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # 1.  count the char freq
        count = Counter(s)

        # 3. before, sort the chars by freq
        sorted_chars = sorted(s, key = lambda x: (-count[x], x))
        
        # 2. return that as str
        return ''.join(sorted_chars)