'''
strategy to be used here:
    - hash set count

complexity:
    - O(n) time and O(1) space
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(stone in jewels for stone in stones)
