class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        flag = 0
        result = 0
        curr = 0

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                curr = curr + 1 if flag == -1 else 1
                flag = 1
            elif arr[i] < arr[i + 1]:
                curr = curr + 1 if flag == 1 else 1
                flag = -1
            else:
                curr = 0
                flag = 0

            result = max(result, curr)

        return result + 1
                