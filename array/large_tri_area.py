'''
strategy to be used here:
    - heron formula brute force

complexity:
    - O(n^3) time and O(1) space
'''

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        # 1. float max_area var set
        max_area = 0.0

        # 3. three for loops for the sides
        for point1 in points:
            x1, y1 = point1

            for point2 in points:
                x2, y2 = point2

                for point3 in points:
                    x3, y3 = point3

                    # calc vectors form 1 to 2 and 1 to 3
                    vec1x = x2 - x1
                    vec1y = y2 - y1
                    vec2x = x3 - x1
                    vec2y = y3 - y1

                    # area = vec prod / 2.0
                    vec_prod = vec1x * vec2y - vec2x * vec1y
                    area = abs(vec_prod) / 2.0

                    # update max area
                    max_area = max(max_area, area)

        # 2. return it
        return max_area