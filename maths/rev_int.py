'''
strategy to be used here:
    - digit by digit construction

complexity:
    - O(log n) time, O(1) space

'''

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        reversed_num = 0

        # handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10

            # check for overflow BEFORE multiplying/adding
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0

            reversed_num = reversed_num * 10 + digit
            x //= 10

        return sign * reversed_num