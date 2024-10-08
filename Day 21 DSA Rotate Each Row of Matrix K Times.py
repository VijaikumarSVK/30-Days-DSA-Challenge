
// Question link  - https://www.geeksforgeeks.org/problems/left-rotate-matrix-k-times2351/1

// youtube link - https://www.youtube.com/@VijaiTheAnalyst

// Solution 1
    def rotateMatrix(self, k, mat):
        # code here
        k = k % len(mat[0])
    
        new_mat = []
        for i in mat:
            temp_lst = i[k:]+i[:k]
            
            new_mat.append(temp_lst)
        
        return new_mat

// Solution 2

    def rotateMatrix(self, k, mat):
        # code here
        k = k % len(mat[0])
        return [i[k:]+i[:k] for i in mat]


