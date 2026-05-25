# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def counter(root):
            

            if not root:
                return 0
            left = counter(root.left)
            right = counter(root.right)
            self.result = max(self.result, left + right)

            return 1 + max(left, right)

        counter(root)
        return self.result