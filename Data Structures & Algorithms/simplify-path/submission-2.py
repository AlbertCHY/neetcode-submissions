class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for curr in path:
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr != "." and curr != "":
                stack.append(curr)

        return "/" + "/".join(stack)