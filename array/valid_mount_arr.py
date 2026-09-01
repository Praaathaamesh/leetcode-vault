'''
strategy to be used here:
    - pointer for each end

complexity:
    - O(n) time and O(1) space
'''
from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # valid mountain has slight inc then peak and then dec and len(arr) >= 3
        
        #set up the len var
        n = len(arr)
        
        # check if the len is valid
        if n < 3:
            return False

        i = 0 #set pointer

        # go ahead and check if slight inc and record peak
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1 # increment it by one

        # i is index of peak then check if it is not at the start or end
        if i == 0 or i == n-1:
            return False

        # go ahead and check if slight dec after peak
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1 # increment it by one

        # if everything is right,  n-1 and i must be same
        return i == n-1
