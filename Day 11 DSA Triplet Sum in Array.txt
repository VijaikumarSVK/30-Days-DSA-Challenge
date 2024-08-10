
// Question link  - https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution:
    def find3Numbers(self, arr, n, x):
        # Your Code Here
        
        arr.sort()
        for i in range(n-2):
            left = i +1
            right = n-1
            
            while left < right:
                
                sum_val = arr[i]+arr[left]+arr[right]
                
                if sum_val == x:
                    return 1
                elif sum_val < x:
                    left +=1
                else :
                    right -=1
        return 0


