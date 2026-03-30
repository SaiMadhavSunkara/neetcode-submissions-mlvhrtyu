class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                prof = prices[j] - prices[i]
                profit = max(profit, prof)
            else:
                i = j
            j += 1
        return profit

        

        

