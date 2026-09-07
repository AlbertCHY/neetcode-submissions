class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def findparent(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.findparent(x1), self.findparent(x2)
        if p1 != p2:
            self.parent[p2] = p1
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {}

        for userIndex, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(userIndex, emailToAccount[email])
                else:
                    emailToAccount[email] = userIndex

        emailGroup = defaultdict(list)
        for email, userIndex in emailToAccount.items():
            leader = uf.findparent(userIndex)
            emailGroup[leader].append(email)

        result = []
        for userIndex, emails in emailGroup.items():
            name = accounts[userIndex][0]
            result.append([name] + sorted(emailGroup[userIndex]))
        return result

        