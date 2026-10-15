'''
strategy to be used here:
    - count bitlength, use mask and xor it
complexity:
    - O(log num) time and O(1) space
'''

class Solution:
    def findComplement(self, num: int) -> int:
        # 1. find bit length
        num_bit_len = num.bit_length()

        # 2, create mask
        mask = (1 << num_bit_len) - 1

        # 3. return xor of num and mask
        return num ^ mask