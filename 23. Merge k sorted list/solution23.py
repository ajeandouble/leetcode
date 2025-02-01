from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []
        head = tail = ListNode(None)

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, head))

        print(heap)

l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
l2 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
l3 = ListNode(2, ListNode(2, ListNode(4, ListNode(6, ListNode(8)))))
l4 = ListNode(2, ListNode(10, ListNode(20, ListNode(30, ListNode(40)))))
s = Solution()
s.mergeKLists([l1, l2, l3, l4])