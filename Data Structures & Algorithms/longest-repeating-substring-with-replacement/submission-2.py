class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        windowSize = 0
        left = 0
        maxFreq = 0
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            maxFreq = max(freq[s[right]], maxFreq)

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            
            windowSize = max(windowSize, right - left + 1)
        return windowSize