'''
strategy to be used here:
    - brute force using range and for loop and or

complxity:
    - O(n) time and O(1) space
'''

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(3, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total