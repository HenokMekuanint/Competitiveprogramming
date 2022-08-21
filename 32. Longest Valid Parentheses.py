class Solution:
    def longestValidParentheses(self, string: str) -> int:
        stack=[]
        dict={")":"("}
        newarray=[]
        array=[-1 for i in range(len(string))]
        for close in range(len(string)):
            if string[close] not in dict:
                stack.append(string[close])
                newarray.append(close)
            elif stack and stack[-1]==dict[string[close]]:
                stack.pop()
                poppend=newarray.pop()


                array[poppend]=poppend
                array[close]=close
            elif len(stack)==0:
                continue
        count=0
        thirdarray=[]
        for i in range(len(array)):
            if array[i]!=-1:
                count=count+1
                if i==len(array)-1:
                    thirdarray.append(count)
            elif array[i]==-1:
                thirdarray.append(count)
                count=0
        return max(thirdarray) if len(thirdarray)!=0 else 0
