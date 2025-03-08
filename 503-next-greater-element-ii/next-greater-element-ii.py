class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        # len(nums) = 5
        # i = 4
        # len(nums) - i - 1 == j

        s = []
        for i in range(len(nums) * 2):
            idx = i % len(nums) 
            while s and nums[idx] > nums[s[-1]]:
                top = s.pop()
                res[top] = nums[idx]
            
            s.append(idx)

        return res


        # found = False

        # for j in range(len(nums)):
        #     curr_num = nums[j]
        #     found = False
        #     for i in range(j, len(nums)):
        #         next_num = nums[i]
        #         if next_num > curr_num:
        #             res[j] = next_num
        #             found = True
        #             break
        #     for i in range(0,j):
        #         if found == True:
        #             break
        #         next_num = nums[i]
        #         if next_num > curr_num:
        #             res[j] = next_num
        #             break
        
        # return res

