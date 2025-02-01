from typing import Optional


def print_list(head):
    if head == None:
        print("None")
        return
    while head.next:
        import time

        # time.sleep(0.001)
        print(f"{head.val} -> ", end="")
        head = head.next
    print(head.val)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseSubList(self, head):
        print(self.reverseSubList.__name__, f"sublist:\t{head}")
        curr_node, prev = head, None
        while curr_node:
            saved_next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = saved_next_node
        print(self.reverseSubList.__name__, f"\t\t(head: {prev}, tail: {head})")
        return (prev, head)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev_tail = dummy
        i = 0
        curr_node = head
        print(f"NODE[{i}]:\t\t{curr_node}")
        while curr_node:
            if i // k == i / k:
                curr_head = curr_node
                print(f"curr_head (i//k)\t{curr_head}")
            if i % k == k - 1:
                next_head = curr_node.next
                print(f"curr_head:\t\t{curr_head}")
                curr_node.next = None
                (curr_head, curr_tail) = self.reverseSubList(curr_head)
                print(f"curr_head:\t\t{curr_head}")
                print(f"curr_tail:\t\t{curr_tail}")
                curr_tail.next = next_head
                print(f"curr_tail.next:\t\t{curr_tail.next}")
                print(f"curr_head:\t\t{curr_head}")
                prev_tail.next = curr_head
                print(f"prev_tail.next:\t\t{prev_tail.next}")
                curr_node = curr_tail
                print(f"curr_node:\t\t{curr_node}")
                prev_tail = curr_tail
                print(f"prev_tail:\t\t{prev_tail}")
                print(f"dummy:\t\t\t{dummy}")
                print()

            curr_node = curr_node.next
            i += 1
            print(f"NODE[{i}]:\t\t{curr_node}")
        dummt

l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,None)))))
s = Solution()
s.reverseKGroup(l, 3)
