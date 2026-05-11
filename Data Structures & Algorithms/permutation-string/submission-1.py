class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        if not s1:
            return True

        n = len(s1)
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in range(len(s1)):
            arr1[ord(s1[i]) - 97] += 1
            arr2[ord(s2[i]) - 97] += 1
        if arr1 == arr2:
            return True
        
        for i in range(n, len(s2)):
            arr2[ord(s2[i - n]) - 97] -= 1
            arr2[ord(s2[i]) - 97] += 1
            print(arr1, arr2)
            if arr2 == arr1:
                return True

        return False