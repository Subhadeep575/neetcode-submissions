class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if (char.isalnum()):
                newStr += char
        newStr = newStr.lower()
        right = len(newStr)-1
        for i in range(len(newStr)):
            if(newStr[i] == newStr[right]):
                right -= 1
            else:
                return False
        return True