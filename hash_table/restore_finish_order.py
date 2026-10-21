'''
strategy to be used:
    - hash set

complexity:
    - O(n + m) time and O(m) space {n : len(order), m : len(friends)} 
'''

from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # 1. set hash set
        res = set(friends)
        # 2. return "for if in" logic list comprehension 
        return [x for x in order if x in res]