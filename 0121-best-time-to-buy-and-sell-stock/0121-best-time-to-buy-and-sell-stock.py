class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_min = [0] * len(prices)
        min_val = prices[-1]
        right_min[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > min_val: 
                right_min[i] = min_val
                min_val = prices[i]
            else: right_min[i] = min_val

        profit = 0 

        for i in range(len(right_min)):
            net_profit = right_min[i] - prices[i]
            if net_profit > profit: 
                profit = net_profit

        return profit
 
        