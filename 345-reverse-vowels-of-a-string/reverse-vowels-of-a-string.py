class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        positions = []
        for i, char in enumerate(chars):
            if char in "aeiouAEIOU":
                positions.append((char, i))
        

        i, j = 0, len(positions) - 1
        while i <= j:
            leftChar, leftIndex = positions[i][0], positions[i][1]
            rightChar, rightIndex = positions[j][0], positions[j][1]

            chars[leftIndex], chars[rightIndex] = chars[rightIndex], chars[leftIndex]

            i += 1
            j -= 1
        
        return "".join(chars)