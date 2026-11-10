'''
strategy to be used here:
    - brute force

complexity:
    - O(n) time and space
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total, prod = 0, 1
        while n > 0:
            digit = n % 10
            total += digit
            prod *= digit
            n //= 10

        return prod - total
        
