# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        left, right = head, head.next
        while right:
            middle = ListNode(math.gcd(left.val, right.val))
            left.next = middle
            middle.next = right
            left = left.next.next
            right = right.next        

        return dummy
