import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        pmin = 1e4
        dmax = 0

        for i in range(len(prices)):

            if prices[i]-pmin > dmax:
                dmax = prices[i]-pmin

            elif prices[i] < pmin:
                pmin = prices[i]
        
        return dmax