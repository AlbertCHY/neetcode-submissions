class TrieNode():
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            curr = root
            for j in range(len(words[i])):
                if words[i][j] not in curr.children:
                    curr.children[words[i][j]] = TrieNode()
                curr = curr.children[words[i][j]]
            curr.wordEnd = True

        result = []
        visited = set()
        m, n = len(board), len(board[0])

        def checker(i, j, node, arr):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] not in node.children:
                return

            next_node = node.children[board[i][j]]
            visited.add((i, j))
            arr.append(board[i][j])

            if next_node.wordEnd:
                result.append("".join(arr))
                next_node.wordEnd = False

            ((i - 1, j) not in visited) and checker(i - 1, j, node.children[board[i][j]], arr)
            ((i + 1, j) not in visited) and checker(i + 1, j, node.children[board[i][j]], arr)
            ((i, j - 1) not in visited) and checker(i, j - 1, node.children[board[i][j]], arr)
            ((i, j + 1) not in visited) and checker(i, j + 1, node.children[board[i][j]], arr)
            visited.remove((i, j))
            arr.pop()
        
        for i in range(m):
            for j in range(n):
                checker(i, j, root, [])

        return result
