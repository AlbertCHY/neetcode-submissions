# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        def reverser(start):
            prev, curr = None, start

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev

        dummy = ListNode(0)
        dummy.next = head
        beforeLeft = dummy

        for _ in range(left - 1):
            beforeLeft = beforeLeft.next

        reverseHead = beforeLeft.next
        reverseTail = reverseHead
        for _ in range(right - left):
            reverseTail = reverseTail.next

        afterRight = reverseTail.next
        reverseTail.next = None
        newHead = reverser(reverseHead)
        beforeLeft.next = newHead
        reverseHead.next = afterRight

        return dummy.next
        

        