class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if (char.isalnum()):
                newStr += char
        newStr = newStr.lower()
        if( newStr != newStr[::-1]):
            return False
        return True