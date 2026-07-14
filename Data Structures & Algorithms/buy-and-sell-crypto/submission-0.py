class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0

        for i in range(1, len(prices)):

            if i == 1:
                buy = prices[0]
                sell = prices[i]
            
            if buy > prices[i]:
                if i < len(prices) - 1:
                    buy = prices[i]
                    sell = prices[i + 1]
            elif sell < prices[i]:
                sell = prices[i]
                
            profit = sell - buy
            max_p = max(max_p, profit)
            
        return max_p
        