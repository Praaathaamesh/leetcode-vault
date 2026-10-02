'''
strategy to be used here;
    - if 0/1 at even/odd idx, then it must stick the parity --> if does incr count, else dont.
    - since s can also start with 1; instead of 0, then return len(s)-count

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def minOperations(self, s: str) -> int:
        # 1. set count var
        count = 0
        
        # 3. iterate over each idx ele of s
        for i in range(len(s)):
            if i % 2 == 0:
                count += 1 if s[i] == '0' else 0
            else:
                count += 1 if s[i] == '1' else 0

        # 2. return the min for count if it starts at 0 else len - count
        return min(count, len(s)-count)