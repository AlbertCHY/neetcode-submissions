class Solution:
    def countBits(self, n: int) -> List[int]:
        index = 1
        result = []
        result.append(0)

        while index <= n:
            tmp = len(result)
            for i in range(tmp):
                result.append(1 + result[i])
            index += tmp

        return result[:n + 1]
