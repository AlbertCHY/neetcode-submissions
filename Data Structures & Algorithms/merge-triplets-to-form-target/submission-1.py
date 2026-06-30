class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag1, flag2, flag3 = False, False, False

        for ai, bi, ci in triplets:
            if ai > target[0] or bi > target[1] or ci > target[2]:
                continue
            if ai == target[0]:
                flag1 = True
            if bi == target[1]:
                flag2 = True
            if ci == target[2]:
                flag3 = True


        return flag1 and flag2 and flag3