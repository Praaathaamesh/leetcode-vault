'''
strategy to be used here:
    - math prop (perfect square is addition of consecutive odd nums)
    - for eg 9 = 1 + 3 + 5 

complexity:
    - O(sqrt(n)) time and O(1) space
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 1. set odd iterable going from 1 to 3, 5, and so on
        i = 1

        # 2. while num is positive
        while num > 0:
            num -= i # reduce i from num till it goes 0 
            i += 2 # increment 2 to keep the i odd
        
        # 3. check and return the identity
        return num == 0