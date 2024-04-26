class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        ans = list(s)
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else: # both are vowels
                ans[left], ans[right] = ans[right], ans[left]
                left += 1
                right -= 1
        return "".join(ans)
