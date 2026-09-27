'''
strategy to be used here:
    - Optimal prefix sum

complexity:
    - O(n) time and O(1) space
'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # 1. set total sum and left sum vars
        total_sum = sum(nums)
        left_sum = 0

        # 3. iterate over each nums ele using index
        for i in range(len(nums)):
            # 4. calculate right sum
            right_sum = total_sum - left_sum - nums[i]

            # 5. if leftsum and rightsum are same, return the index
            if left_sum == right_sum:
                return i
            
            # 6. update the leftsum
            left_sum += nums[i]
        # 2. finally return -1 if the nums is not a suitable array
        return -1