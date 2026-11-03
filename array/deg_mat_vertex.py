'''
strategy to be used here:
    - brute force

complexity:
    - O(n^2)time and O(n) space
'''

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []

        for i in matrix:
            count = 0
            for j in i:
                if j:
                    count += 1
            res.append(count)

        return res

'''
strategy to be used here:
    - row sum

complexity:
    - O(n) time and O(n) space

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]
'''
