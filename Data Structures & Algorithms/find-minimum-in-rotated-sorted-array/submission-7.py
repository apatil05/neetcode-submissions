class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return nums[0]
    
        left = 0
        right = len(nums) - 1

        while left<=right:

            midpoint = (left + right) //2

            if nums[midpoint-1] > nums[midpoint]:
                return nums[midpoint]

            if nums[midpoint + 1] < nums[midpoint]:
                return nums[midpoint+1]

            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint -1