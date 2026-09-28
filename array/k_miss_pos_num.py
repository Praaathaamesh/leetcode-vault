'''
strategy to be used here:
    - binary search

complexity:
    - O(log n) time and O(1) space
'''

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        # 1. set pointers
        l = 0
        r = len(arr) - 1

        # 2. while l <= r
        while l <= r:
            # 3. find mid
            mid = (l + r) // 2
            # 4. find missing num
            missing = arr[mid] - (mid+1)

            # 5. if missing num < k; 
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        
        # 6. return left + k
        return l+k