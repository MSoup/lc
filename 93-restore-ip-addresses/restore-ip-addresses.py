class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # impossible to build a valid IP if s isn't the right length
        if len(s) < 4 or len(s) > 12:
            return []

        # build chunks
        solution = []

        def bfs(i: int, dots: int, result: str):
            if dots == 4 and i == len(s):
                solution.append(result[:-1])
            elif dots > 4:
                return
            for j in range(i, min(i+3, len(s))):
                substring = s[i:j+1]
                if int(substring) < 256 and (len(substring) > 1 and substring[0] != "0" or i == j):
                    bfs(j+1, dots+1, result + substring + ".")

        
        bfs(0, 0, "")
        return solution
