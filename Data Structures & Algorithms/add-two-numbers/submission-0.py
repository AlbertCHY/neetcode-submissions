# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        forward = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            if l1 and l2:
                curr.next = ListNode((l1.val + l2.val + forward) % 10)
                forward = (l1.val + l2.val + forward) // 10
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                curr.next = ListNode((l2.val + forward) % 10)
                forward = (l2.val + forward) // 10
                l2 = l2.next
            else:
                curr.next = ListNode((l1.val + forward) % 10)
                forward = (l1.val + forward) // 10
                l1 = l1.next
            curr = curr.next

        if forward != 0:
            curr.next = ListNode(forward)

        return dummy.next
                