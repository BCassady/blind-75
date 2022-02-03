class Solution:
    
    def numBits(self, num):
        count = 0
        for c in str(bin(num)):
            if c == '1':
                count += 1
        return count
    
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.numBits(i))
            
        return res