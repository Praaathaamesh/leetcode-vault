'''
strategy to be used here:
    - greedy hash set

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def partitionString(self, s: str) -> int: # unique chars are subcombos
        # 1. empty set as result
        optSet = set()
        # 2. result int to keep the results
        result = 1 # since min is always
        # 4. iterate over chars of str
        for char in s:
            # 6. if char in optset, increment result var and clear the optset
            if char in optSet:
                result += 1
                optSet.clear()
            # 5. add the char to set, BUT BEFORE THAT
            optSet.add(char)
        # 3. return the result
        return result