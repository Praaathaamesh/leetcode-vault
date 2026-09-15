'''
strategy to be used here:
    - iteration

complexity:
    - O(n * 4 ^ n) time and O(1) space
'''

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 1. if string is empty return empty list
        if not digits:
            return []
        
        # 2. now if digits is not empty
        # 3. define result strlist
        result = [""]

        # 4.  Define hashmap of keys tp chars
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # 5. for every digit char in digits str
        for i in digits:
            # 6. make a temp strlist
            temp = []
            # 7. for each char in result strlist
            for j in result:
                for k in digitToChar[i]: # 8. for each value at hashmap[i]
                    temp.append(j+k) # add the concat of j and k
            # 9. update res as temp
            result = temp

        # 4. in the end we are returning the result strlist
        return result