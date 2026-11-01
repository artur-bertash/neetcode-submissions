class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastExp = float("+inf")
        profit = 0

        for p in prices:
            if p < leastExp:
                leastExp  = p
            profit = max(p - leastExp, profit)
        return profit