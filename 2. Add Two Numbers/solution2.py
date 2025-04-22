from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            s = ""
            while node:
                s += str(node.val)
                node = node.next
            return int(s[::-1])
        addition = helper(l1) + helper(l2)
        dummy = ListNode()
        prev = dummy
        for val in str(addition)[::-1]:
            prev.next = ListNode(int(val))
            prev = prev.next
        return dummy.next