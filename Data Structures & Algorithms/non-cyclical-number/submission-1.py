class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = 0
        while curr != 1:
            curr = 0
            while n > 0:
                curr += (n % 10) * (n % 10)
                n //= 10
            if curr in seen:
                return False
            seen.add(curr)
            n = curr
            
        return True