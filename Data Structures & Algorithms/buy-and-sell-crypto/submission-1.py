class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        L, R = 0, len(prices) - 1

        while(L < R):
            while(R > L):
                if prices[L] < prices[R]:
                    profit = prices[R] - prices[L]
                    print(profit)
                    maxP = max(maxP, profit)
                R -= 1
            L += 1
            R = len(prices)-1 

        return maxP;