class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #approach
        """
        Then for each number we have in our array "nums"
        we scan through the remainder of the array and find combinations 
        of numbers that add to the negative of the original number

        Must use some sort of set to remove dupes

        maybe run 2sum with some sort of target for the rest of the 
        values in the array, with the target value of 2 sum being the number
        that will negate the original number in the index

        So for each number in our original array, we run 2 sum for the specified target
        through the rest of the array, and then store those indicies in a triplet,
         which we will then return at the end
        """
        nums.sort()
        res = set()
        
        for i in range(len(nums)):
            target = -nums[i]
            pt1 = 0
            pt2 = len(nums)-1
            
            while pt1 < pt2:
                if pt1 == i:
                    pt1 += 1
                if pt2 == i:
                    pt2 -= 1
                
                if pt1 >= pt2:
                    break
                
                current_sum = nums[pt1] + nums[pt2]
                
                if current_sum == target:
                    sortedTup = tuple(sorted([nums[i], nums[pt1], nums[pt2]]))
                    res.add(sortedTup)
                    pt1 += 1
                    pt2 -= 1
                elif current_sum < target:
                    pt1 += 1
                else:
                    pt2 -= 1
        
        res = [list(i) for i in res]
        return res
