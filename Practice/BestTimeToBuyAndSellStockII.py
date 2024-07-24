def BestTimeToBuyAndSellStockII(prices):
    n = len(prices)  # Get the number of days
    # Create a DP table to store the maximum profit at each day
    # dp[i][0] -> Max profit on day i, if we do not have a stock
    # dp[i][1] -> Max profit on day i, if we hold a stock
    dp = [[-1 for i in range(2)] for _ in range(n+1)]  
    dp[n][0] = dp[n][1] = 0  # Base case: no profit on the day after the last day

    # Iterate backward through the days
    ind = n - 1
    while ind >= 0:
        # For each day, consider the two possibilities: buy or not buy
        for buy in range(2):
            if buy:  # If we buy a stock today
                # Profit is either from buying today and selling later (-prices[ind] + dp[ind+1][0])
                # or not buying today and sticking with previous decision (0 + dp[ind+1][1])
                profit = max(-prices[ind] + dp[ind+1][0], 0 + dp[ind+1][1]) 
            else:  # If we don't buy a stock today
                # Profit is either from selling today if we held a stock (prices[ind] + dp[ind+1][1])
                # or not selling today and sticking with previous decision (0 + dp[ind+1][0])
                profit = max(prices[ind] + dp[ind+1][1], 0 + dp[ind+1][0])
            dp[ind][buy] = profit  # Store the max profit for this day and this buying decision
        ind -= 1
    # The final answer is the maximum profit on the first day when we don't hold a stock
    return dp[0][1]  
