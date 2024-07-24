class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []


        solution = []
        dots = 0
        
        # no valid IP until we reach end of string 
        # and 3 dots have been placed

        # also we need all valid IPs
        def explore(i: int, dots: int, running_result: str):
            if i == len(s) and dots == 4:
                solution.append(running_result[:-1])
                return
            elif dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))):
                substring = s[i:j+1]
                # check substring
                if int(substring) < 256 and (i == j or s[i] != "0"):
                    # valid path
                    explore(j+1, dots+1, running_result + substring + ".")
        
        explore(0,0,"")
        return solution