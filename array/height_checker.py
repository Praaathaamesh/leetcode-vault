'''
strategy to be used here:
    - sort and comapre
complexity:
    - O(nlogn) time and O(n) space
''' 

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights) # sort the list
        count = 0 # counter int var set
        for i in range(len(heights)): # use for loop to iterate over the heights arr
            if heights[i] != expected[i]: # if at i not same
                count += 1 # increment the counter

        return count # imp lol (missed it till 4th submission)