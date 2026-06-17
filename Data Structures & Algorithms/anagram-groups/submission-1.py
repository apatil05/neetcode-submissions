class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        answer = []
        for word in strs:
            wrd_array = sorted(word)
            anagrams[tuple(wrd_array)].append(word)

        for anagram in anagrams.values():
            answer.append(anagram)
        
        return answer
        