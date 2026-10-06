'''
strategy to be used here:
    - two pointers

complexity:
    - O(n) time and O(1) space
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        # 1. set two pointers
        slow, fast = head, head

        # 3. run loop check emptiness of fast and its edge
        while fast and fast.next:
            # slow = slow.next
            fast = fast.next.next

        # 2. return the slower
        return slow 