class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num]+=1

        #This is the sorted dict, where key = num, and value = count.
        #Sorted by value descending.
        reverse = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        
        answer = list(reverse)[:k]

        return answer