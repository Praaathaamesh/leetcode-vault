"""
strategies to be used:
    - brute force

complexity:
    - O(n) time and O(1) space
"""


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        res = 0
        for s in operations:
            if "+" in s:
                res += 1
            else:
                res -= 1

        return res
