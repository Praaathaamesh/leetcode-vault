'''
strategy to be used here:
    - sorting

complexity:
    - O(n log n) time and O(1 or n) space complexity
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort the nested list beforehand
        intervals.sort(key = lambda pair: pair[0])
        # 2. define output nested list with first interval
        output = [intervals[0]]

        # 3. iterate to each interval
        for start, end in intervals:
            # 5. define last interval's end
            last_end = output[-1][1]

            # 6. if in range overlap
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else: # 7. if not in range, append
                output.append([start, end])

        # 4. return the output nested list
        return output