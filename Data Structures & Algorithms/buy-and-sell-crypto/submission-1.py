class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [0] * n 
        cheapest = [0] * n # cheapest from 0 to i included
        cheapest[0] = prices[0]

        for i in range(1, n):
            cheapest[i] = min(cheapest[i - 1], prices[i])
            profit[i] = max(profit[i - 1], prices[i] - cheapest[i])
        return profit[-1]
