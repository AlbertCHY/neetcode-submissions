class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m1, m2 = money, money
        for p in prices:
            if p <= m1:
                m1 = p
                if p <= m2:
                    m1, m2 = m2, p

        return money if m1 + m2 > money else money - m1 - m2