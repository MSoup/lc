
class CallStack:
    def __init__(self, value, sign):
        self.value = value
        self.sign = sign

class Solution:
    def calculate(self, s: str) -> int:
        current = result = 0
        sign = 1
        stack = []

        i = 0
        while i < len(s):
            current_char = s[i]
            # Accumulate number
            if s[i].isdigit():
                current = current * 10 + int(s[i])
            elif s[i] in "+-":
                # apply computation of prev
                result += sign * current
                sign = -1 if s[i] == "-" else 1
                current = 0
            elif s[i] == "(":
                # append current result then start again
                stack.append(CallStack(result, sign))
                
                # reset sign and result
                sign = 1
                result = 0
            elif s[i] == ")":
                # apply cur val to prev
                result += sign * current
                stackTop = stack.pop()
                result *= stackTop.sign
                result += stackTop.value

                current = 0
            i += 1

        return result + (sign * current)