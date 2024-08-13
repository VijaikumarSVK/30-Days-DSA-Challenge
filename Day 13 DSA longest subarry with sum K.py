
// Question link  - https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        dictionary = {0:-1}
        val = 0
        res = 0
        
        for i in range(n):
            val += arr[i]
            if val not in dictionary:
                dictionary[val]=i
            if (val -k) in dictionary:
                res = max(res, i -dictionary[val-k])
        return res