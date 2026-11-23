class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        prev = self.head
        while index != 0 and curr.next:
            curr = curr.next
            prev = prev.next
            index -= 1
        if index != 0 or not curr:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        oldHead = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = oldHead

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        curr = self.head.next
        prev = self.head
        while index != 0 and curr.next:
            curr = curr.next
            prev = prev.next
            index -= 1
        if index != 0 or not curr:
            return False
        prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
