class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        
        stack = []
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while stack and stack[-1][0] < curr_temp:
                temp, idx = stack.pop()
                ans[idx] = i - idx
                
            stack.append([curr_temp, i])


        return ans