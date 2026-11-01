class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0] * n        # profit if holding 
        nHold = [0] * n       # profit if no share  
        hold[0] = -prices[0]
        nHold[0] = 0
        for i in range(1, n):
            hold[i] = max(hold[i - 1], nHold[i - 1] -prices[i])
            nHold[i] = max(hold[i - 1] + prices[i], nHold[i - 1])
        return nHold[n - 1]