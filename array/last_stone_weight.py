'''
strategy to be used here:
    - sort check the current and append

complexity:
    - O(n^2 logn) time and O(n or 1) space
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            curr = stones.pop() - stones.pop()
            if curr:
                stones.append(curr)

        return stones[0] if stones else 0