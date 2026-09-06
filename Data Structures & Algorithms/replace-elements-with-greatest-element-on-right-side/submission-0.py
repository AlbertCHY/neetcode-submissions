class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        target = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = max(arr[i], target)
            arr[i] = target
            target = tmp
            
        return arr