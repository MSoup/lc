class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        ans = s
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else: # both are vowels
                ans = ans[:left] + ans[right] + ans[left+1:right] + ans[left] + ans[right+1:]
                left += 1
                right -= 1
        return ans
