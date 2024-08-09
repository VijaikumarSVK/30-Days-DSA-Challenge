
// Question link  - https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&company=Amazon&sortBy=submissions

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        
        arr.sort()
        temp = arr[0]
        new_lst = []
        for i in range(1, len(arr)):
            if temp == arr[i]:
                new_lst.append(arr[i])
                temp = arr[i]
            else:
                temp = arr[i]
        if len(new_lst) >0:
            new_lst = list(set(new_lst))
            new_lst.sort()
            return new_lst
        else:
            return [-1]