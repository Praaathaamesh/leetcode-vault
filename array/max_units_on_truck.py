'''
strategy to be used here:
    -  sort rev and calculate

complexity:
    - O(log n) and O(1) space
'''

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # 1. sort the boxes reverse as per units
        boxTypes.sort(key = lambda x: x[1],  reverse = True)

        # 2. set result max unit var
        max_units = 0

        # 4. iterate over boxes and units using for loop
        for boxes, units in boxTypes:
            # 5. if trucksize is 0 stop the count
            if truckSize == 0:
                break
            
            # 6. fit a box, increment result var and decrement truckSize by count, each loop
            # 7. set count var which counts the avail option
            count = min(boxes, truckSize) # min of them as count
            max_units += count * units
            truckSize -= count

        # 3. return the result var
        return max_units