class Solution:
    def calculate(self, s: str) -> int:
        total = current_num = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                # need to start building the number
                current_num = current_num * 10 + int(char)
            elif char == "+":
                # current_num won't grow anymore
                total += sign * current_num
                current_num = 0
                sign = 1
            elif char == "-":
                total += sign * current_num
                current_num = 0
                sign = -1
            elif char == "(":
                # save current progress
                stack.append(total)
                stack.append(sign)

                sign = 1
                total = 0

            elif char == ")":
                total += sign * current_num
                total *= stack.pop()
                total += stack.pop()


                current_num = 0
        return total + current_num * sign