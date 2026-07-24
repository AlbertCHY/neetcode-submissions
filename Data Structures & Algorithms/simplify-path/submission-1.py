class Solution:
    def simplifyPath(self, path: str) -> str:
        result = deque()

        idx = 0
        while idx < len(path):
            tmp = []
            while idx < len(path) and path[idx] == "/":
                idx += 1
            if idx != len(path):
                tmp.append("/")
            while idx < len(path) and path[idx] != "/":
                tmp.append(path[idx])
                idx += 1
            tmp = "".join(tmp)
            if tmp == "/..":
                if result:
                    result.pop()
            elif tmp == "/.":
                continue
            else:
                result.append(tmp)
        result = "".join(result)
        return result if result else "/"
