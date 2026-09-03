'''
strategy to be used here:
    - hash map

complexity:
    - O(m+n) time and O(min(n,m)) space
'''

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if nums1 is greater than nums2 just find the intersection
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        # if nums2 size is greater
        count = {} # set up the count hash
        # for every number in num1, update the value of that number key by one
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # now we have a dict with nums as keys and their occurance as values

        result = [] # intersection list
        for num in nums2: # for every num on num2
            if num in count and count[num] > 0: # if num is in count and has more than one occurance
                result.append(num) # add that num to intersectlist
                count[num] -= 1 # reduce the count by one

        return result