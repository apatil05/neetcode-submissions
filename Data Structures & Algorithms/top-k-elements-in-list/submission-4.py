class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        #We have established a count for each number, could just sort the list, then return the k slice
        sortedCount = sorted(count.items(), key = lambda item: item[1], reverse = True)
        return [item[0] for item in sortedCount[:k]]