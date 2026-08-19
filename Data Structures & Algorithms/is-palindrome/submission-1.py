class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):

            while not isAlphaNumeric(s[l].lower()) and l < r:
                l += 1
            while not isAlphaNumeric(s[r].lower()) and l < r:
                r -= 1
            if l < r and (s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True

def isAlphaNumeric(char):
    value = ord(char)
    return (value >= 97 and value <= 122) or (value >= 48 and value <= 57)