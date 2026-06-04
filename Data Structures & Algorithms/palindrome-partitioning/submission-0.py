class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        
        def palindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(left, right, arr):
            if left == n:
                result.append(arr.copy())
                return
            if right == n:
                return

            if palindrome(left, right):
                arr.append(s[left:right + 1])
                dfs(right + 1, right + 1, arr)
                arr.pop()
            dfs(left, right + 1, arr)

        dfs(0, 0, [])
        return result