class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)

        cache = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in cache:
                return cache[i]

            result = 1 + dfs(i + 1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    result = min(result, dfs(j + 1))
            cache[i] = result
            return result
        
        return dfs(0)