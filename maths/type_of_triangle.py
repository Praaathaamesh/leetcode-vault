'''
strategy to be used here:
    - make sides vars using list indexing, check if tri then check the cases

complexity:
    - O(1) time and space
'''

from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2] # get the sides as vars

        # if sum of two sides is less than third (use or)
        if a + b <= c or b + c <= a or a + c <= b:
            return "none" # not a triangle
        
        # if triangle, check the cases
        if a == b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"