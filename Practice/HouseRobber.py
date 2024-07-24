def houseRobberI(nums): 
  n = len(nums)
  dp = [0] * (n + 1) # Initialize a dp array to store the maximum amount that can be robbed till that house
  dp[0] = 0  #Base case, no houses, no money
  dp[1] = nums[0] #If only 1 house, rob it. 
  for i in range(2, n+1): 
    steal = nums[i-1] + dp[i-2] #Steal from the current house and add it to the amount robbed till the i-2th house
    skip = dp[i-1] #Skip the current house and take the amount robbed till the i-1th house
    dp[i] = max(steal, skip) #Find the maximum of the two options and store it in the dp array
  return dp[n] #Return the maximum amount that can be robbed till the last house

def HouseRobberII(nums): 
  if len(nums) == 0: return 0
  if len(nums) == 1: return nums[0]
  if len(nums) == 2: return max(nums)
  return max(houseRobberI(nums[:-1]), houseRobberI(nums[1:]))
