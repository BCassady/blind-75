class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        longest = s[0]
        for chunk in range(len(s), 0, -1):
            for i in range(0, len(s)-chunk+1):
                if s[i:i+chunk] == s[i:i+chunk][::-1]:
                    longest = s[i:i+chunk]
                    break
            if longest != s[0]:
                break
        return longest
    