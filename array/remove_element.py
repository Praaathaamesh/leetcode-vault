'''
strategy to be used here is: 
    - binary search: 
        - left as leftmost idx and right as rightmost idx
        --> while left is smaller right
            --> calculate the middle index
            --> if nums at mid is target; return mid, less than target add 1 to left, else minus 1 by right
        --> return left

complexity:
    - O(log n) time
'''
