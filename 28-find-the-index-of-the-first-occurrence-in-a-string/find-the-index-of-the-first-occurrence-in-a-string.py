class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        i = 0

        while i <= len(haystack) - needleLength:
            if haystack[i] == needle[0]:
                if self.isMatch(haystack[i:i+needleLength], needle):
                    return i
                
            i += 1

        return -1
    
    def isMatch(self, str1, str2):
        if len(str1) != len(str2):
            raise Exception("Str lengths don't match") 
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        
        return True
