
// Question link  - https://www.geeksforgeeks.org/problems/row-with-minimum-number-of-1s5430/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

// youtube link - https://www.youtube.com/@VijaiTheAnalyst

// Solution


class Solution:
    def minRow(self,n,m,a):
        #code here
        
        index = 1
        min_val = m
        
        for i in range(n):
            row_sum = sum(a[i])
            
            if row_sum < min_val:
                min_val = row_sum
                index = i+1
        return index
                
