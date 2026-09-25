'''
strategy to be used here:
    - iteration + even nums divisible by 3 are multiples of 6

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        # 1. set sums and counts var
        total_sum = 0
        count = 0

        # 3. if number in nums is div by 6 add num to total_sum and one increment count
        for num in nums:
            if num % 6 == 0:
                total_sum += num
                count += 1

        # 2. return 0 if count is 0; if not 0, return floor div of total_sum by count
        return 0 if count == 0 else total_sum // count