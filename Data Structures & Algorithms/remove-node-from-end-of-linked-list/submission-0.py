# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        counter = 0
        while head:
            head = head.next
            counter += 1
        head = dummy.next
        
        curr = dummy
        for i in range(counter - n):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
        
        return dummy.next