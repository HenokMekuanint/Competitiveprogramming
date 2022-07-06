class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans =[]
        intervals.sort()
        ans.append(intervals[0])
        for i in range (len(intervals)):
            if ans[-1][-1] >= intervals[i][0]:
                    if ans[-1][-1] <= intervals[i][1]:
                         ans[-1][-1] = intervals[i][1]
                    else:
                        continue
            else:  
                ans.append(intervals[i])
        return ans 
