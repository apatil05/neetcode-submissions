import math
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [-math.inf for x in height]
        maxRight= [-math.inf for x in height]

        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] = max(maxLeft[i-1], height[i])
        

        for i in range(len(height)-1, -1, -1):
            if i == len(height) -1:
                maxRight[i] = height[i]
            else:
                maxRight[i] = max(maxRight[i+1], height[i])
        
        #maxRight and maxLeft are now initalized properly

        area = 0
        for i in range(len(height)):
            area += min(maxRight[i], maxLeft[i]) - height[i]

        return area