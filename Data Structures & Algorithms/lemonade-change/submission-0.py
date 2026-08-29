class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)

        for i in range(len(bills)):
            if bills[i] == 5:
                changes[5] += 1
            elif bills[i] == 10:
                if changes[5] <= 0:
                    return False
                else:
                    changes[5] -= 1
                    changes[10] += 1
            else:
                if changes[10] >= 1 and changes[5] >= 1 or changes[5] >= 3:
                    if changes[10] > 0:
                        changes[10] -= 1
                        changes[5] -= 1
                    else:
                        changes[5] -= 3
                else:
                    return False
        
        return True
