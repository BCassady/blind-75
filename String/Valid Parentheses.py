from collections import defaultdict

class Solution:
    def isValid(self, s: str) -> bool:
        correct = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                
            elif c == ")" or c == "}" or c == "]":
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if val != correct[c]:
                    return False
        
        if len(stack) > 0:
            return False
        return True
            