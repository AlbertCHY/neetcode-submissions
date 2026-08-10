# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findNode(node, prev):
            if not node:
                return -1, prev
            
            if key == node.val:
                return node, prev
            if key < node.val:
                return findNode(node.left, node)
            if key > node.val:
                return findNode(node.right, node)

        dummy = TreeNode(-1, None, root)
        target, preTarget = findNode(root, dummy)
        if target == -1:
            return root

        if not target.left and not target.right:
            if preTarget.val > target.val:
                preTarget.left = None
            else:
                preTarget.right = None
            return dummy.right
        elif not target.right:
            target = target.left
        elif not target.left:
            target = target.right
        else:
            tRight = target.right
            target = target.left
            tLeft_right = target
            while tLeft_right.right:
                tLeft_right = tLeft_right.right
            tLeft_right.right = tRight

        if not preTarget:
            return target
        if preTarget.val > target.val:
            preTarget.left = target
        else:
            preTarget.right = target

        return dummy.right

        