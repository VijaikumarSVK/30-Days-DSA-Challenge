
// Question link  - https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1

// youtube link - https://www.youtube.com/@VijaiTheAnalyst

// Solution

 def rotateby90(self,a, n): 
        # code here
        
        for i in range(n):
            a[i].reverse()
        
        for i in range(n):
            for j in range(0,i):
                a[i][j],a[j][i] = a[j][i],a[i][j]
       
        return a

