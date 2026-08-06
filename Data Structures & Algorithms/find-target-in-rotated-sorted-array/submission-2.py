class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return midpoint

            if nums[left] <= nums[midpoint]:
                # left half is sorted
                if nums[left] <= target < nums[midpoint]:
                    right = midpoint - 1
                else:
                    left = midpoint + 1
            else:
                # right half is sorted
                if nums[midpoint] < target <= nums[right]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1

        return -1
        