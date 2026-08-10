# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        preTarget = None
        target = root

        while target and target.val != key:
            preTarget = target
            if key > target.val:
                target = target.right
            else:
                target = target.left

        if not target:
            return root

        if not target.left or not target.right:
            child = target.left if target.left else target.right
            if not preTarget:
                return child
            if preTarget.left == target:
                preTarget.left = child
            else:
                preTarget.right = child
        else:
            targetLeft = target.left
            child = target.right
            tmp = child
            while tmp.left:
                tmp = tmp.left
            tmp.left = targetLeft
            if not preTarget:
                return child
            if preTarget.left == target:
                preTarget.left = child
            else:
                preTarget.right = child

        return root

        