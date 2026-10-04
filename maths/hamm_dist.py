'''
strategy to be used here;
    - xor op, bit count

complexity:
    - O(b) time and O(1) space {b = number of bits in binary}
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()