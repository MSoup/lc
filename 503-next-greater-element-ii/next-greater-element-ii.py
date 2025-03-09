class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        s = [] # store indexes of elements
        for i in range(len(nums) * 2):
            _index = i % len(nums)
            while s and nums[s[-1]] < nums[_index]:
                idx_to_replace = s.pop()
                res[idx_to_replace] = nums[_index]
            if _index <= len(nums):
                s.append(_index)

        return res