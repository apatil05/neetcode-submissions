class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #approach
        """
        We need two pointers, the width of the tank will be the difference 
        between the two pointers,and for each of the possible pointer 
        arrangements we will calculate area by taking the min of the two 
        numbers stored at the index, and multiplying it by the width

        For each column we need to find the index of the farthest column
        with height >= our first cols height

        Must use an approach that does not sort the array first, 
        and that can do it in one pass

        
        """

        pt1 = 0
        pt2 = len(heights) - 1
        maxArea = 0
        while pt2 != pt1:
            width = pt2 - pt1
            height = min(heights[pt1], heights[pt2])
            area = width * height
            maxArea = max(maxArea, area)
            
            if heights[pt1] < heights[pt2]:
                pt1+=1
            else:
                pt2-=1
            
        return maxArea

        
        


        