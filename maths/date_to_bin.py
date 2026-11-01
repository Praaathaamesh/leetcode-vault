'''
strategy to be used here:
    - :b, and join

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(f"{int(s):b}" for s in date.split("-"))
