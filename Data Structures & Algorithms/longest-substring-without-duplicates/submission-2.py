class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        j = 0
        seen = set()
        while j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
                longest = max(longest, j-i)
            else:
                seen = set()
                i+=1
                j=i
            
        return longest
