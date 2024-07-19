class Solution: 
  def decodeWays(s): 
    '''You need to convert a set of numbers into a secret message, For example 11106 can be decoded as 
    AAJF or KJF, so total ways is 2. Given a number, find the total ways to decode it. '''
    #Check if the string is empty
    if not s or s[0] == '0':
      return 0 
      
    n = len(s)
    dp = [0] * (n+1) 
    #Initialize DP Array 

    #Ways to check an empty string or 1 character string is 1, assign it. 
    dp[0] = 1
    dp[1] = 1

    #From 2, n+1 check the oneDigit and twoDigit combinations
    for i in range(2, n + 1):
      oneDigit = int(s[i-1])
      twoDigit = int(s[i-2:i])

      if oneDigit != 0:
        dp[i] += dp[i-1}

      if 10 <= twoDigit <= 26: 
        dp[i] += dp[i-2] 

    return dp[n]
  
