# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        que = deque()
        que.append(root)
        serial = []

        while que:
            curr = que.popleft()
            if not curr:
                serial.append(".")
            else:
                serial.append(str(curr.val) + " ")
                que.append(curr.left)
                que.append(curr.right)

        if not serial:
            return "."
        else:
            return "".join(serial)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue = deque()
        self.idx = 0

        def getNum(arr):
            if arr[self.idx] == ".":
                self.idx += 1
                return None
            start = self.idx
            while arr[self.idx] and arr[self.idx] != " ":
                self.idx += 1
            self.idx += 1
            return int(arr[start:self.idx])

        root = getNum(data)
        if not root:
            return None
        queue.append(TreeNode(root))
        dummy = TreeNode()
        dummy.right = queue[0]

        while queue:
            curr = queue.popleft()
            left = getNum(data)
            right = getNum(data)
            if left:
                curr.left = TreeNode(left)
                queue.append(curr.left)
            if right:
                curr.right = TreeNode(right)
                queue.append(curr.right)
            

        return dummy.right