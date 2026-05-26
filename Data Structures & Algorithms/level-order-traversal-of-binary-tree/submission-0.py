# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = deque()
        stack.append(root)
        result = []

        while stack:
            level = []
            while stack:
                level.append(stack.popleft())
            tmp = []
            for i in level:
                if i.left:
                    stack.append(i.left)
                if i.right:
                    stack.append(i.right)
                tmp.append(i.val)
            result.append(tmp)

        return result
            
