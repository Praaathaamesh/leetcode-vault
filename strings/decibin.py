'''
strategy to be used here:
    - largest digit is the ans

complexity:
    - O(1) time and space
'''

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
