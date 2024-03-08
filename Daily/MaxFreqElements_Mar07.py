# Description : 
# You are given an array nums consisting of positive integers. Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Create frequency array 
        freq = dict(Counter(nums))
        # Find max element 
        maxFreq = max(freq.values())
        ans = 0 
        # Update ans when you find the match
        for k,v in freq.items(): 
            if v == maxFreq: 
                ans += v
        return ans 
