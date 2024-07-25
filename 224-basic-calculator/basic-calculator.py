class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        # 1 - (2 + 3)
        # ignore whitespace
        
        total = 0
        operand = 0
        # sign is 1 if operator is + else -1
        sign = 1

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char in "+-":
                total += operand * sign
                sign = 1 if char == "+" else -1
                operand = 0
            elif char == "(":
                total += operand * sign
                # new stack
                stack.append([total, sign])
                
                total = 0
                sign = 1
            elif char == ")":
                total += operand * sign
                top = stack.pop()
                total *= top[1]
                total += top[0]

                operand = 0
                sign = 1
                
        return total + operand * sign