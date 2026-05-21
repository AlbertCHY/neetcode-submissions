"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        table = {}
        newHead = Node(0)
        newNode = newHead
        oldNode = head

        while oldNode:
            newNode.val = oldNode.val
            if oldNode.next:
                newNode.next = Node(0)
            table[oldNode] = newNode
            oldNode = oldNode.next
            newNode = newNode.next

        newNode = newHead
        oldNode = head
        while oldNode:

            newNode.random = table.get(oldNode.random)
            oldNode = oldNode.next
            newNode = newNode.next

        return newHead