'''
strategy to be used here:
    - sort first then check the min_diff then check the adj ele pairs with same min_diff

complexity:
    - O(n logn) time and O(1) space
'''

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # first sort the array
        arr.sort()

        # find the minimum difference in all the pairs
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i]) # min of current minimum diff and diff between two adjecent eles as greater is given first

        # put all pairs of min diff as [[]]
        results = []

        # use same loop
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff: # if min diff and adjele diff is same
                results.append([arr[i], arr[i + 1]]) # append em as smaller ele first

        return results 