class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        rowIndegree, rowAdajency = self.buildIndegree(k, rowConditions)
        colIndegree, colAdajency = self.buildIndegree(k, colConditions)
        topoRowOrder = self.kahnAlgorithm(rowIndegree, rowAdajency)
        topoColOrder = self.kahnAlgorithm(colIndegree, colAdajency)
        #print(topoRowOrder, topoColOrder)
        if(len(topoRowOrder)!=k or len(topoColOrder)!=k):
            return []
        order = [[0,0] for i in range(k)]
        for i in range(k):
            order[topoRowOrder[i]-1][0]=i
            order[topoColOrder[i]-1][1]=i
        matrix = [[0 for j in range(k)] for i in range(k)]
        
        for i in range(len(order)):
            u, v = order[i]
            matrix[u][v]=i+1
        return matrix
        
    def kahnAlgorithm(self, indegree, adajency):
        queue = []
        for i, j in indegree.items():
            #print(i,j)
            if(j==0):
                queue.append(i)
        result = []
        while(len(queue)):
            n=len(queue)
            
            for i in range(n):
                node = queue.pop(0)
                result.append(node)
                for j in adajency[node]:
                    indegree[j]-=1
                    if(indegree[j]==0):
                        queue.append(j)
        return result
        
    def buildIndegree(self, k, matrix):
        
        indegree = dict()
        adajencyList = dict()
        for i in range(k):
            indegree[i+1]=0
            adajencyList[i+1]=[]
        for u, v in matrix:
            indegree[v]+=1
            adajencyList[u].append(v)
    
        return (indegree, adajencyList)
        