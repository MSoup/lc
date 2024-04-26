class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        stop_point = min(len(word1), len(word2))

        for i in range(stop_point):
            result.append(word1[i])
            result.append(word2[i])
        
        resulting_word = "".join(result)

        if i < len(word1):
            resulting_word = resulting_word + word1[i+1:]
        if i < len(word2):
            resulting_word = resulting_word + word2[i+1:]
        return resulting_word

