class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        ls = 0
        rs = sum(nums)

        for n in nums:
            rs -= n
            ans.append(abs(ls-rs))
            ls += n

        return ans
