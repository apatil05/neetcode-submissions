class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        freq = [(freq, num) for num,freq in dic.items()]

        freq.sort(key = lambda item: item[0], reverse = True)

        return [item[1] for item in freq[:k]]
        