# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head.next:
            return head

        dummy = ListNode()
        dummy.next = cut = head
        curr = dummy
        
        while cut:
            for i in range(k):
                if not cut:
                    return dummy.next
                cut = cut.next
            end = cut
            start = curr
            curr = curr.next
            for i in range(k):
                tmp = curr.next
                curr.next = end
                end = curr
                curr = tmp
            curr = start.next
            start.next = end

        return dummy.next
            
