class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleantext = "".join(char for char in s if char.isalnum()).lower()
        chars = list(cleantext)
        pt1 = 0
        pt2 = len(chars)-1
        while pt1 <= pt2:
            if chars[pt1] != chars[pt2]:
                print(chars[pt1], chars[pt2])
                return False
            else:
                print(chars[pt1], chars[pt2])
                pt1+=1
                pt2-=1
        
        return True
