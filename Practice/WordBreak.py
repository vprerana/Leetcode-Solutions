def WordBreak(s, wordDict):
  #Initialize a DP array to store if the word can be segmented or not
  dp = [False] * (len(s) + 1)
  #An empty string can always be segmented
  dp[0] = True 
  #Loop from 1 to the length of the string 
  for i in range(1, len(s) + 1):
    #For every word in the dictionary
    for word in wordDict: 
      #If the current index is greater than the length of the word and the word is present in the string
      if i >= len(word) and s[i - len(word):i] == word:
        #If the word is present, check if the remaining part of the string can be segmented or not
        dp[i] = dp[i - len(word)] or dp[i]
  #Return if the string can be segmented or not
  return dp[len(s)]

print(WordBreak('leetcode', ['leet', 'code']))
