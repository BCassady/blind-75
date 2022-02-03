from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                unique = True
                current_sub = s[i:j]
                if j-i > longest_sub:
                    occurences = defaultdict(int)
                    for c in current_sub:
                        if(occurences[c] == 1):
                            unique = False
                            break
                        else:
                            occurences[c] = 1
                    if unique:
                        longest_sub = j-i
                    else:
                        break
                    
        return longest_sub