'''
strategy to be used here:
    - two pointers from the end

complexity:
    - O(n) time, O(1) space
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0 or carry:
            # get digits (or 0 if exhausted)
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # add and compute carry
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            
            # append digit to result
            result.append(str(digit))
            
            # move pointers
            i -= 1
            j -= 1
        
        # result was built in reverse, so reverse it back
        return ''.join(reversed(result))