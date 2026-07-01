class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)

        visited = set()
        prev = -1
        result = []
        for i in range(len(s)):
            visited.add(s[i])
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                counter = 0
                for curr in visited:
                    if freq[curr] == 0:
                        counter += 1
                if counter == len(visited):
                    result.append(i - prev)
                    prev = i
                    visited = set()

        return result
                