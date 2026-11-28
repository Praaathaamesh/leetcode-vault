class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        seen = set(nums)

        return [n for n in range(mn+1, mx) if n not in seen]
