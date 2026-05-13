class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
                continue
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                result[temp] = i - temp

            stack.append(i)


        return result