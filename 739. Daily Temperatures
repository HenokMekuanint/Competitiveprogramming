class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import defaultdict
        ans = []
        st = []
        distancePairs = defaultdict(int)

        for index, value in enumerate(temperatures):
            if len(st) == 0:
                st.append((index,value))
            else:
                if value > st[-1][1]:
                    while st:
                        toPop = st[-1]
                        if value <= toPop[1]:
                            break
                        distancePairs[toPop[0]] =  (index - toPop[0])
                        st.pop()
                    st.append((index,value))
                else:
                    st.append((index,value))


        for i in range (len(temperatures)):
            if i in distancePairs.keys():
                ans.append(distancePairs[i])
            else:
                ans.append(0)

        return ans
        
