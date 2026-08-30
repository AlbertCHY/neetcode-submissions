class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                arr[i] = 1
            elif i == 2:
                arr[i] = 1
            else:
                arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

        return arr[n]