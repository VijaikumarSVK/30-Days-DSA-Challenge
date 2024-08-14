
// Question link  - https://leetcode.com/problems/majority-element/description/

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution(object):
    def majorityElement(self, nums):

        # first solution
        res = 0
        temp =0
        dictionary = {}

        for i in set(nums):
            dictionary[i] = nums.count(i)
        for i in dictionary.keys():
            if dictionary[i] > temp:
                temp = dictionary[i]
                res = i
        return res

        # Second solution
        for i in set(nums):
            if nums.count(i)> len(nums)//2:
                return i
    