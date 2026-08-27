'''
strategy to be used here:
    - use for loop, check cases with if elif else add strings 

complexity:
    - O(n) time and O(1) space

'''
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = [] # empty list to add strings

        for i in range(1, n + 1): # starting from 1
            if i % 15 == 0: # check this first
                results.append("FizzBuzz")
            elif i % 3 == 0:
                results.append("Fizz")
            elif i % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(i))
    
        return results