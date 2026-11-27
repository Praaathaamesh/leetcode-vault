class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        dig_sum = 0
        num = x

        while x > 0:
            dig = x % 10
            dig_sum += dig
            x //= 10

        return dig_sum if num % dig_sum == 0 else -1