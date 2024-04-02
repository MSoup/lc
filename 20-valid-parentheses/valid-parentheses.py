class Solution:
    def isValid(self, s: str) -> bool:
        opening_pairs = {"{": "}", "[": "]", "(":")" }
        stack = []
        for bracket in s:
            if bracket in opening_pairs:
                stack.append(bracket) 
            elif not stack or opening_pairs[stack.pop()] != bracket:
                    return False
        return stack == [] 