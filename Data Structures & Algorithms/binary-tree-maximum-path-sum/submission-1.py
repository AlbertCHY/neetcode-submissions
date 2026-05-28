# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = -float("inf")

        def dfs(node):
            if not node:
                return -float("inf")

            left = dfs(node.left)
            right = dfs(node.right)
            local_max = max(node.val, node.val + right, node.val + left)

            # if not left and not right:
            #     local_max = node.val
            # elif not left:
            #     local_max = max(node.val, node.val + right)
            # elif not right:
            #     local_max = max(node.val, node.val + left)
            # else:
            #     local_max = max(node.val, node.val + right, node.val + left)

            self.maximum = max(self.maximum, local_max, node.val + left + right)
            print(node.val, local_max)
            return local_max

        dfs(root)

        return self.maximum