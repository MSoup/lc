class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s) - 1):
            j = i + 1
            if s[i] != s[j]:
                # We found a 10 or 01, expand
                left, right = i, j 
                leftMarker, rightMarker = s[left], s[right]
                
                total += 1
                while left > 0 and right < len(s) - 1 and s[left] == leftMarker and s[right] == rightMarker:
                    left -= 1
                    right += 1
                    if s[left] == leftMarker and s[right] == rightMarker:
                        total += 1  
                # at this point we hit an end OR we know that s[left] == s[right]

        return total
