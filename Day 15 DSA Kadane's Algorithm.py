
// Question link  - https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        
        max_till_now = float('-inf')
        max_end = 0
        
        for i in arr:
            max_end = max(i, i+max_end)
            max_till_now = max(max_till_now, max_end)
        
        return max_till_now