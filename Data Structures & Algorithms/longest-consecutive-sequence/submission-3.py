import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(list(nums))
        print(nums)
        longest = [1 for x in nums]
        for i in range(0,len(nums)):
            if nums[i] == nums[i-1] + 1:
                longest[i] = longest[i-1] + 1
            else:
                longest[i] = 1
        
        if len(nums)>=1:
            return max(longest)
        else:
            return 0

            
                