'''
strategies to be used here:
    - just do it cuh

complexity:
    - O(1) time and space
'''

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15 , celsius * 1.80 + 32.00]