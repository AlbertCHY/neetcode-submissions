# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        table = {k : v for v, k in enumerate(inorder)}
        self.index = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)
            mid = table[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root


        return dfs(0, len(preorder) - 1)