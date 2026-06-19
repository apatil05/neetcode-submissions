class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range (len(nums)):
                if j==i:
                    continue
                else:
                    product*=nums[j]
            output[i] = product
        return output
