# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        rhead = None
        curr = head
        length = 0
        while curr:
            tmp = ListNode(curr.val, rhead)
            rhead = tmp
            curr = curr.next
            length += 1

        dummy = ListNode(0, head)
        for i in range(length):
            if i % 2 == 0:
                tmp = head.next
                head.next = rhead
                head = tmp
            else:
                tmp = rhead.next
                rhead.next = head
                rhead = tmp
        
        head = dummy.next
        for i in range(length - 1):
            head = head.next
        head.next = None
