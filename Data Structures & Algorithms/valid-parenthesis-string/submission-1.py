class Solution:
    def checkValidString(self, s: str) -> bool:
        stars =[]
        lefts = []

        for i in range(len(s)):
            if s[i] == "(":
                lefts.append(i)
            elif s[i] == ")":
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            elif s[i] == "*":
                stars.append(i)

        while lefts and stars:
            l, s = lefts.pop(), stars.pop()
            if l > s:
                return False

        return not lefts
