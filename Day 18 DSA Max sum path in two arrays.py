
// Question link  - https://www.geeksforgeeks.org/problems/max-sum-path-in-two-arrays/1

// youtube link - https://www.youtube.com/@VijaiTheAnalyst

// Solution


class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        sum1, sum2, max_sum = 0,0,0
        n, m = len(arr1), len(arr2)
        i, j = 0,0
        
        while i <n and j<m:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] == arr2[j]:
                max_sum += max(sum1,sum2)+arr1[i]
                i +=1
                j +=1
                sum1 = sum2 = 0
            else:
                sum2 += arr2[j]
                j += 1
        sum1 += sum(arr1[i:])
        sum2 += sum(arr2[j:])
        max_sum += max(sum1, sum2)
        return max_sum