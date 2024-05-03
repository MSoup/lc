class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ans = []
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                # if num > top of stack then we can say that it is the NEXT greater element
                # this means we can map this value to the num for the ans
                d[stack.pop()] = num

            stack.append(num)
        
        for num in nums1:
            ans.append(d.get(num, -1))
        
        return ans