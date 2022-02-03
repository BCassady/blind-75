class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        smallest = float('inf')
        
        
        for price in prices:
            smallest = min(price, smallest)
            best = max(best, price-smallest)
                
        return best
                    
        