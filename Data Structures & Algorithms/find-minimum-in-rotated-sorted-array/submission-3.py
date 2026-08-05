class Solution:
    def findMin(self, nums: List[int]) -> int:

        midpoint = (len(nums)-1)//2
        if len(nums) == 2:
            return min(nums[1], nums[0])
        if midpoint == 0 or midpoint == len(nums):
            return nums[midpoint]
        if nums[midpoint + 1] > nums[midpoint] and nums[midpoint-1] > nums[midpoint]:
            return nums[midpoint]
        else:
            left = self.findMin(nums[0:midpoint])
            right = self.findMin(nums[midpoint+1 : len(nums)])
            print(left, right)
            minimum = min(left,right)
            return minimum