'''
strategy to be used here:
    - hash arr

complexity:
    - O(d) time and O(1) space {d : num of digits in n}
'''

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freqmap = [0] * 10
        while n > 0:
            digit = n % 10
            freqmap[digit] += 1
            n = n // 10

        return sum(i*x for i, x in enumerate(freqmap))