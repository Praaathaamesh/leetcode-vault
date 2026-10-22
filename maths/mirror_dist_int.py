'''
strategy to be used here:
    - math rev int strat and do the subs

complexity:
    - O(n) time and O(n) space
'''

class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        rev = 0

        while n > 0:
            digit = n % 10
            rev = (rev * 10) + digit
            n //= 10
        
        return abs(temp - rev)