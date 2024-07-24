class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        current_number = 0
        sign = 1

        for char in s:
            if char.isdigit():
                # build
                current_number = current_number * 10 + int(char)
            elif char == "+":
                result += current_number * sign
                sign = 1
                current_number = 0
            elif char == "-":
                result += current_number * sign
                sign = -1
                current_number = 0
            elif char == "(":
                # init new call stack
                stack.append(result)
                stack.append(sign)

                # reset result
                result = 0
                sign = 1
            elif char == ")":
                result += current_number * sign
                result *= stack.pop()
                result += stack.pop()

                # reset
                sign = 1
                current_number = 0
        return result + current_number * sign