'''
strategy to be used here:
    - list comp to clean (join, for loop each char, check if chars are alnum, lower char) return identity

complexity:
    - O(n) time and O(m) space {n = inp length, m = cleaned str len}
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. list comp to str --> make sure if each char is alnum and lower the char 
        clean_str = ''.join([char.lower() for char in s if char.isalnum()])
        
        # 2. return bool of identity
        return clean_str == clean_str[::-1]