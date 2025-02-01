# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        # Find middle
        print("Find middle:")
        print("slow\t\t", end="")
        print_list(slow)
        print("fast\t\t", end="")
        print_list(fast)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            print("slow\t\t", end="")
            print_list(slow)
            print("fast\t\t", end="")
            print_list(fast)

        # Reverse fast list
        print("Reverse:")
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        print("'til mid\t", end="")
        print_list(head)
        print("reversed\t", end="")
        print_list(prev)

        # Reorder
        print("Reorder:")
        curr1, curr2 = head, prev
        while curr1 and curr2:
            saved1, saved2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = saved1
            curr1, curr2 = saved1, saved2

def print_list(head):
    if head == None:
        print("None")
        return
    while head.next:
        print(f"{head.val} -> ", end="")
        head = head.next
    print(head.val)


s = Solution()

n6 = ListNode(6, None)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)
ans = s.reorderList(head)
