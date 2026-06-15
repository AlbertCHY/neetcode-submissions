class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        table = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + "*" + word[i + 1:]
                table[tmp].append(word)

        visited = set()
        queue = deque()
        visited.add(beginWord)
        queue.append(beginWord)
        result = 1

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return result
                for j in range(len(curr)):
                    tmp = curr[:j] + "*" + curr[j + 1:]
                    for nei in table[tmp]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

            result += 1

        return 0
