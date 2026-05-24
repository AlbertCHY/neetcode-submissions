# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        
        def mergeTwoLists(list1, list2):
            dummy = ListNode()

            curr = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            else:
                curr.next = list2
                

            return dummy.next

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i - 1])
            dummy.next = lists[i]

        return dummy.next
