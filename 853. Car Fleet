class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import defaultdict

        positionTimePair = defaultdict(int)
        st = []
        fleet = len(position)

        for i in range(len(position)):
            positionTimePair[position[i]] = ((target - position[i])/speed[i])
        positionTimePair = sorted(positionTimePair.items(), key = lambda t: t[0])

        for i in range(len(positionTimePair)):

            if len(st) == 0:
                st.append(positionTimePair[i][1])

            else:
                if positionTimePair[i][1] >= st[-1]:
                    while st:
                        top= st[-1]
                        if positionTimePair[i][1] < top:
                            break
                        st.pop()
                        fleet -= 1

                    st.append(positionTimePair[i][1])

                else:
                    st.append(positionTimePair[i][1])


        return fleet
        
