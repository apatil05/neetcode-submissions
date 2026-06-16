class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = list(s)
        t_lst = list(t)
        s_lst.sort()
        t_lst.sort()

        if len(t_lst) != len(s_lst):
            return False
            
        for i in range(len(s_lst)):
            if s_lst[i] != t_lst[i]:
                return False
        
        return True

