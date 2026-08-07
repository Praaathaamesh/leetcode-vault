'''
strategy to be used here:
    - Greedy two pointers

complexity:
    - O(n log n + m log m) time, O(1) space)
'''

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        g_idx = 0
        satisfied = 0

        for cookie_size in s:
            if g_idx < len(g) and g[g_idx] <= cookie_size:
                satisfied += 1
                g_idx += 1

        return satisfied