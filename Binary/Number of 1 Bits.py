class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_rep = bin(n)
        count = 0
        for c in bin_rep:
            if c == "1":
                count += 1
        return 