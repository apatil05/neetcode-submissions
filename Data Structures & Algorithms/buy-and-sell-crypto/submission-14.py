
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #approach
        """
        Naive:
        for each day we can mark that as the buy date, and then scan through the rest of the array and find the max value that exceeds the buy date.  then set this as maxProfit. 
        Do this for each day, and then we return the final max profit, however this is O(N^2) runtime

        What can we do differently:
        We could instead decide to find the max on the right side of the arr.  Then after that we can 
        """
        
        maxRight = [-1 for i in prices]
        maxProfit = 0

        for i in range(len(prices)-1, -1, -1):
            if i == len(prices) -1:
                maxRight[i] = prices[i]
            else:
                maxRight[i] = max(maxRight[i+1], prices[i])
        
        print(maxRight)
        for i in range(len(prices)):
            profit = maxRight[i]- prices[i]
            maxProfit = max(profit, maxProfit)


        return maxProfit

        