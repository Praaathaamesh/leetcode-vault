'''
strategy to be used here:
    - fast and slow pointer --> they eventually meet if circ LL

complexity:
    - O(n) time and O(1) space
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution answer class
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # precaution
        if not head or head.next == None:
            return False

        # 1. set the slow and fast pointers
        fast = head
        slow = head

        # 3. while fast and next node of fast are non emp
        while fast and fast.next:
            # slow = slow.next # this moves one node ahead
            fast = fast.next.next # two nodes ahead
            if slow == fast:
                return True 

        # 2. if loop is not traversed, return false
        return False
