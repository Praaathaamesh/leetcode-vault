'''
strategy to be used here:
    - hash map dict and compare each char in str with next

complexity:
    - O(n) time; O(1) space
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        for i in range(len(s)):
            curr = values[s[i]]
            if i + 1 < len(s) and curr < values[s[i + 1]]:
                total -= curr
            else:
                total += curr

        return total