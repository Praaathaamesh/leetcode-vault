'''
strategy to be used here:
    - reverse and transpose

complexity:
    - O(n^2) time and O(1) space
'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. reverse the matrix
        matrix.reverse()

        # 2. transpose it using nested for loops
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]