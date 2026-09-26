'''
strategy to be used:
    - stack
complexity:
    - O(n) time and space
'''

class Solution:
    def minLength(self, s: str) -> int:
        # 1. set the char stack
        stack = []

        # 3. check the stack if non emp and char in string if AB or CD and pop it; else append it
        for char in s:
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()
            else:
                stack.append(char)
        # 2. return the length of the stack
        return len(stack)  