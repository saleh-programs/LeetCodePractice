class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(
            filter(lambda x: (ord(x) >= 97 and ord(x) <= 122) or (ord(x) >= 48 and ord(x) <= 57), s.lower()))

        return s == s[::-1]