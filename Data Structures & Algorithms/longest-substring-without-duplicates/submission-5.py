class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        que = deque()
        repeat = set()
        result = 1
        que.append(s[0])
        repeat.add(s[0])

        for i in range(1, len(s)):
            if s[i] not in repeat:
                repeat.add(s[i])
                que.append(s[i])
            else:
                while que[0] != s[i]:
                    target = que.popleft()
                    repeat.remove(target)
                que.popleft()
                que.append(s[i])
            result = max(result, len(que))

        return result