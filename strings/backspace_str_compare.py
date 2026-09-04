'''
strategy to be used here:
    - stack

complexity:
    - O(n+m) time and space
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(s): # create a function to create a str after backspacing
            res = [] # create empty list
            for char in s: # loop through s
                if char == "#": # if it is #
                    if res: # and result list is not empty
                        res.pop() # pop the last ele
                else:
                    res.append(char) # else add it
            return "".join(res) # return join the chars as str in result list

        return convert(s) == convert(t)  # check equality