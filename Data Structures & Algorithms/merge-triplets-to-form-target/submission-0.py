class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag1, flag2, flag3 = False, False, False

        for ai, bi, ci in triplets:
            if ai == target[0] and bi <= target[1] and ci <= target[2]:
                flag1 = True
            if bi == target[1] and ai <= target[0] and ci <= target[2]:
                flag2 = True
            if ci == target[2] and ai <= target[0] and bi <= target[1]:
                flag3 = True


        return flag1 and flag2 and flag3