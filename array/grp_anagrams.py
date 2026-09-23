'''
strategy to be used here:
    - hash map

complexity:
    - O(m * n) time and space (if total space is counted) 
'''

from typing import DefaultDict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. set result hash map of lists as values
        result = DefaultDict(list)

        # 3. loop through and add the anagrams groupwise
        for s in strs:
            count = [0] * 26 # cuz 26 slphabets
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)

        # 2 return the result hashmap values as list using type conversion
        return list(result.values())