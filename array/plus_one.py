'''
strategy to be used here is:
    - Traverse fro the end, handle carry
        --> start from back
            --> check if digitlist at i is less than 9
                --> advance by one
                --> return digitlist
            --> digitlist at i becomes 0
        --> return [1] + digitlist

complexity:
    - O(n) time; O(1) space
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits
                
            digits[i] = 0

        return [1] + digits