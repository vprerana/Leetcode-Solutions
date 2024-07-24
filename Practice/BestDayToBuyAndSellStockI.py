class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the minimum buying price and maximum profit
        mini = prices[0]  # Start with the assumption that the first day is the best to buy
        maxProfit = 0     # No profit initially

        # Iterate through the stock prices starting from the second day
        for i in range(1, len(prices)):  
            # Calculate the potential profit if we buy at the minimum price seen so far and sell today
            cost = prices[i] - mini 

            # Update the maximum profit if we find a better profit today
            maxProfit = max(maxProfit, cost)

            # Update the minimum buying price if we find a lower price today
            mini = min(mini, prices[i])

        # Return the maximum profit achieved
        return maxProfit 
