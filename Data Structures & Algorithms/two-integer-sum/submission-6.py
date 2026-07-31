class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}
        for i,n in enumerate(nums):
            table[n] = i
        
        for i,num in enumerate(nums):
            complement = target - num
            if complement in nums and table[complement] != i:
                if table[complement] <= i:
                    return [table[complement],i]
                else:
                    return [i, table[complement]]
        
        return None
            