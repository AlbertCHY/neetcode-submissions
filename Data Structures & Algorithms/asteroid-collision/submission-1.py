class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                if not stack:
                    result.append(asteroid)
                while stack:
                    if stack[-1] + asteroid == 0:
                        stack.pop()
                        break
                    if stack[-1] + asteroid > 0:
                        break
                    stack.pop()
                    if not stack:
                        result.append(asteroid)

        return result + stack
