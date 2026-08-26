'''
strategy to be used here:
    - hashmap and reference
complexity:
    - O(1) time and space
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        # design the hashmap of list with nested tuples as int and sym (substratced instances too)
        val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = '' # string btw and we are returning this 
        for value, symbol in val_sym: # iterate over both int and sym eles in hashmap
            count = num // value # find how many times we need to add the symbol (floor div num with int)
            result += symbol * count # repeat add those syms required times (repeat add sym by count of times)
            num -= value * count # repeat reduce the num by ints added in last step (repeat subs int value by count of times)
        return result