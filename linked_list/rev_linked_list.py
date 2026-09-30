'''
strategy to be used here:
    - iterate and shift

complexity:
    - O(n) time and O(1) space
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 1. set data nodes current and previous
        prev = None
        curr = head

        # 3. while current has value in data node: 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 2. return the previous node
        return prev