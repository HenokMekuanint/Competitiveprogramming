class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans=[]
        stack=[]
        temp=""
        for i in range(len(source)):
            line=list(source[i])
            for j in range(len(line)):
                if j<len(line)-1 and (line[j]+line[j+1])=="/*" and len(stack)==0:
                    stack.append([i,j+1])
                elif (line[j-1]+line[j])=="*/" and stack and stack[-1]!=[i,j-1]:
                    stack.pop()
                elif j<len(line)-1 and (line[j]+line[j+1])=="//" and len(stack)==0:
                    if temp:
                        ans.append(temp)
                    temp=""
                    break
                elif len(stack)==0:
                    temp+=line[j]
            if len(stack)==0 and temp:
                ans.append(temp)
                temp=""
        return ans
            