# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def travel(node):
            if not node:
                return

            travel(node.left)
            result.append(node.val)
            travel(node.right)

            return

        travel(root)
        return result