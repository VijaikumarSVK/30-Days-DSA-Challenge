
// Question link  - https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1

// youtube link - https://www.youtube.com/@VijaiTheAnalyst

// Solution


	def maxProduct(self,arr, n):
	    
	    max_till_now = float('-inf')
	    first_product = 1
	    last_product = 1
	    
	    for i in range(n):
	        
	        if first_product == 0:
	            first_product = 1
	        if last_product == 0:
	            last_product = 1
	        first_product *= arr[i]
	        last_product *= arr[n-i-1]
	        
	        max_till_now = max(max_till_now, first_product, last_product)
	    return max_till_now