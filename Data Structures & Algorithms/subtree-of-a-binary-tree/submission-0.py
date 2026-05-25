# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(head, subhead):
            if not head:
                return False
            
            if head.val == subhead.val:
                result = checker(head, subhead)
                if result:
                    return result
            return dfs(head.left, subhead) or dfs(head.right, subhead)

        def checker(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            return checker(node1.left, node2.left) and checker(node1.right, node2.right) and node1.val == node2.val

        return dfs(root, subRoot)  