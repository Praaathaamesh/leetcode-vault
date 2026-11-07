'''
strategy to be used here:
    - brute force

complexity:
    - O(n x d) time and O(1) space
'''
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = 0

        for x in nums:
            if x == 0 and digit == 0:
                res += 1
                continue
            while x > 0:
                if x % 10 == digit:
                    res += 1
                x //= 10

        return res
