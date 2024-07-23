class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        total = 0
        current_number = 0
        sign = 1

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
                print("curr num is", current_number)
            elif char == "+":
                # we completed a number
                total += current_number * sign
                sign = 1
                current_number = 0
            elif char == "-":
                total += current_number * sign
                sign = -1
                current_number = 0
            elif char == "(":
                # start a new 'call stack'
                stack.append([total, sign])
                total = 0
                sign = 1
            elif char == ")":
                prev_total = stack.pop()
                total += current_number * sign
                total *= prev_total[1]
                total += prev_total[0]

                current_number = 0

        return total + current_number * sign