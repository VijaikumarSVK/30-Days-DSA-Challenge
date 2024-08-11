
// Question link  - https://www.geeksforgeeks.org/problems/count-the-triplets4615/1

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution:
	def countTriplet(self, arr, n):
		# code here
		
		count_triplet =0
		set_val = set(arr)
		for i in range(n-1):
		    for j in range(i+1,n):
		        sum_val = arr[i]+arr[j]
		        if sum_val in set_val:
		            count_triplet +=1

        return count_triplet

