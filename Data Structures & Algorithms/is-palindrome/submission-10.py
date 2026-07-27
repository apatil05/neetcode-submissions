class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = s.lower()
        pt1 = 0
        pt2 = len(chars)-1
        while pt1 <= pt2:
            while pt1 < len(chars) and chars[pt1].isalnum() == False:
                pt1+=1
            while pt2>=0 and chars[pt2].isalnum() == False:
                pt2-=1
            if pt1 < len(chars) and pt2 >=0 and chars[pt1] != chars[pt2]:
                return False
            else:
                pt1+=1
                pt2-=1
        return True
