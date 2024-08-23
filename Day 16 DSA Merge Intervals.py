
// Question link  - https://leetcode.com/problems/merge-intervals/

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution


class Solution(object):
    def merge(self, intervals):

        intervals.sort()
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
        