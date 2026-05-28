# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        table = {val : index for index, val in enumerate(inorder)}
        self.curr = 0

        def dfs(left, right):
            if left > right:
                return None
            
            curr_val = preorder[self.curr]
            root = TreeNode(curr_val)
            pivot = table[curr_val]
            self.curr += 1
            root.left = dfs(left, pivot - 1)
            root.right = dfs(pivot + 1, right)

            return root

        return dfs(0, len(inorder) - 1)