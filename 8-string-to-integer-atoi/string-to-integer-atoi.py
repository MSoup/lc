class Solution:
    def get_result(self, result, sign):
        MAX_INT = 2_147_483_647
        NEGATIVE_MAX_INT = -2_147_483_648

        result = result * sign
        if result > MAX_INT:
            return MAX_INT
        if result < NEGATIVE_MAX_INT:
            return NEGATIVE_MAX_INT
        return result

    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        sign = 1
        result = 0
        while i < len(s) and s[i] == " ":
            i += 1

        # sign switch
        if i < len(s) and s[i] in "+-":
            sign = 1 if s[i] == "+" else -1
            i += 1

        while i < len(s):
            # stop
            if not s[i].isdigit():
                return self.get_result(result, sign)
            else:
                result = result * 10 + int(s[i])
            i += 1
        return self.get_result(result, sign)

    