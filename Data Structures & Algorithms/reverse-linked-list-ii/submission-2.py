# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        beforeLeft, curr = dummy, head

        for _ in range(left - 1):
            beforeLeft, curr = curr, curr.next

        prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        beforeLeft.next.next = curr
        beforeLeft.next = prev

        return dummy.next

        

        