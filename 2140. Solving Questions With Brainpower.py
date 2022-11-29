class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        D=[0]*len(questions)+[0]
        for i in range(len(questions)-1,-1,-1):
            pointsI,brainpowerI=questions[i]
            D[i]=max(pointsI+D[min((i+1)+brainpowerI,len(D)-1)],D[i+1])
        return D[0]
        
