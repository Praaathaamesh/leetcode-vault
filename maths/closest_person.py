'''
strategy to be used here:
    - brute force

complexity:
    -O(1) time and space
'''

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x) < abs(z-y):
            return 1
        elif abs(z-x) > abs(z-y):
            return 2
        else:
            return 0
