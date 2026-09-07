'''
strategy to be used here:
    - reverse the nested lists then XOR the indiv binaries

complexity:
    - O(n^2) time and O(n) space
'''

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # access the image in the nested list or matrix
        for img in image:
            img.reverse() # reverse each intlist
            for idx in range(len(img)): # here flip it using XOR with 1
                img[idx] ^= 1 # 0 or 1 in list at idx 0, 1 and 2 is XOR with 1

        return image