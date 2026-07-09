class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        result = 0
        
        while x != 0:
            curr = int(math.fmod(x, 10))
            x = int(x / 10)
            if result > MAX // 10 or result == MAX // 10 and curr > MAX % 10:
                return 0
            if result < MIN // 10 or result == MIN // 10 and curr < MIN % 10:
                return 0

            result = (result * 10) + curr


        return result