class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list("".join(char for char in s if char.isalnum()).lower())
        pt1 = 0
        pt2 = len(chars)-1
        while pt1 <= pt2:
            if chars[pt1] != chars[pt2]:
                return False
            else:
                pt1+=1
                pt2-=1
        
        return True
