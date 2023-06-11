class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i]=[tasks[i][0],tasks[i][1],i]
        tasks.sort(key=lambda x:x[0])
        res=[]
        time=tasks[0][0]
        min_heap=[]
        i=0
        while min_heap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(min_heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not min_heap:
                time=tasks[i][0]
            else:
                procTime,index=heapq.heappop(min_heap)
                time+=procTime
                res.append(index)
        return res
        