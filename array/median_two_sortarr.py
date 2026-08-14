'''
strategy to be used here:
    - merge and find

complexity:
    - O(m+n) time
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i = 0
        j = 0

        # merge first
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        # find median
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2-1] + merged[n // 2]) / 2.0
                