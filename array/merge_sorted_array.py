'''
strategy to be used:
    - Two pointers from the back

complexity:
    - O(m+n) time; O(1) space
'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1 # last position in entire nums1
        p1 = m - 1 # last real element in nums1 (non-zeros)
        p2 = n - 1 # last real element in entire nums2

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums1[p2]
                p2 -= 1

            p -= 1